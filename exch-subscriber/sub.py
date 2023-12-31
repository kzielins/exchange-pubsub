"""
Docs for sub GCP pubsub

TODO !!

"""
import os,json,time

from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from google.api_core.exceptions import AlreadyExists

SERVICE_ACCOUNT_PATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS",'./exchnage-pubsub-sa.json')
PROJECT_ID = os.environ.get('PROJECT_ID',"exchnage-pubsub")
TOPIC_ID = os.environ.get('TOPIC_ID',"my-topic")

#container_name = os.environ.get('HOSTNAME')
#sub = f"sub-{container_name}-{uuid.uuid4().hex}"
SUBSCRIPTION_ID=os.environ.get('SUBSCRIPTION_ID',"my-sub")
DELAY_SLEEP = int(os.environ.get('DELAY_SLEEP',5))

# Number of seconds the subscriber should listen for messages
TIMEOUT = 5.0
  
  
def main():
  """Continuously pull messages from subsciption"""
 
  create_subscription(PROJECT_ID, TOPIC_ID, SUBSCRIPTION_ID)
      
  subscriber = pubsub_v1.SubscriberClient.from_service_account_json(SERVICE_ACCOUNT_PATH)
  # The `subscription_path` method creates a fully qualified identifier
  # in the form `projects/{project_id}/subscriptions/{subscription_id}`
  subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)
  
  flow_control = pubsub_v1.types.FlowControl(max_messages=10)
  streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback, flow_control=flow_control)
  print(f"Listening for messages on {subscription_path}..\n")
  
  # Wrap subscriber in a 'with' block to automatically call close() when done. 
  with subscriber:
      try:
          # When `timeout` is not set, result() will block indefinitely,
          # unless an exception is encountered first.
          # streaming_pull_future.result(timeout=TIMEOUT)
          streaming_pull_future.result()
      except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.
 
 

def create_subscription(project_id, topic_id, subscription_id):
  """create subscription if not exist  project_id -> topic if not exists"""
  subscriber = pubsub_v1.SubscriberClient.from_service_account_json(SERVICE_ACCOUNT_PATH)
  subscription_path = subscriber.subscription_path(project_id, subscription_id)
  try:
    topic_path = subscriber.topic_path(project_id, topic_id)
    with subscriber:
      subscription = subscriber.create_subscription(
          request={"name": subscription_path, "topic": topic_path}
      )
    print(f"Created subscription: {subscription_path}")
  except AlreadyExists:
    #print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f' [WARNING] Subscription subscription_path: {subscription_path} already exists')

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    """callback for subscriber """
    print(f"Received {message.data}.")
    message.ack()

if __name__ == '__main__':
  main()