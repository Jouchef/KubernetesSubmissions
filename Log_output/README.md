This deployment works in conjuction with the pingpong deployment. This deployment gets the ping amount from the shared PV




1. ```k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2``` create cluster with these specs 
2. Make sure that this command has been ran ```docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube``` This creates directory for the PV
3. PV needs to be applied from: ```/admin/manifests``` with ```kubectl apply -f persistentVolume.yaml```
4. ```kubectl apply -f manifests``` run this command in Log_output folder
5. Install kubens with ```apt install kubens```
6. ```kubens exercises``` to change to exercises namespace. Original is named default if you need to change back to that. 
7. [8081/logs](http://localhost:8081/logs) Here you should be able to see the website 


The PORT variable is defined in _"deployment.yaml"_ and you may change that according to your needs. Remember also to change it from _"service.yaml"_

This exercise is intended to be used in "exercises" Namespace. You can install **kubens** or use kubectl commands to change between namespaces. 


