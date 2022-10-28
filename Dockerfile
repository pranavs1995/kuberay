FROM rayproject/ray:2.0.0

RUN sudo apt update && sudo apt-get install zip -y

RUN mkdir -p /tmp/location/test

WORKDIR /home/ray/

COPY test_dag-c620251044717ace0a4c19d766d43c5099af8a77 test_dag-c620251044717ace0a4c19d766d43c5099af8a77

RUN zip c620251044717ace0a4c19d766d43c5099af8a77.zip test_dag-c620251044717ace0a4c19d766d43c5099af8a77/* && sudo rm -rf test_dag-c620251044717ace0a4c19d766d43c5099af8a77

# temp comment
#ADD https://github.com/ray-project/test_dag/archive/c620251044717ace0a4c19d766d43c5099af8a77.zip /home/ray/

RUN sudo chmod +x c620251044717ace0a4c19d766d43c5099af8a77.zip && sudo chown ray:users c620251044717ace0a4c19d766d43c5099af8a77.zip

EXPOSE 6379 8265 10001 8000

#CMD ray start --head
