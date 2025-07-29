
0. Add .env -file that has the PORT variable in it. 
1. Make sure your cluster is running
2. ```kubectl apply -f manifests/deployment.yaml``` This adds server deployment to the cluster.
3. You can inspect the logs with ```kubectl logs -f server-dep-......``` tab for dots.
4. ```kubectl port-forward server-dep-...... LOCAL-PORT:PORT-IN-ENV-FILE``` Connect your local port to clusters port. Tab for dots.
5. Now you can see the web page in [localhost:LOCAL-PORT](http://localhost:3003/)
