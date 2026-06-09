from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Get DB configuration
provider = os.environ.get('DB_PROVIDER')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')

# Configure SQLAlchemy with the database URL
app.config['SQLALCHEMY_DATABASE_URI'] = f"{provider}://{user}:{password}@{host}:{port}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)


@app.route("/")
def index():
    todos = Todo.query.order_by(Todo.id.desc()).all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if title:
        db.session.add(Todo(title=title))
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/toggle/<int:id>", methods=["POST"])
def toggle(id):
    todo = db.session.get(Todo, id)
    if todo:
        todo.completed = not todo.completed
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    todo = db.session.get(Todo, id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("index"))

# Run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
