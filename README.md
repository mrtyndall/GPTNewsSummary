# GPTNews Summary

GPTNews Summary is a Python application that uses OpenAI's GPT-3 and the Notion API to generate summaries, outlines, bullet points, and key quotes from news articles. The generated content is then added to a Notion page, making it easy to organize and review information from various sources.

## Features

- Extract article text and links from a given URL
- Generate summaries, outlines, bullet points, and key quotes using GPT-3
- Create and populate Notion pages with the generated content

## Installation

1. Clone this repository to your local machine: git clone https://github.com/mrtyndall/GPTNewsSummary.git

2. Install the required Python libraries: pip install -r requirements.txt


## Configuration

1. Replace `<YOUR-KEY-HERE>` with your OpenAI API key in the `main.py` file.
2. Replace `<YOUR-NOTION-KEY-HERE>` with your Notion API key in the `main.py` file.
3. Replace `<YOUR-DATABASE-ID-HERE>` with the ID of the Notion database you want to use in the `main.py` file.

## Usage

GPTNews Summary can be used in two ways:

1. Running the `app.py` file, which allows you to paste a URL at your address (e.g., `example.com:5000`): 

``python app.py``

After running the script, open your web browser and go to the address where the app is hosted (e.g., `http://localhost:5000`). Enter the URL of the news article you want to summarize and click the "Submit" button.

2. Running the `shortcuts.py` file, which allows you to run the summarizer via a GET URL method with a URL formatted like `example.com/news_summary?url=example.com`: ``python shortcuts.py``

After running the script, open your web browser and go to the address where the app is hosted, followed by `/news_summary?url=` and the URL of the news article you want to summarize (e.g., `http://localhost:5000/news_summary?url=https://www.example.com/news-article`).

Both methods will generate a summary, outline, bullet points, and key quotes for the news article and create a Notion page with the generated content.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT



