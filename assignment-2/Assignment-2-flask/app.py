from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # Handle form submission here (extract information, etc.)
        # For demonstration purposes, let's assume you extract information and questions from the article ID
        article_id = request.form.get('articleId')
        extracted_info = "Information extracted from article ID {}".format(article_id)
        question = request.form.get('question')

        # Render the template with the extracted information and question
        return render_template('index.html', extracted_info=extracted_info, question=question)

    # Render the template for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
