
 # INSTRUCTIONS FOR INSTALLATION
1. ```k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2``` create cluster with these specs 
2. Make sure that this command has been ran ```docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/server/database``` This creates directory for the PV
3. PV needs to be applied from: ```/admin/manifests``` with ```kubectl apply -f serverPersistentVolume.yaml```
4. ```kubectl apply -f manifests``` Run this in todo_app folder to apply the configurations.
5. Now you can see the web page in [localhost:8081](http://localhost:8081/)


The PORT variable is defined in _"deployment.yaml"_ and you may change that according to your needs. Remember also to change it from _"service.yaml"_