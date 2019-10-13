FROM python:3
MAINTAINER Gian Luca Fiasco <glf@lucacloud.info>

ADD TVHm3u /opt/TVHm3u

WORKDIR /opt/
RUN pip install requests

CMD ["python3", "-m", "TVHm3u"]