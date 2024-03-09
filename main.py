from flask import Flask, request, render_template
from scrapper import get_reviews


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def handle_submit():
    form_data = request.form
    return get_reviews(form_data['url'], form_data['lang'])

if __name__ == '__main__':
    app.run(debug=True)