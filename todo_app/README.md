
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
3. Github workflow will upload the application to your Google Artifact registry and GKE. These need to be setup beforehand.
   1. Some info [here](https://github.com/Jouchef/KubernetesSubmissions?tab=readme-ov-file#work-instruction-for-workload-identity-federation-to-connect-github-and-google-cloud)
4. After succesfull upload check the sites address with
   1. `kubectl get gateway -n shared` (It might take a while for it to appear.)
5. Go to the ip-address/todotest to see the site. 
   1. You can inspect the loadbalancer configuration with:
      1. `gcloud compute url-maps list` This lists you the gateway resources. Pick one which starts with `gkemg-...`
      2. `gcloud compute url-maps describe <gkemg-alkuinen-nimi> --global` Get the configuration with this command. From here you can see the routing. 
   2. You can inspect the local situation with
      1. `kubectl describe gateway shared-gateway -n shared`

# INSTRUCTIONS FOR DATABASE RESETTING
1. Go inside of the backend container
   1. `kubectl exec -it server-dep-... -c backend-container -- bash`
2. Run the initialiase command with reset flag
   1. `python3 initialize_database.py -reset`