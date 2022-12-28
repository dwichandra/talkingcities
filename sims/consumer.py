from kafka import KafkaConsumer
consumer = KafkaConsumer('resources',bootstrap_servers='cdp.dct-tech.local:9092')
for msg in consumer:
	print(msg)
