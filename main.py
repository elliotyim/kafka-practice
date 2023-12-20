from kafka import KafkaConsumer, KafkaProducer


producer = KafkaProducer(bootstrap_servers="localhost:29092")

future = producer.send("my-topic", b"some_message_bytes")
result = future.get(timeout=60)

result

# consumer = KafkaConsumer("my-topic", bootstrap_servers="localhost:29092")

# for msg in consumer:
#     print(msg)
