__all__ = ['main']
import requests
from newspaper import Article
import openai
from notion_client import Client
from lxml import html

def extract_article_links(url):
    article = Article(url, keep_article_html=True)
    article.download()
    article.parse()

    article_top_node = article.clean_top_node

    if article_top_node is not None:
        links = [a.get('href') for a in article_top_node.cssselect('a[href]')]
    else:
        links = []

    cleaned_links = [f"{link}" for link in links if link.startswith("http") and link != url]
    return cleaned_links


def extract_article_text(url, max_tokens=4000):
    article = Article(url)
    article.download()
    article.parse()
    article_text = article.text
    # Split the text into chunks
    chunks = [article_text[i:i+max_tokens] for i in range(0, len(article_text), max_tokens)]
    return chunks

openai.api_key = "<YOUR-KEY-HERE>"

def extract_article_title(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title

def generate_text(prompt, n=1):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        n=n,
        stop=None,
        temperature=0.7,
        logprobs=10,  # Add this line
    )
    choices = response.choices
    choices = sorted(choices, key=lambda x: sum(x.logprobs.token_logprobs) if x.logprobs and x.logprobs.token_logprobs else float("-inf"), reverse=True)
    full_text = choices[0].text.strip()

    # Remove any incomplete sentences at the beginning and end of the generated text
    sentences = full_text.split(".")
    if len(sentences) > 1:
        first_sentence = sentences[0].strip()
        if not first_sentence[0].isupper() or not first_sentence[-1].isalnum():
            full_text = full_text[len(first_sentence):].strip()

        last_sentence = sentences[-1].strip()
        if not last_sentence or not last_sentence[-1].isalnum():  # Add check for empty string
            full_text = full_text[:len(full_text) - len(last_sentence)].strip()

    # Additional cleanup
    full_text = full_text.strip(".”")
    return full_text



def generate_summary(article_chunks):
    summaries = []
    for chunk in article_chunks:
        prompt = f"Please provide an executive summary of the following news article in 3-5 sentences, clearly stating the main topic, key points, and implications:\n\n---\n{chunk}\n---\nSummary:"
        summary = generate_text(prompt)
        summaries.append(summary)
    
    # Combine the summaries of all chunks
    combined_summary = " ".join(summaries)
    return combined_summary

    prompt = f"Please provide an executive summary of the following news article in 3-5 sentences, clearly stating the main topic, key points, and implications:\n\n---\n{article_text}\n---\nSummary:"
    return generate_text(prompt)

def generate_outline(article_chunks):
    prompt = f"Please provide a comprehensive summary of the following news article in a well-organized and clearly written outline format. Focus on conveying the key information and important details about each game featured in the article. The outline should enable the reader to gain a high-level understanding of the information in the article without needing to read the full text. Keep the output to under 2000 characters.:\n\n---\n{article_chunks}\n---\n\nOutline:"
    return generate_text(prompt)

def generate_bullet_points(article_chunks):
    prompt = f"Please provide 3-5 bullet points summarizing the main points and key takeaways of the following article, ensuring they are concise and informative:\n\n{article_chunks}"
    raw_text = generate_text(prompt)
    return raw_text.replace("•", "\n•").strip()

def generate_key_quotes(article_chunks):
    prompt = f"Please provide 3-5 key quotes from the following article that represent important statements or opinions, and include the speaker's name, title (if applicable), and a brief context for the quote:\n\n{article_chunks}"
    raw_text = generate_text(prompt)
    return raw_text.replace("A.", "\n\nA.").replace("B.", "\n\nB.").replace("C.", "\n\nC.").strip()


notion = Client(auth="<YOUR-NOTION-KEY-HERE>")

def format_for_notion(text):
    formatted_text = text.replace("1.", "\n\nA.")
    formatted_text = formatted_text.replace("2.", "\n\nB.")
    formatted_text = formatted_text.replace("3.", "\n\nC.")
    formatted_text = formatted_text.replace("4.", "\n\nD.")
    formatted_text = formatted_text.replace("5.", "\n\nE.")
    return formatted_text.strip()


def create_notion_page(title, url, summary, outline, bullet_points, key_quotes, formatted_summary, formatted_outline, formatted_bullet_points, formatted_key_quotes, article_text, sources):
    # Replace the following line with the ID of the Notion database you want to use
    database_id = "<YOUR-DATABASE-ID-HERE>"

    new_page = {
        "Title": {"title": [{"text": {"content": title}}]},
        "Summary": {"rich_text": [{"text": {"content": formatted_summary}}]},
        "Outline": {"rich_text": [{"text": {"content": formatted_outline}}]},
        "Bullet Points": {"rich_text": [{"text": {"content": formatted_bullet_points}}]},
        "Key Quotes": {"rich_text": [{"text": {"content": formatted_key_quotes}}]},
        "Article URL": {"url": url},
        "Sources": {"rich_text": [{"text": {"content": sources}}]},
    }


    created_page = notion.pages.create(parent={"database_id": database_id}, properties=new_page, has_children=True)

    # Split article_text into chunks of 2000 characters or less
    article_text_chunks = [article_text[i:i + 2000] for i in range(0, len(article_text), 2000)]

    # Add content to the page's content area
    page_content = [
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "Summary"}}]
            },
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": formatted_summary}}]
            },
        },
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "Outline"}}]
            },
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": formatted_outline}}]
            },
        },
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "Bullet Points"}}]
            },
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": formatted_bullet_points}}]
            },
        },
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "Key Quotes"}}]
            },
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": formatted_key_quotes}}]
            },
        },
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "Article Text"}}]
            },
        },
    ]

    # Add the article text chunks as separate paragraph blocks
    for chunk in article_text_chunks:
        page_content.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": chunk}}]
            },
        })

        

    page_content.append({
        "object": "block",
        "type": "heading_1",
        "heading_1": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Sources and Backlinks"
                    }
                }
            ]
        }
    })

# Add the sources as separate paragraph blocks with clickable links
    for link in sources.split("\n"):
        page_content.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": link, "link": {"url": link}}
                    }
                ]
            },
        })



    # Add the content to the Notion page
    notion.blocks.children.append(created_page["id"], children=page_content)


def main(url):
    article_chunks = extract_article_text(url)

    # Store the article chunks (you can use a cache or database to store them)
    stored_article_chunks = article_chunks

    # Read the stored article chunks
    article_chunks = stored_article_chunks

    # Make separate API calls for each part of the article
    summary = generate_summary(article_chunks)

    # Replace 'article_text' with 'article_chunks' in the following three function calls
    outline = generate_outline(article_chunks)
    bullet_points = generate_bullet_points(article_chunks)
    key_quotes = generate_key_quotes(article_chunks)
    
    formatted_summary = format_for_notion(summary)
    formatted_outline = format_for_notion(outline)
    formatted_bullet_points = format_for_notion(bullet_points)
    formatted_key_quotes = format_for_notion(key_quotes)

    # Extract the title from the article text
    title = extract_article_title(url)

    # Join the article chunks into a single string
    article_text = " ".join(article_chunks)

    # Extract the links from the article
    links = extract_article_links(url)
    sources = "\n".join(f"{link}" for link in links)


    create_notion_page(title, url, summary, outline, bullet_points, key_quotes, formatted_summary, formatted_outline, formatted_bullet_points, formatted_key_quotes, article_text, sources)
    # Return the generated content as a dictionary
    return {
        'title': title,
        'url': url,
        'summary': summary,
        'outline': outline,
        'bullet_points': bullet_points,
        'key_quotes': key_quotes,
    }



if __name__ == "__main__":
    url = "https://www.npr.org/2023/03/27/1165899152/ted-lasso-brett-goldstein-shrinking"  # Replace with a URL for testing
    main(url)