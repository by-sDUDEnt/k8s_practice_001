## Backend
To build docker image:

```bash
docker build -t  bysdudent/nginx-frontend:0.1 .
docker tag bysdudent/nginx-frontend:0.1 bysdudent/nginx-frontend:latest
docker push bysdudent/nginx-frontend:0.1
docker push bysdudent/nginx-frontend:latest
```

