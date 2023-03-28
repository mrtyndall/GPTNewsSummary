# ***Introduction***

GPTNews Summary is a Python application that leverages OpenAI's GPT-3 and the Notion API to generate summaries, outlines, bullet points, and key quotes from news articles. The generated content is then added to a Notion page, simplifying the process of organizing and reviewing information from various sources.

***Contents***

Features
Installation
Configuration
Usage
Function Breakdown
Contributing
License
---

### 1. Features

The GPTNews Summary app offers a range of features designed to streamline the process of summarizing, organizing, and reviewing news articles. These features include:

- **Extract article text and links from a given URL**: GPTNews Summary uses the **`newspaper`** library to efficiently extract the main text and associated links from a given news article URL. This process removes unnecessary content such as ads, comments, and navigation elements, leaving only the core information for further processing.
- **Generate summaries, outlines, bullet points, and key quotes using GPT-3**: By leveraging the power of OpenAI's GPT-3, GPTNews Summary can create concise summaries, informative outlines, easy-to-read bullet points, and highlight key quotes from the extracted article text. GPT-3's advanced natural language understanding capabilities ensure that the generated content is coherent and relevant.
    - *Summaries*: GPTNews Summary produces succinct summaries that capture the main points and context of the article, allowing users to quickly understand the content without reading the full text.
    - *Outlines*: The app generates outlines that present the article's structure and main topics, offering users a clear roadmap of the content and making it easier to navigate.
    - *Bullet points*: GPTNews Summary creates bullet points that emphasize important details and key facts from the article, making it simple for users to review the critical information.
    - *Key quotes*: The app identifies and extracts key quotes from the article, showcasing the most compelling or significant statements for users to reference.
- **Create and populate Notion pages with the generated content**: GPTNews Summary automates the process of organizing and storing the generated summaries, outlines, bullet points, and key quotes in a Notion database. By integrating with the Notion API, the app creates new pages for each summarized article and populates them with the generated content, facilitating easy access, review, and management of the information within the Notion platform.

### 2**. Libraries and Dependencies**

GPTNews Summary relies on several Python libraries and APIs to perform its functions effectively. This section provides an overview of these libraries and how they contribute to the app's functionality.

- **OpenAI GPT-3**: GPTNews Summary uses OpenAI's GPT-3 language model to generate summaries, outlines, bullet points, and key quotes from news articles. To interact with GPT-3, the app utilizes the **`openai`** Python library, which provides an interface to OpenAI's API.
- **Notion API**: The app integrates with the Notion API to create and populate Notion pages with the generated content. The **`notion-client`** library is used to interact with the Notion API, enabling the app to authenticate, create pages, and manage content within a Notion database.
- **Newspaper3k**: The **`newspaper3k`** library is used to extract article text, links, and titles from a given URL. This library simplifies the process of obtaining the core content from news articles by automatically filtering out unnecessary elements such as ads, comments, and navigation items.
- **Flask**: The Flask web framework is used to create a lightweight web application that allows users to input a news article URL and receive the generated summaries, outlines, bullet points, and key quotes. Flask provides a simple and flexible way to build web applications in Python.
- **Requests**: The **`requests`** library is used to make HTTP requests and interact with web services, such as the OpenAI API and Notion API. This library simplifies the process of sending and receiving data over the internet.

To install the required libraries and dependencies, run the following command:

```
Copy code
pip install -r requirements.txt

```

This command will automatically install the necessary Python packages listed in the **`requirements.txt`** file. By utilizing these libraries, GPTNews Summary can efficiently perform its tasks and provide a seamless experience for users.

### 3. Installation

1. Clone this repository to your local machine:
    
    ```
    bashCopy code
    git clone <https://github.com/mrtyndall/GPTNewsSummary.git>
    
    ```
    
2. Install the required Python libraries:
    
    ```
    Copy code
    pip install -r requirements.txt
    
    ```
    

### 4. Configuration

1. Replace **`<YOUR-KEY-HERE>`** with your OpenAI API key in the **`main.py`** file.
2. Replace **`<YOUR-NOTION-KEY-HERE>`** with your Notion API key in the **`main.py`** file.
3. Replace **`<YOUR-DATABASE-ID-HERE>`** with the ID of the Notion database you want to use in the **`main.py`** file.

### 5. Usage

GPTNews Summary can be used in two ways:

1. Running the **`app.py`** file, which allows you to paste a URL at your address (e.g., **`example.com:5000`**):
    
    ```python
    python app.py
    ```
    
    After running the script, open your web browser and go to the address where the app is hosted (e.g., **`http://localhost:5000`**). Enter the URL of the news article you want to summarize and click the "Submit" button.
    
2. Running the **`shortcuts.py`** file, which allows you to run the summarizer via a GET URL method with a URL formatted like **`example.com/news_summary?url=example.com`**:
    
    ```
    python shortcuts.py
    ```
    
    After running the script, open your web browser and go to the address where the app is hosted, followed by **`/news_summary?url=`** and the URL of the news article you want to summarize (e.g., **`http://localhost:5000/news_summary?url=https://www.example.com/news-article`**).
    

Both methods will generate a summary, outline, bullet points, and key quotes for the news article and create a Notion page with the generated content.

### 6. Function Breakdown

Here's a brief explanation of each function in the news_summary_app.py script:

- **`extract_article_links(url)`**: Extracts article links from the given URL using the **`newspaper`** library.
- **`extract_article_text(url, max_tokens=4000)`**: Extracts the article text from the given URL using the **`newspaper`** library and splits the text into chunks with a maximum token count.
- **`extract_article_title(url)`**: Extracts the article title from the given URL using the **`newspaper`** library.
- `generate_text(prompt, n=1)` is a function that utilizes the OpenAI GPT-3 API to generate text from a given prompt. The function takes two arguments: `prompt`, a string containing the text prompt to generate the response from, and `n`, an optional integer specifying the number of responses to generate (default is 1).
    
    The function calls the `openai.Completion.create()` method to generate the text, which is a powerful tool that allows users to generate various types of text, such as articles, stories, summaries, and much more.
    
    One parameter of the `openai.Completion.create()` method is `engine`, which specifies the GPT-3 engine to use for text generation. In this case, the `text-davinci-003` engine is used, which is one of the most advanced and expensive models available.
    
    Another parameter is `max_tokens`, which specifies the maximum number of tokens (words) that the generated text can have. This parameter is essential because it controls the length of the generated text, which can affect the quality and coherence of the output.
    
    The `n` parameter specifies the number of responses to generate, which can be useful when trying to generate multiple versions of the same prompt or when attempting to generate text with different styles or tones.
    
    The `stop` parameter is a string or list of strings used to indicate when the response should stop generating. If `None`, the response will continue generating until the `max_tokens` limit is reached. This parameter is useful when generating text with a specific goal or objective, such as summarizing an article, creating a bullet point list, or generating a conclusion.
    
    The `temperature` parameter is a float value between 0 and 1 that controls the randomness of the generated text. A higher value will produce more random text, while a lower value will produce more predictable text. This parameter can affect the coherence and quality of the output and must be adjusted accordingly.
    
    Finally, the `logprobs` parameter is an optional integer that controls the amount of information the API returns about its prediction process. This parameter can be useful for debugging and troubleshooting purposes, but it can also slow down the text generation process.
    
    In summary, the `generate_text()` function is a powerful tool that allows users to generate high-quality text from a given prompt using the OpenAI GPT-3 API. By adjusting the various parameters of the `openai.Completion.create()` method, users can generate text with different lengths, styles, tones, and degrees of randomness, making it a versatile and flexible tool for various text generation tasks.
    
- ***Open AI API Prompts:***
    
    These four functions are critical to the functionality of the GPTNews Summary application. Each of them uses GPT-3 to generate different types of summary and key information from the news article.
    
    `generate_summary(article_chunks)` generates a 3-5 sentence summary for each chunk of text passed to it, combining them into a single string. The function uses a prompt that asks GPT-3 to provide an executive summary of the news article in 3-5 sentences, clearly stating the main topic, key points, and implications. The prompt can be customized as per the user's needs.
    
    `generate_outline(article_chunks)` prompts GPT-3 to generate a comprehensive summary of the article in a well-organized and clearly written outline format. The outline focuses on conveying the key information and important details about each game featured in the article. The output of this function is limited to under 2000 characters. The prompt can be customized as per the user's needs.
    
    `generate_bullet_points(article_chunks)` prompts GPT-3 to generate 3-5 bullet points that summarize the main points and key takeaways of the article. The function ensures that the bullet points are concise and informative. The prompt can be customized as per the user's needs.
    
    `generate_key_quotes(article_chunks)` prompts GPT-3 to generate 3-5 key quotes from the article that represent important statements or opinions. The quotes include the speaker's name, title (if applicable), and a brief context for the quote. The prompt can be customized as per the user's needs.
    
    These functions are all built on the `generate_text(prompt)` function, which is used to prompt GPT-3 to generate text based on the given prompt. The prompt can be modified to change the output of the function.
    
    By using these functions, the GPTNews Summary application can quickly summarize news articles and extract key information, making it easier to organize and review information from various sources. Additionally, the prompts can be modified to generate summaries and key information for different types of articles or documents, making the application flexible and versatile for various use cases.
    
    ---
    
- **`format_for_notion(text)`**: Formats text for compatibility with the Notion API.
- **`create_notion_page(...)`**: Creates a Notion page and populates it with the given content.
- **`main(url)`**: The main function, which ties together all the other functions. Takes a URL as input, extracts and processes the article text, generates summaries, outlines, bullet points, and key quotes, and creates a Notion page with the generated content.

### 7. Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

If you would like to contribute to the project, please submit a pull request on GitHub with your proposed changes. All contributions are welcome.

### 8. License

This project is licensed under the MIT License. 

GPTNews Summary utilizes the following third-party libraries, which are subject to their respective licenses:

- **OpenAI GPT-3**: The **`openai`** Python library is used to interact with GPT-3. Please refer to **[OpenAI's Terms of Service](https://platform.openai.com/docs/terms-of-service)** and the library's **[LICENSE](https://github.com/openai/openai/blob/master/LICENSE.txt)** for more details.
- **Notion API**: The **`notion-client`** library is used to interact with the Notion API. The library is licensed under the MIT License. Please refer to the library's **[LICENSE](https://github.com/ramnes/notion-sdk-py/blob/main/LICENSE)** for more details.
- **Newspaper3k**: The **`newspaper3k`** library is licensed under the Apache License 2.0. Please refer to the library's **[LICENSE](https://github.com/codelucas/newspaper/blob/master/LICENSE)** for more details.
- **Flask**: The Flask web framework is licensed under the BSD-3-Clause License. Please refer to Flask's **[LICENSE](https://github.com/pallets/flask/blob/main/LICENSE.rst)** for more details.
- **Requests**: The **`requests`** library is licensed under the Apache License 2.0. Please refer to the library's **[LICENSE](https://github.com/psf/requests/blob/main/LICENSE)** for more details.

Please ensure that you adhere to the terms and conditions of each library's license when using GPTNews Summary.
