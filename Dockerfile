FROM ubuntu:18.04
WORKDIR /usr/src/app
RUN apt-get update 
RUN apt-get install -y python3.8 python3-pip
COPY . .
RUN pip3 install requests 
COPY report_generation.py ./
CMD ["python3", "report_generation.py"]