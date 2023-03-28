# News Summary App

This is a Python app that generates a summary, outline, bullet points, and key quotes for a news article provided by the user. The app uses the OpenAI API to generate the content based on prompts created by the app. The generated content is then added to a Notion database.

## Getting started

### Prerequisites

Before you can use this app, you will need to have the following installed:

- Python 3.6 or higher
- pip

### Installation

1. Clone the repository: `git clone https://github.com/mrtyndall/notionsummary.git`
2. Navigate to the project directory: `cd news_summary_app`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Rename the `example.env` file to `.env` and add your OpenAI API key.

### Usage

1. Start the Flask app: `python app.py`
2. Create a new Notion database with the following properties:
   - Title (title)
   - Article URL (url)
   - Summary (rich text)
   - Outline (rich text)
   - Bullet Points (rich text)
   - Key Quotes (rich text)
   - Sources (rich text)
3. Note the ID of the database, which can be found in the database URL.
4. Navigate to `http://localhost:5000/news_summary?url=<article_url>` in your web browser or use a tool like `curl` to make a request to the app's endpoint, replacing `<article_url>` with the URL of the news article you want to summarize.
5. The app will generate a summary, outline, bullet points, and key quotes for the article and add it to the Notion database you created. The generated content will also be returned in the response body in JSON format.

## Credits

This app uses the following third-party libraries:

- [Newspaper3k](https://github.com/codelucas/newspaper/) - for article parsing
- [OpenAI API](https://beta.openai.com/docs/api-reference/) - for text generation
- [Notion API](https://developers.notion.com/) - for database integration
