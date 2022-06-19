```
git clone https://github.com/apmt/challenge1
```
# How to run with docker
Go to **challenge2** directory:
```
cd challenge1
```
Start docker (on ubuntu):
```
sudo dockerd
```
Build and run image iteratively:
```
docker image build -t ana_c1 .
docker container run -it ana_c1
```

Run the script on docker image **cli**:
```
python main.py
```


**WARNING:** Kill all process/containers and delete all images
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
```