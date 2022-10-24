FROM rayproject/ray:2.0.0

RUN mkdir -p /tmp/location/test

EXPOSE 6379 8265 10001 8000

#CMD ray start --head