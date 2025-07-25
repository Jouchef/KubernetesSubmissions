
0. Add .env -file that has the PORT variable in it. 
1. Make sure your cluster is running
2. ```kubectl apply -f manifests/deployment.yaml``` This adds server deployment to the cluster.
3. You can inspect the logs with ```kubectl logs -f server-dep-......``` tab for dots.

