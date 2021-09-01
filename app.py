# [Quickstart — Flask Documentation (2.0.x)](https://flask.palletsprojects.com/en/2.0.x/quickstart/#)

from flask import Flask, render_template, jsonify, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return ("<p>Hello, World!</p>"
            "<a href='./escape'>escape</a><br>"
            "<a href='./hello'>hello</a><br>"
            "<a href='./user/john do'>user: john do</a><br>"
            "<a href='./post/3'>post: 3</a><br>"
            "<a href='./hi/'>hi</a><br>"
            "<a href='./hi/god'>hi god</a><br>"
            "<a href='./incomes'>income</a><br>"
            )


@app.route("/escape")
def test_escape():
    name = 'test'
    return f"Hello, {escape(name)}!"


@app.route("/hello")
def hello():
    return "Hello, World"


@app.route("/user/<username>")
def show_user_profile(username):
    return f"User: {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post: {escape(post_id)}"


@app.route("/hi/")
@app.route("/hi/<name>")
def hi(name=None):
    return render_template('hi.html', name=name)


incomes = [
    {'description': 'salary', 'amount': 5000}
]


@app.route("/incomes")
def get_incomes():
    return jsonify(incomes)


@app.route("/incomes", methods=['POST'])
def add_incomes():
    print(request.get_json())
    incomes.append(request.get_json())
    return '', 204
