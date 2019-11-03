FROM ubuntu:18.04


RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*


RUN apt-get update  && apt-get install -y \
    software-properties-common && \
    rm -rf /var/lib/apt/lists/*


# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt
#Local Dockerfile
#COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]