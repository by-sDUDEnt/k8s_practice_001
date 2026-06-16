# Kubernetes Home Lab Monitor

WIP

## Prerequisites
Docker Desktop with Kubernetes enabled, kubectl

## Deploy
```bash
cd k8s
kubectl apply -f ./ -R
```

## Access
kubectl proxy

Then open:
http://localhost:8001/api/v1/namespaces/default/services/nginx-svc/proxy/



## Roadmap
- [x] Backend Development
- [ ] Backend Deployment
- [ ] Front-End Development
- [ ] Front-End Deployment
- [ ] Prometheus + Grafana monitoring
- [ ] .gitignore and .dockerignore


# App
WIP

Flask backend with /metrics endpoint

## Backend
To build docker image:

```bash
docker build -t  bysdudent/flask-backend:0.1 .
```
