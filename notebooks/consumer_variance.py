from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'variance',
     bootstrap_servers=['kafka:9092'],
     api_version=(0, 10, 2),
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: x.decode('utf-8'))

print("Starting Kafka Consumer")
for message in consumer:
    print("Received message:", message.value)
