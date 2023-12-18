FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]


# Docker build command: docker build -t docker_example_1 .
# Docker run command: docker run -d -p 5001:5000 docker_example_1
# go to hub.docker.com and click on python

# FROM specifies which base operating system from the hub.docker.com with python installed in it
# WORKDIR folder that houses this code
# COPY copies the content of the current directory of the Dockerfile into the app directory within the container
# RUN requirements.txt is to just install the python dependencies in requirements.txt (flask)
# EXPOSE 5000 is to show that the docker container will be designed to listen on port 5000
# CMD is to run the app.py through python when the container starts to run