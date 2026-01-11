
 # INSTRUCTIONS FOR LOCAL INSTALLATION
1. ```k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2``` create cluster with these specs 
2. Make sure that this command has been ran ```docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/server/database``` This creates directory for the PV
3. PV needs to be applied from: ```/admin/manifests``` with ```kubectl apply -f serverPersistentVolume.yaml```
4. ```kubectl apply -k manifests/overlays/local``` Run this in todo_app folder to apply the local configurations with kustomize.
5. Now you should see the web page in [localhost:8081](http://localhost:8081/)


# INSTRUCTIONS FOR GKE INSTALLATION
1. Setup you Google cloud account [Instructions here](https://courses.mooc.fi/org/uh-cs/courses/devops-with-kubernetes/chapter-4/introduction-to-google-kubernetes-engine)
2. Deploy your cluster
   1. `gcloud container clusters create dwk-cluster --zone=europe-north1-b --release-channel=regular --disk-size=32 --num-nodes=3 --machine-type=e2-micro --gateway-api=standard --monitoring=NONE --logging=NONE`
3. From root folder run `kubectl apply -f admin/gke_manifests/`
   1. First it creates "shared" namespace
   2. Second it creates gateway for all apps
      1. This listens for all namespaces and handles http traffic (not https)
4. Go to todo-folder
   1. run `kubectl apply -k manifests/overlays/gke/`
      1. This uses Kustomize to run GKE tailored initialisation
5. Check the sites address with
   1. `kubectl get gateway -n shared`
6. Go to the ip-address/todo to see the site. 

# INSTRUCTIONS FOR DATABASE RESETTING
1. Go inside of the backend container
   1. `kubectl exec -it server-dep-5c7d64ff66-rw5l7 -c backend-container -- bash`
2. Run the initialiase command with reset flag
   1. `python3 initialize_database.py -reset`