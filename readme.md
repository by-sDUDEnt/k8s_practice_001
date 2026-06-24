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
```bash
kubectl portforward <service-name> <port>:<port>
```
Then open:
http://localhost:<port>/


## Roadmap
- [x] Backend Development
- [x] Backend Deployment
- [ ] Front-End Development
- [ ] Front-End Deployment
- [x] Prometheus 
  [ ] Grafana monitoring
- [ ] .gitignore and .dockerignore


# App
WIP

Flask backend with /metrics endpoint

## Backend
To build docker image:

```bash
docker build -t  bysdudent/flask-backend:0.1 .
```
