from kafka import KafkaConsumer
consumer = KafkaConsumer('resources')
for msg in consumer:
	print(msg)
