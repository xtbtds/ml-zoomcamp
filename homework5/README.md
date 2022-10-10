Here is a directory for Homework 5, mlzoomcamp.


**Build docker image:**
```
docker build -t card .
```
**Run docker image:**
```
docker run -it card
docker run -it -p 9696:9696 card
docker run -it --entrypoint=bash card     #to run bash from image
```
