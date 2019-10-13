FROM python:3



ADD TVHm3u /opt/TVHm3u
ADD requirements.txt /opt/

WORKDIR /opt/
RUN pip install requests

CMD ["python3", "-m", "TVHm3u"]