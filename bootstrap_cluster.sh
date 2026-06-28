#!/bin/bash
set -e
kubectl apply -f ./k8s/namespace.yaml
kubectl apply -n argocd --server-side --force-conflicts -f ./k8s/argocd/install.yaml
kubectl apply -f ./k8s/ -R 