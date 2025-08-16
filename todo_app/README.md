
 
1. ```k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2``` create cluster with these specs 
2. ```kubectl create secret generic server-secret --from-literal=PORT=3000``` You can check your secrets with ```kubectl get secrets```
2. ```kubectl apply -f manifests``` Run this in todo_app folder  
5. Now you can see the web page in [localhost:LOCAL-PORT](http://localhost:8081/)
6. ```kubectl get ing``` If you have multiple ingresses you should delete the others so they dont interfere with each other

