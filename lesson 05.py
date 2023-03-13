from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")
def index():
    print(url_for("index"))
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    print((url_for("about")))
    return render_template('about.html', title="О cайте", menu=menu)


@app.route("/profile/<int:username>/<path>")
def profile(username, path):
    return f"Пользователь: {username}, {path}"


@app.route("/contact", methods = ["POST"])
def contact():
    if request.method == "POST":
        print(request.form)
        print(request.form[''])
    return render_template('contact.html', title="Обратная связь", menu=menu)


# with app.test_request_context():
#     print(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
