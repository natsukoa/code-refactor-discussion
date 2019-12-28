bp = Blueprint("hello", __name__)

@app.route("/hello")
def hello():
    return "Hello, World!"
