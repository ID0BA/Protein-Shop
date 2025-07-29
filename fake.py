# Fake python app to test bad practices and insecure code
import flask
import hashlib
import requests

API_KEY = "sk_test_FAKEKEY1234567890abcDEF"  # 🚨 This should be flagged as a secret

password = "supersecret123"
hashed = hashlib.md5(password.encode()).hexdigest()  # 🚨 Weak hash algorithm


def make_request():
    url = "https://example.com/data"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.text


if __name__ == "__main__":
    app = flask.Flask(__name__)

    @app.route("/")
    def index():
        return "Welcome to the insecure app!"

    app.run()
