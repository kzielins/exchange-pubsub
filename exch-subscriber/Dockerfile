FROM python:latest
WORKDIR /code
ADD exchnage-pubsub-sa.json exchnage-pubsub-sa.json
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY sub.py sub.py
CMD ["python", "-u", "sub.py"]