## This file consists of all the commands needed to set up and run this demo using Docker and OpenTelemetry. 🚀

### Installation
```
# install python dependancies
$ pip3 install -r requirements.txt

# install opentelemetry instrumentation dependancies
$ opentelemetry-bootstrap -a install

# list all installed python packages
$ pip3 list
```
### Instrumentation on console
```
# help for opentelemetry-instrument to check all options
$ opentelemetry-instrument --help

# instrument flask app && send ONLY metrics on console
$ opentelemetry-instrument --metrics_exporter console \
 --traces_exporter none --logs_exporter none \
flask run -h 0.0.0.0 -p 3000

# instrument flask app && send ONLY traces on console
$ opentelemetry-instrument --traces_exporter console \
--metrics_exporter none --logs_exporter none \
flask run -h 0.0.0.0 -p 3000

# instrument flask app && send ONLY logs on console
$ export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
$ opentelemetry-instrument --logs_exporter console \
--metrics_exporter none --traces_exporter none \
flask run -h 0.0.0.0 -p 3000
```
### Containerization of flask app
```
# build the container image for the flask app
$ docker build -t flaskapp:v1 .

# check docker images
$ docker images

# run container to test the image
$ docker run -name flask -dit -p 3000:3000 flaskapp:v1

# check container logs
$ docker logs -f flask

# check container status
$ docker ps
```

### Curl outputs from the app
```
$ curl localhost:3000/
200

$ curl localhost:3000/healthz
200

$ curl localhost:3000/notexist
404
```

### Run LGTM Stack + Python flask container
```
# create a network in docker
$ docker network create my-net

# run lgtm stack container
$ docker run -p 3000:3000 -p 4317:4317 -p 4318:4318  -dit \
--network my-net --name otel-lgtm grafana/otel-lgtm

# run python app & send all telemetry data to grafana via otlp
$ docker run -dit -p 3010:3000 --network my-net  \
-e OTEL_TRACES_EXPORTER=otlp \
-e OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://otel-lgtm:4317 \
-e OTEL_METRICS_EXPORTER=otlp \
-e OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://otel-lgtm:4317 \
-e OTEL_LOGS_EXPORTER=otlp \
-e OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://otel-lgtm:4317 \
-e OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true \
-e OTEL_SERVICE_NAME=flask-app \
--name flask  flaskapp:v1
```

### Grafana URL
```
http://localhost:3000

Username: admin
Password: admin
```
