from flask import Flask
from api.views import views

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
    return "Hello"

#app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0",port=5000)


