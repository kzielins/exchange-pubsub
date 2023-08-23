import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="exchnage-pubsub-sa.json"

from google.cloud import pubsub_v1

# projects/exchnage-pubsub/topics/my-topic
#
project_id = "exchnage-pubsub"
subscription_id="my-sub5"
topic_id = "my-topic5"

publisher = pubsub_v1.PublisherClient()
#create topic if not exist  
try:
  topic_path = publisher.topic_path(project_id, topic_id)
  topic = publisher.create_topic(request={"name": topic_path})
  print(f"Created topic: {topic.name}")
except:
  print(f"Create topic {topic_id} failed ")
  
#create subscription if not exist  
try:
  subscriber = pubsub_v1.SubscriberClient()
  topic = subscriber.topic_path(project_id, topic_id)
  # The `subscription_path` method creates a fully qualified identifier
  # in the form `projects/{project_id}/subscriptions/{subscription_id}`
  subscription_path = subscriber.subscription_path(project_id, subscription_id)
  with subscriber:
    subscription = subscriber.create_subscription(
        request={"name": subscription_path, "topic": topic_path}
    )
  print(f"Created subscription: {subscription_path}")
except:
  print(f"Create subscription {subscription_id} failed ")
  
 
