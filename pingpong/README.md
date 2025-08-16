1. ```k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2``` create cluster with these specs 
2. PORT variable has been defined in deployment.yaml. Change it if need to. If you change it, also change it from the service.yaml "targetPort"
3. ```kubectl apply -f manifests``` run this command in pingpong folder. It applies deployment, service and ingress configurations.
4. [8081/pingpong](http://localhost:8081/pingpong) Here you should be able to see the website 

