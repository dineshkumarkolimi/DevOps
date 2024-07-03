# KubernetesApp - with mongodb config, its service, deployment and a webapp service, deployment

run `minikube start`
check for nodes running: `kubectl get node`

Now run following commands to create everything we need:
1. `kubectl apply -f mongo-config.yaml`
2. `kubectl apply -f mongo-secret.yaml`
3. `kubectl apply -f mongo.yaml`
4. `kubectl apply -f web.yaml`

Interacting with K8s Cluster:
1. to get all components: `kubectl get all`
2. to get configMap: `kubectl get configmap`
3. to get secrets: `kubectl get secret`
4. to get pods: `kubectl get pod`
5. to get all details related to a service: `kubectl get service webapp-service`
6. to get all details of a pod: `kubectl get pod <podname>`
7. to get logs or stream the logs: `kubectl logs <podname>` and `kubectl logs <podname> -f`
8. to get address of minikube in order to access the services: `minikube ip`
9. using minikube ip address and port mentioned in webapp-service portnode we can access the app in browser

