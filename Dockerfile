FROM rayproject/ray:2.0.0

RUN mkdir -p /tmp/location/test

#COPY test_dag-c620251044717ace0a4c19d766d43c5099af8a77/* /home/ray/

#RUN unzip /tmp/fruits/c620251044717ace0a4c19d766d43c5099af8a77.zip
#RUN chown -R ray:users /tmp/fruits/

ADD https://github.com/ray-project/test_dag/archive/c620251044717ace0a4c19d766d43c5099af8a77.zip /home/ray/

RUN sudo chmod +x /home/ray/c620251044717ace0a4c19d766d43c5099af8a77.zip && sudo chown ray:users /home/ray/c620251044717ace0a4c19d766d43c5099af8a77.zip

EXPOSE 6379 8265 10001 8000

#CMD ray start --head
