FROM python:latest
WORKDIR /code
#ADD exchnage-pubsub-sa.json exchnage-pubsub-sa.json
ADD requirements.txt requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS=./exchnage-pubsub-sa.json
ENV PROJECT_ID=exchnage-pubsub
ENV TOPIC_ID=my-topic
ENV DELAY_SLEEP=5
ENV SUBSCRIPTION_ID=my-sub

RUN pip install -r requirements.txt

COPY sub.py sub.py
CMD ["python", "-u", "sub.py"]