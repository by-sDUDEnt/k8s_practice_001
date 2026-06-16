from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST


app = Flask(__name__)

c = Counter('http_requests_on_root_page', 'Number of visits for main page')


@app.route('/')
def hello_world():
    c.inc()
    return 'Hello World'


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


