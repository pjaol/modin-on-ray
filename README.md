# Modin on ray

## Building the image
This is based on ray project image, however to use something like modin on ray you have to build an image with your desired modules installed. 
Check out the Dockerfile to see how this is done
Customize this with your own libraries, package manager, code copy etc 

```sh
docker build -t ray-modin .
```

## Running 
I'm a fan of docker compose so
```sh
docker compose up -d --scale worker=2
docker compose logs 
```

### Scaling out more 
If you want to add additional workers

```sh
docker compose up -d --scale worker=3 --no-recreate
```

