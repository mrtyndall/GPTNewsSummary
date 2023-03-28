from flask import Flask, render_template, request, jsonify
from news_summary_app import main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.json['url']
        if not url:
            return jsonify({"error": "URL is required"}), 400
        result = main(url)
        formatted_result = {
            "title": result["title"],
            "summary": result["summary"].replace("\n", "<br>"),
            "outline": result["outline"].replace("\n", "<br>"),
            "bullet_points": result["bullet_points"].replace("\n", "<br>"),
            "key_quotes": result["key_quotes"].replace("\n", "<br>")
        }
        return jsonify(formatted_result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)