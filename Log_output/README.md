1. ```k3d cluster start```  if you already have cluster set up
1. ```k3d cluster create``` if you dont yet have cluster running
2. ```kubectl apply -f manifests/deployment.yaml``` run this command in Log_output folder
If you have deplyment with the same name running you can delete it with ```kubectl delete deployment log-output-dep```
4. ```kubectl get pods``` Take note of the "name"
5. ```kubectl logs -f log-output-dep.....``` use tab to fill the name.

Now you should see the printout.