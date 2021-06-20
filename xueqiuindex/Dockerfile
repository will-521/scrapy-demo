FROM python:3.8.2

ADD . /xueqiuindex/

WORKDIR /xueqiuindex

RUN pip install scrapy

RUN pip install kafka-python

CMD ["python", "main.py"]
