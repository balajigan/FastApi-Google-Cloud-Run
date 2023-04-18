import os
from google.cloud import pubsub_v1

class PubSub:
  def publishMessage():
    publisher = pubsub_v1.PublisherClient()
    topic_name = 'projects/mytemporaryproject28490/topics/gcp-resource-topic'
    publisher.create_topic(name=topic_name)
    future = publisher.publish(topic_name, b'My first message!', spam='eggs')
    future.result()
  # End of class
