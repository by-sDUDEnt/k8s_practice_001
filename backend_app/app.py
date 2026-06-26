from flask import Flask, Response, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import os


app = Flask(__name__)

c = Counter('http_requests_on_root_page', 'Number of visits for main page')


@app.route('/')
def hello_world():
    c.inc()
    return 'Hello World'


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/api/pod-info')
def pod_info():
    pod_name = os.environ.get("POD_NAME")
    node_name = os.environ.get("NODE_NAME")
    pod_ip = os.environ.get("POD_IP")
    return jsonify({
    "pod_name": pod_name,
    "node_name": node_name,
    "pod_ip": pod_ip
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


