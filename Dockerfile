FROM rayproject/ray:2.0.0

RUN mkdir -p /tmp/location/test

ADD https://github.com/ray-project/test_dag/archive/c620251044717ace0a4c19d766d43c5099af8a77.zip /tmp/fruits/
 
#RUN chown -R ray:users /tmp/fruits/

EXPOSE 6379 8265 10001 8000

#CMD ray start --head
