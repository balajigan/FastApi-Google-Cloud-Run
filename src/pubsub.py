import os
from google.cloud import pubsub_v1

class PubSub:
  def publishMessage(cls,resource_type,data_str):
    publisher = pubsub_v1.PublisherClient()
    topic_name = 'projects/mytemporaryproject28490/topics/gcp-resource-topic'
    #publisher.create_topic(name=topic_name)
    #future = publisher.publish(topic_name, b'My first message!', spam='eggs')
    data = data_str.encode("utf-8")
    future = publisher.publish(topic_name, data, resourceType=resource_type)
    
    future.result()

  def callback(message):
    print(message.data)
    message.ack()
    
  def registerSubscriber(cls):
    topic_name = 'projects/mytemporaryproject28490/topics/gcp-resource-topic'
    subscription_name = 'projects/mytemporaryproject28490/subscriptions/gcp-resource-topic-sub'

  with pubsub_v1.SubscriberClient() as subscriber:
    subscriber.create_subscription(name=subscription_name, topic=topic_name)
    future = subscriber.subscribe(subscription_name, callback)
  
# End of class  
