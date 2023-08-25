FROM python:latest
WORKDIR /code
#ADD exchnage-pubsub-sa.json exchnage-pubsub-sa.json
ADD requirements.txt requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS=./exchnage-pubsub-sa.json
ENV PROJECT_ID=exchnage-pubsub
ENV TOPIC_ID=my-topic
ENV DELAY_SLEEP=5
ENV EXCH_URL="https://internetowykantor.pl/kurs-euro/"


RUN pip install -r requirements.txt
COPY pub.py pub.py
CMD ["python", "-u", "pub.py"]