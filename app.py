from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Local VM!"

# Optional: simulate load endpoint
@app.route('/load')
def load():
    for _ in range(10**7):
        pass
    return "Load generated!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
