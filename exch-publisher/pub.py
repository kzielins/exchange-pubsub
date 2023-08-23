import os,json,time,datetime
import requests
import lxml.html

from google.cloud import pubsub_v1
from google.api_core.exceptions import AlreadyExists

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="exchnage-pubsub-sa.json"
SERVICE_ACCOUNT_PATH='./exchnage-pubsub-sa.json'
PROJECT_ID = "exchnage-pubsub"
TOPIC_ID = "my-topic"
DELAY_SLEEP = 5



def create_topic(project_id, topic_id):
  """Create pubsub project_id -> topic if not exists"""
  publisher = pubsub_v1.PublisherClient.from_service_account_json(SERVICE_ACCOUNT_PATH)
  #create topic if not exist  
  topic_path = publisher.topic_path(project_id, topic_id)
  try:
    topic = publisher.create_topic(request={"name": topic_path})
    print(f"Created topic: {topic.name}")
  except AlreadyExists:
    #print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f' [WARNING] Topic {topic_id} already exists, ')
 
def publish_data(project_id, topic_id, data_str):
  """publish data_str to topic_id"""
  publisher = pubsub_v1.PublisherClient.from_service_account_json(SERVICE_ACCOUNT_PATH)
  #create topic if not exist  
  topic_path = publisher.topic_path(project_id, topic_id)
  data = data_str.encode("utf-8")
  # When you publish a message, the client returns a future.
  future = publisher.publish(topic_path, data)
  print(f" data: {data_str} publish_data result: {future.result()}") 



def get_exch(web_http):
  """get currency exchane rate from url"""
  html = requests.get(web_http)
  doc = lxml.html.fromstring(html.content)
  buy = float(doc.xpath('//*[@data-rates-direction="buy"]/text()')[0].replace(',', '.'))
  sell = float(doc.xpath('//*[@data-rates-direction="sell"]/text()')[0].replace(',', '.'))
  forex = float(doc.xpath('//*[@data-rates-direction="forex"]/text()')[0].replace(',', '.'))
  exch_name =   doc.xpath('//*[@class="bem-chart-intro__current-rate"]/text()')[0].replace(":","").replace('Aktualny kurs', '').replace(" ","").replace("\n","") 
  parsed_exch={"exchange":exch_name, "buy":buy, "sell":sell, "averange":forex , "datetime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  return parsed_exch


#create topic
create_topic(PROJECT_ID, TOPIC_ID)

while 1:
    data=get_exch("https://internetowykantor.pl/kurs-euro/")
    #print(f"exchange values {data}")
    data_str = json.dumps(data)
    publish_data(PROJECT_ID, TOPIC_ID, data_str)
    time.sleep(DELAY_SLEEP)


 