FROM python:3.9
WORKDIR /usr/src/app
RUN pip install requests 
COPY report_generation.py ./
CMD ["python", "report_generation.py"]