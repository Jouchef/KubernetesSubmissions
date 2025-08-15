# Kubernetes submissions

## Exercises

### CHAPTER 2
- [1.1](https://github.com/Jouchef/KubernetesSubmissions/tree/1.1/Log_output)
- [1.2](https://github.com/Jouchef/KubernetesSubmissions/tree/1.2/todo_app)
- [1.3](https://github.com/Jouchef/KubernetesSubmissions/tree/1.3/Log_output)
- [1.4](https://github.com/Jouchef/KubernetesSubmissions/tree/1.4/todo_app)
- [1.5](https://github.com/Jouchef/KubernetesSubmissions/tree/1.5/todo_app)



## Commands

### K3D
| Command | about |
| ------- | ----- |
| k3d cluster start / stop | Start ands stops current cluster | 
| k3d image import | Import docker image to the cluster |
| k3d cluster create / delete / list /  edit | Modify cluster in some manner |

### Kubectl
| Command | about |
| ------- | ----- |
| kubectl config use-context CLUSTERNAME | Change context to toher cluster |
| kubectl explain RESOURCE | Get explanation to the resource |
| kubectl describe RESOURCE | shows all specs of the resource |
| kubectl get RESOURCE | List all objects of that type |
| kubectl logs -f PODNAME | see the output of the pod |
| kubectl delete deployment DEPNAME | Delete the deployment |
| kubectl apply -f FILEPATH-TO-YAML | create or modify deployment / service according to the YAML |
| kubectl config view --minify --raw | get kubeconfig for example to use with lens |
| kubectl port-forward PODNAME LOCALPORT:APPPORT | Create temporary access to software for example debugging purposes |
|kubectl create secret generic SECRETNAME --from-env-file=.env | Use your .env file to bring secret to the cluster |






## Key concepts

### Part II

- cluster: group of nodes / containers (server or agent)
- deployment: resource that controls pods creation, updating and scaling
- Resource: pod, service, node, deployment, 
- Nodeport: Port that is available outside. It has to be between 30080 - 32767
- Service: Ensures that application is accessible and secured. Handles routing, load balancing... 