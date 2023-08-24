# install gcloud components

gcloud components install kubectl
gcloud components install docker-credential-gcr
+---------------+------------------------------------------------------+------------------------------+----------+
|     Status    |                         Name                         |              ID              |   Size   |
+---------------+------------------------------------------------------+------------------------------+----------+
| Installed     | BigQuery Command Line Tool                           | bq                           |  1.6 MiB |
| Installed     | Cloud Storage Command Line Tool                      | gsutil                       | 11.3 MiB |
| Installed     | Google Cloud CLI Core Libraries                      | core                         | 21.6 MiB |
| Installed     | Google Cloud CRC32C Hash Tool                        | gcloud-crc32c                |  1.3 MiB |
| Installed     | gke-gcloud-auth-plugin                               | gke-gcloud-auth-plugin       |  8.0 MiB |
| Installed     | kubectl                                              | kubectl                      |  < 1 MiB |

# Create Google cloud project 
#Project name #exchnage-pubsub 
#Project ID #exchnage-pubsub
#Project number: 944510545188

gcloud projects create exchnage-pubsub 
gcloud config set project Pexchnage-pubsub 


# Pub Sub
# enable services pubsub
gcloud services enable pubsub.googleapis.com

## Authorisation
gcloud auth application-default login
gcloud auth application-default set-quota-project exchnage-pubsub

## Google clound manual create topic and sub
gcloud pubsub topics create my-topic
gcloud pubsub subscriptions create my-sub --topic my-topic


#local PC install python libs
pip install --upgrade google-cloud-pubsub

# Google cloud kubernetes
gcloud services enable artifactregistry.googleapis.com
gcloud services enable containerregistry.googleapis.com

# Auth docker to push to Google
gcloud auth configure-docker
#?? Not sure
#gcloud auth configure-docker europe-central2-docker.pkg.dev

# docker
## build docker local
docker-compose build

## local docker docker rename
docker tag exchange-pubsub-exch-publisher:latest gcr.io/exchnage-pubsub/exchange-pubsub-exch-publisher
docker tag exchange-pubsub-exch-subscriber:latest gcr.io/exchnage-pubsub/exchange-pubsub-exch-subscriber 

docker push gcr.io/exchnage-pubsub/exchange-pubsub-exch-publisher
docker push gcr.io/exchnage-pubsub/exchange-pubsub-exch-subscriber 


## Terminal config 
# google cluster create
gcloud config set project exchnage-pubsub
gcloud config set compute/zone europe-central2-a
gcloud container clusters get-credentials  exchnage-pubsub-cmd2-cluster  --location europe-central2-a

## create k8 cluster
gcloud container clusters create exchnage-pubsub-cmd2-cluster --num-nodes=3 --location europe-central2-a


# get config kubectl
kubectl config view
kubectl get pods --cluster gke_exchnage-pubsub_europe-central2-a_exchnage-pubsub-cmd2-cluster


## run docker on k8
kubectl create deployment exchange-pubsub-publisher --image=gcr.io/exchnage-pubsub/exchange-pubsub-exch-publisher:latest  
kubectl create deployment exchange-pubsub-subscriber --image=gcr.io/exchnage-pubsub/exchange-pubsub-exch-subscriber:latest  

kubectl apply -f sub.yaml
kubectl apply -f pub.yaml



