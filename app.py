from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from zoneinfo import ZoneInfo
import time
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get APP configuration
app_host = os.environ.get('APP_HOST', '0.0.0.0')
app_port = int(os.environ.get('APP_PORT', 5005))
app_env = os.environ.get('APP_ENV', 'dev')

# Get DB configuration
db_provider = os.environ.get('DB_PROVIDER')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')

# Configure SQLAlchemy with the database URL
app.config['SQLALCHEMY_DATABASE_URI'] = f"{db_provider}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define the Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    completed_at = db.Column(db.DateTime, nullable=True)


# ---- Routes ----
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
        todo.completed_at = db.func.now() if todo.completed else None
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    todo = db.session.get(Todo, id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("index"))
# ---- End of Routes ---- 


# Set timezone conversion for display
def filter_datetime(dt, tz=ZoneInfo('Asia/Jakarta')):
    if dt is None:
        return ""
    return dt.astimezone(tz).strftime('%d %b %y, %H:%M %Z')

app.jinja_env.filters['localtime'] = filter_datetime


def create_tables():
    retries = 5
    for attempt in range(retries):
        try:
            with app.app_context():
                db.create_all()
            return
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(3)
            else:
                raise


# Run the Flask app
if __name__ == "__main__":
    create_tables()
    app.run(host=app_host, port=app_port, debug=(app_env == 'dev'))
