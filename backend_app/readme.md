## Backend
To build docker image:

```bash
docker build -t  bysdudent/flask-backend:0.2 .
docker tag bysdudent/flask-backend:0.2 bysdudent/flask-backend:latest
docker push bysdudent/flask-backend:0.2
docker push bysdudent/flask-backend:latest
```

## To run locally with test OS envs (Windows):
```bash
$env:POD_NAME="test-pod"; $env:NODE_NAME="test-node"; $env:POD_IP="192.168.1.1"; python app.py
```
