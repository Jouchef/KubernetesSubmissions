This deployment works in conjuction with Log_output deployment. Log_output gets the ping data from this app via shared volume. 

PVC for both of the deployments is defined in this app.

1. ```k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2``` create cluster with these specs 
2. ```docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube``` Add directory to this specific node so that we can use it to save files. 
3. Navigate to ```/admin/manifests``` to apply the PV  with ```kubectl apply -f persistentVolume.yaml```
4. ```kubectl apply -f manifests``` run this command in pingpong folder. It applies deployment, service, PVC and ingress configurations.
5. [8081/pingpong](http://localhost:8081/pingpong) Here you should be able to see the website 


The PORT variable is defined in _"deployment.yaml"_ and you may change that according to your needs. Remember also to change it from _"service.yaml"_ "targetPort".


