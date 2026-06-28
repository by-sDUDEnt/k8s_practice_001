# Kubernetes Home Lab Monitor

WIP

## Prerequisites
Docker Desktop with Kubernetes enabled, kubectl

## Deploy 
```bash
cd k8s
kubectl apply -f ./k8s/ -R --server-side --force-conflicts
```
The --server-side and --force-conflicts is because of ArgoCD


## Access
```bash
kubectl port-forward service/<service-name> <port>:<port>
```
Then open:
http://localhost:<port>/


## Roadmap
- ✅ Backend Development
- ✅ Backend Deployment
- ✅ Front-End Development
- ✅ Front-End Deployment
- ✅ Prometheus 
- ✅ Grafana monitoring
- ✅ .gitignore and .dockerignore
- [ ] Convert to Helm charts
- [ ] CI/CD
- [ ] Persistance storage
- [ ] Autoscaling
- [ ] Flask healthchecks



