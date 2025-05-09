FROM python:3.8-slim-buster
WORKDIR /python-docker
COPY . .
RUN pip3 install -r requirements.txt && opentelemetry-bootstrap -a install && apt update && apt install curl -y
ENV OTEL_TRACES_EXPORTER=console
ENV OTEL_METRICS_EXPORTER=none
ENV OTEL_LOGS_EXPORTER=none
EXPOSE 3000
CMD ["opentelemetry-instrument", "flask", "run" , "-h", "0.0.0.0", "-p", "3000"]
