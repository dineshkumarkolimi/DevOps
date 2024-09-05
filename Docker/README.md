# Docker & Docker Compose

# Docker Commands:

1. docker pull <image name> - to pull image from docker hub
2. docker ps - to list all containers
3. docker images - to list all images
4. docker run -d -p <destination-port-no>:<source-port-no> --name <give-it-a-name> <image-name> -> to run a docker image
5. docker build -t image-name:version . -> to build an image
6. docker start containerid/containername -> to start a stopped container
7. docker stop containerid/containername -> to stop a running container
8. docker rm containerid/containername -> to delete a container
9. docker rmi image-name/id -> to remove an image
10. docker logs <container_id/name> -> to look at the logs
11. docker logs <container_id/name> -f -> to stream the logs
12. docker-compose -f <yaml-file-name> up -> to run all containers of docker images mentioned in docker-compose file and also docker network
13. docker-compose -f <yaml-file-name> down -> to remove all the running containers and network too.
14. docker exec -it <contiainername/id> . -> to enter into the container

# To create a network with mongo-db and express:
1. docker network ls -> to list the docker networks
2. docker network create <name> -> to create a new network
3. docker pull mongo
4. docker pull mongo-express
5. docker run -d --name <containername> -e MONGO_INITDB_USER_NAME=<username> -e MONGO_INITDB_ROOT_PASSWORD=<password> -p <destinationport>:27017 --net <network-name> mongo
6. docker run -d --name <containername> -e ME_CONFIG_MONGODB_ADMINUSERNAME=<username> -e ME_CONFIG_MONGODB_ADMINPASSWORD=<password> -e ME_CONFIG_MONGODB_SERVER=<container-name-of-mongodb> -p <destinationport>:8081 --net <network-name> mongo-express

# Docker File
Blueprint for building an image
Contents of docker file are as follows:
1. FROM <baseimage> This is the image on top of which our application/image is built
2. ENV - contains environmental variables (Its better to have these details in docker compose yaml file)
3. RUN - runs/executes the linux commands like creating a directory, installing requirements
4. WORKING DIR - to provide the working directory of the container
5. COPY - copy some of the source code and the docker file to the container. EX: COPY . /home/app
6. ENTRY POINT [“<filename>”] - using this we can run entire shell script instead of writing all the commands in the docker file
7. CMD - to run our application EX: CMD [“python”, “/home/app/src/main.py”]

# Push Image to Registry:
1. docker login <respositoryURI/aws command>
2. docker build -t <image-name>:version
3. docker tag <image-that-you-want-to-rename>:<tag/version> <registryDomain/imageName:tag> (if we push with out this docker would not know to which repository it has to push)
4. docker push <name of new image created>:tag

# Docker Volumes: using docker volumes we can achieve data persistency. 
 3 Types of volumes
1. Host Volume: docker run -v <host directory:container directory> —> you decide where on the host we store the volume
2.  Container Volumes: Create a volume just by referencing the container directory docker run -v <container directory> —> for each container a folder is generated and gets mounted automatically
3. Named Volumes: It specifies the name of folder on host Docker run -v <folder-name>:<container-directory>  —> Mostly used volumes

# How to write a Docker Compose file?

Docker compose is a tool for defining and running multi-container docker applications. 

We might have to use multiple images together to run an application. So, we use yaml files to configure application services. We can start and stop all the services with a single command. We can also scale up and scale down an application easily.

Run following commands:
1. `docker-compose -v` to check if docker-compose is installed or not. If not installed make sure we install it (`pip install -U docker-compose`)
2. Create a docker compose file: `touch docker-compose.yml`
3. This files contains following:
    version: ‘3.8’   —> This is always there  
    services:    —> This is always there
      mongodb:   —> Container name      
            &emsp &ensp &ensp build: ./app   —> path for the docker file. We use build incase we dont use prebuild image as below and we want to build our own image    
            &emsp &ensp &ensp image:     —> your image name and version     
            &emsp &ensp &ensp port:        
                &emsp &ensp &ensp &ensp - 8000:8080   —> Host:Container, ‘-’ indicates list  
            &emsp &ensp &ensp environment:    —> environment variables       
                &emsp &ensp &ensp &ensp - ME_MONGO_USERNAME=admin     
            &emsp &ensp &ensp volumes:       
                &emsp &ensp &ensp &ensp - db-data: /data/db       —> path of the volume inside of the container eg: mysql - /var/lib/mysql/data, postgres- /var/lib/postgresql/data, mongo - /data/db       
                &emsp &ensp &ensp &ensp - ./app: /WORKINGDIR/app  —> this will be used in case we are building our own image and if there are any code changes it will pick up automatically.     
            &emsp &ensp &ensp depends_on:       
                &emsp &ensp &ensp &ensp - fastapiapp   —> name of the service that it is dependent on mentioned in this file 
    &emsp volumes:   —> list all the volumes under this section   
        &emsp &ensp db-data:    --> this is name of the volume     
            &emsp &ensp &ensp driver: local   —> to create physical storage on a local file system. mac - /var/lib/docker/volumes, linux - /var/lib/docker/volumes, windows - C:\ProgramData\docker\volumes. 
            
    * Docker for mac creates a Linux VM and all the Docker data is stored in this VM. So to access the VM: `screen ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/ttyl`. Once we get the terminal of VM we can go to the above specified path    
    
    * Docker compose will take care of creating a common network for these containers
5. Map the above configuration to the following command:
    &emsp docker run -d \
        &emsp &ensp--name mongodb \
        &emsp &ensp-p 8000:8080 \
        &emsp &ensp-e ME_MONGO_USERNAME=admin \
        &emsp &ensp--net mongo-network \
        &emsp &enspmongodb:version <imagename goes here>
6. check the validity of file using the command `docker-compose config`. if you see the file’s content then the file structure is good.
7. Run the docker-compose file in detached mode by `docker-compose up -d`
8. To stop everything run `docker-compose down`
9. Also, we can populate the config by visiting the docker hub and opening the specific image we want to use. Search for docker-compose in the documentation section of that image and use it.
10. Tips: using scale flag we can scale up or down the application. By running the command `docker-compose up -d —scale database=3` to create 3 containers of database.
