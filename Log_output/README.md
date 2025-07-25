1. ```k3d cluster create -a 2```
2. ```docker build -t log_output:1.1 .```
3. ```kubectl create deployment log-output-dep --image=jouchef/log_output:1.1```
4. ```kubectl get pods``` Take note of the "name"
5. ```kubectl logs -f jouchef/log-output-dep.....``` use tab to fill the name.

Now you should see the printout.