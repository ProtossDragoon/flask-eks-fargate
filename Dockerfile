FROM python:3.8

WORKDIR /ws

COPY * /ws/

RUN make all

EXPOSE 5000

ENTRYPOINT ["flask", "run", "-p", "5000", "--host=0.0.0.0"]