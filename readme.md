# Kubernetes Home Lab Monitor

WIP

## Prerequisites
Docker Desktop with Kubernetes enabled, kubectl

## Deploy 
The `bootstrap_cluster.sh` contains commands to deploy the cluster. The need of one comes from deploying ArgoCD in the dedicated namespace `argocd`.
The imperative nature will be fixed after introduction of kustomize. 
For PowerShell (Windows) deploy - copy paste the commands.


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



