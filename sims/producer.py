from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='cdp.dct-tech.local:9092')
for _ in range(100):
	producer.send('resources', b'Test text')
	producer.flush()
