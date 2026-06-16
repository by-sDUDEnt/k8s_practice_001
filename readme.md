# Kubernetes Home Lab Monitor

WIP

## Prerequisites
Docker Desktop with Kubernetes enabled, kubectl

## Deploy
`cd k8s
kubectl apply -f ./ -R`

## Access
kubectl proxy

Then open:
http://localhost:8001/api/v1/namespaces/default/services/nginx-svc/proxy/



## Roadmap
- [ ] Prometheus + Grafana monitoring


# App
WIP

Flask backend with /metrics endpoint

## Backend
    To build docker image
    `docker build -t  bysdudent/flask-backend:0.1 .`   

