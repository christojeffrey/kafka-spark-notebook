from time import sleep
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0, 10),
                         value_serializer=lambda x:
                         x.encode('utf-8'))

while True:
    message = "1 2 3 4 5 6"
    producer.send('variance', value=message)
    print("testing")
    sleep(2)