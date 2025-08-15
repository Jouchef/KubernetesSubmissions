
0. Add .env -file that has the PORT variable in it. 
1. Make sure your cluster is running
2. ```kubectl apply -f manifests/deployment.yaml``` This adds server deployment to the cluster.
3. ```kubectl apply -f manifests/service.yaml``` This configures network service to the cluster.
4. You can inspect the logs with ```kubectl logs -f server-dep-......``` tab for dots. 
5. Now you can see the web page in [localhost:LOCAL-PORT](http://localhost:3000/)
