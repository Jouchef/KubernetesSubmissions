This deployment works in conjuction with Log_output deployment. Log_output gets the ping data from this app via GET request.

## Local Development

1. ```k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2``` create cluster with these specs 
2. ```kubectl apply -f manifests``` run this command in pingpong folder. It applies deployment, service, PVC and ingress configurations.
3. Install kubens with ```apt install kubens```
4. ```kubens exercises``` to change to exercises namespace. Original is named default if you need to change back to that. 
5. [8081/pingpong](http://localhost:8081/pingpong) Here you should be able to see the website 


## GKE Development
This assumes that you have installed [Google Cloud SDK](https://cloud.google.com/sdk/install)
And installed auth plugin `gcloud components install gke-gcloud-auth-plugin`

1. Create cluster `gcloud container clusters create dwk-cluster --zone=europe-north1-b --release-channel=regular --disk-size=32 --num-nodes=3 --machine-type=e2-micro --gateway-api=standard  --monitoring=NONE --logging=NONE`
2. Apply the configuration in pingpong folder `kubectl apply -f gke_manifests/`
3. Change namespace to "Exercises" `kubens exercises`
4. `kubectl get gateway --watch` And open my-gateway Address/pingpong when it is not as pending.

This app uses postgres to store ping count. It it deployed in statefulset.yaml.


The PORT variable is defined in _"deployment.yaml"_ and you may change that according to your needs. Remember also to change it from _"service.yaml"_ "targetPort".


This exercise is intended to be used in "exercises" Namespace. You can install **kubens** or use kubectl commands to change between namespaces. 