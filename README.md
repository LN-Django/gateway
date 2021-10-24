# boilerplate
Django + REST boilerplate for future services

## Docker config
### Prequisites
- Docker is installed and accessible via terminal

How to use Docker to serve the application locally

Build the docker image
```
docker build -t web:latest .
```

Run the container with the name of `boilerplate` using the image built on the last step
```
docker run -d --name boilerplate -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest
```

Check on `http://localhost:8007` to see if the app is running.

Stop the docker container
```
docker stop boilerplate
```

Remove the container
```
docker rm boilerplate
```