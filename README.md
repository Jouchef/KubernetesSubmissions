# Kubernetes submissions

## Exercises

### CHAPTER 2
- [1.1](https://github.com/Jouchef/KubernetesSubmissions/tree/1.1/Log_output)
- [1.2](https://github.com/Jouchef/KubernetesSubmissions/tree/1.2/todo_app)
- [1.3](https://github.com/Jouchef/KubernetesSubmissions/tree/1.3/Log_output)
- [1.4](https://github.com/Jouchef/KubernetesSubmissions/tree/1.4/todo_app)
- [1.5](https://github.com/Jouchef/KubernetesSubmissions/tree/1.5/todo_app)
- [1.6](https://github.com/Jouchef/KubernetesSubmissions/tree/1.6/todo_app)
- [1.7](https://github.com/Jouchef/KubernetesSubmissions/tree/1.7/Log_output)
- [1.8](https://github.com/Jouchef/KubernetesSubmissions/tree/1.8/todo_app)
- [1.9](https://github.com/Jouchef/KubernetesSubmissions/tree/1.9/pingpong) 
- [1.10](https://github.com/Jouchef/KubernetesSubmissions/tree/1.10/Log_output)
- [1.11](https://github.com/Jouchef/KubernetesSubmissions/tree/1.11/Log_output)
- [1.12](https://github.com/Jouchef/KubernetesSubmissions/tree/1.12/todo_app)
- [1.13](https://github.com/Jouchef/KubernetesSubmissions/tree/1.13/todo_app)

### CHAPTER 3
- [2.1](https://github.com/Jouchef/KubernetesSubmissions/tree/2.1/Log_output)
- [2.2](https://github.com/Jouchef/KubernetesSubmissions/tree/2.2/todo_app)
- [2.3](https://github.com/Jouchef/KubernetesSubmissions/tree/2.3/Log_output)
- [2.4](https://github.com/Jouchef/KubernetesSubmissions/tree/2.4/todo_app)
- [2.5](https://github.com/Jouchef/KubernetesSubmissions/tree/2.5/Log_output)
- [2.6](https://github.com/Jouchef/KubernetesSubmissions/tree/2.6/todo_app)
- [2.7](https://github.com/Jouchef/KubernetesSubmissions/tree/2.7/pingpong) 
- [2.8](https://github.com/Jouchef/KubernetesSubmissions/tree/2.8/todo_app)


## Commands

### K3D
| Command                                    | about                              |
| ------------------------------------------ | ---------------------------------- |
| k3d cluster start / stop                   | Start ands stops current cluster   |
| k3d image import                           | Import docker image to the cluster |
| k3d cluster create / delete / list /  edit | Modify cluster in some manner      |

### Kubectl
| Command                                                           | about                                                                                                                       |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| kubectl config use-context CLUSTERNAME                            | Change context to other cluster                                                                                             |
| kubectl explain RESOURCE                                          | Get explanation to the resource                                                                                             |
| kubectl describe RESOURCE RESOURCENAME                            | shows all specs of the resource                                                                                             |
| kubectl get RESOURCE                                              | List all objects of that type                                                                                               |
| kubectl logs -f PODNAME                                           | see the output of the pod                                                                                                   |
| kubectl delete deployment DEPNAME                                 | Delete the deployment                                                                                                       |
| kubectl apply -f FILEPATH-TO-YAML                                 | create or modify deployment / service according to the YAML                                                                 |
| kubectl config view --minify --raw                                | get kubeconfig for example to use with lens                                                                                 |
| kubectl port-forward PODNAME LOCALPORT:APPPORT                    | Create temporary access to software for example debugging purposes                                                          |
| kubectl create secret generic SECRETNAME --from-env-file=.env     | Use your .env file to bring secret to the cluster                                                                           |
| kubectl create secret generic SECRETNAME --from-literal=KEY=VALUE | Save variable to the cluster. After this add details to the deployment configuration yaml.                                  |
| kubectl get deployment DEPNAME -o yaml                            | Get the deployments info in yaml format.                                                                                    |
| kubectl exec -it PODNAME -- printenv                              | See all variables used in pod. Can be used with grep command                                                                |
| kubectl rollout restart deployment DEPNAME                        | Restart a deployment when envs updated.                                                                                     |
| kubectl exec -it DEPLOYMENTNAME -- bash                           | Run commands inside the deployment for troubleshooting                                                                      |
| wget -qO - http://SERVICENAME:SERVICEPORT                         | From inside of an another pod you can connect to anothor pod inside the same cluster if you have ClusterIp service defined. |
| kubectl config set-context --current --namespace=<name>           | If you want to use specific namespace contantly use this command to change default namespace.                               |




### Docker
| Command                     | About                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| docker exec -it NODENAME sh | Inspect specific Node. In this course this was used to check file status when troubleshooting DB problems. |


### Virtual Env
| Command                       | About                                                                  |
| ----------------------------- | ---------------------------------------------------------------------- |
| python3 -m venv venv          | Create virtual environment including python and pip.                   |
| source venv/bin/activate      | Activate virtual environment in terminal.                              |
| pip install DEPENDENCY        | Install dependency to the virtual environment.                         |
| pip freeze > requirements.txt | Create requirements.txt file that Dockerfile needs for image building. |
| deactivate                    | Escape pip virtual environment.                                        |

### Kubens - Manage Namespaces
Install it with apt or other
| Command          | About                                            |
| ---------------- | ------------------------------------------------ |
| kubens           | List Namespaces in active cluster.               |
| kubens NAMESPACE | Change the namespace to the specified namespace. |

### psql
```pip install psycopg2-binary```
| Command                              | About                                           |
| ------------------------------------ | ----------------------------------------------- |
| psql -U POSTGRES_USER -d POSTGRES_DB | Use postgres when you have exec'd into the pod. |
| \l                                   | List databases                                  |
| \c DATABASENAME                      | Connect to specific database.                   |
| \dt                                  | list tables                                     |
| \d TABLENAME                         | Show table info                                 |

## Key concepts

### Part II

- **cluster:** group of nodes / containers (server or agent)
- **deployment:** resource that controls pods creation, updating and scaling
- **Resource:** pod, service (svc), node, deployment, PV, PVC, namespace
- **Nodeport:** Port that is available outside. It has to be between 30080 - 32767
- **Service:** Ensures that application is accessible and secured. Handles routing, load balancing... 
- **pod:** Pod can have one or multiple containers running inside of it. 
- **Ingress:** Ingress is a resource that handles routing to the running services inside of a cluster according to the set rules.
- **PersistentVolume (PV):** Defines space for filestorage. Can be stored in different storage mediums. Pods can claim these with *PVC's*
- **PersistentVolumeClaim (PVC):** This allows a pod to claim storagespace from a PV.


### Part III
- **Namespace** Virtual cluster inside of a cluster. With namespace it is possible to divide cluster to smaller logical sections so other software does not interfere with another.
- **ConfigMap** Used to store configuration variables for the application. Changes in configMap reflect instantly in the running application.
- **Secrets** Used to store sensitive information for example API keys.
- **StatefulSet** Like a deployment, but when restarting or crashing they keep their state. 


## Problems and fixes for them
- Suddenly could not pull image from Dockerhub when deploying the application. Did work earlier. Pulling with Docker commands worked. 
  - Errors: 
    - ```ImagePullBackOff```, 
    - ```failed to do request: Head "https://registry-1.docker.io/v2/jouchef/log_creator/manifests/1.10.1": dial tcp: lookup registry-1.docker.io: Try again```
  - Fix: ```k3d cluster stop CLUSTER``` ```k3d cluster start CLUSTER```
  - This fixed the problem for me. 
- If you want to update pvc and connect it to the old pv, but ```kubectl get pv``` shows "Released" instead of "Available" on the **status** \
  you can use ```kubectl patch pv PVNAME -p '{"spec":{"claimRef": null}}'``` This command releases the pv from the old pvc and sets **status** to Available.
- If your computer does not have pg_config you need to install psycopg2-binary instead of psycopg2
