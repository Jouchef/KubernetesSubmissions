1. ```k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2``` create cluster with these specs 
2. If you have deplyment with the same name running you can delete it with ```kubectl delete deployment log-output-dep```
3. ```kubectl create secret generic log-output-secret --from-literal=PORT=3001``` 
4. ```kubectl apply -f manifests``` run this command in Log_output folder
5. [8081](http://localhost:8081/) Here you should be able to see the website 
6. ```kubectl get ing``` If you have multiple ingresses you should delete the others so they dont interfere with each other

Now you should see the printout.
