1. ```k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2``` create cluster with these specs 
2. If you have deployment with the same name running you can delete it with ```kubectl delete deployment logger-dep```
3. ```kubectl apply -f manifests``` run this command in Log_output folder
4. [8081/logs](http://localhost:8081/logs) Here you should be able to see the website 


```kubectl get ing``` If you have multiple ingresses you should delete the others so they dont interfere with each other

The PORT variable is defined in _"deployment.yaml"_ and you may change that according to your needs. Remember also to change it from _"service.yaml"_


