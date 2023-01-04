"""
Data Generator for Simulating input or output of a city resources
# Brief:
#  - The 'consume' is the resource consumption of a city
#  - The 'produce' is the resource production from a city
"""

import random
import json
import logging
from kafka import KafkaProducer
from kafka.errors import KafkaError


def randomize_data_resource():
    """
    Initialize data generator from various data sources
    :return:
    """

    print("Generating random data")

    # Randomizing country and state/emirate/province from resources-values-countries.json
    with open('schema/resources-values-countries-uae-dxb.json', encoding="utf-8")\
            as resource_values_countries:
        resource_data_countries = json.load(resource_values_countries)
        country_res_data = {"data": []}
        random.seed()
        resource_country_randomizer = len(resource_data_countries["countries"])
        random_idx_country = random.randint(1, resource_country_randomizer)
        data_country_name = resource_data_countries["countries"][random_idx_country - 1]["country"]
        country_state_randomizer = len(resource_data_countries["countries"]\
                                           [random_idx_country - 1]["states"])
        if country_state_randomizer == 0:
            data_country_state_name = ""
        else:
            random_idx_country_state = random.randint(1, country_state_randomizer)
            data_country_state_name = resource_data_countries["countries"]\
                [random_idx_country - 1]["states"]\
                [random_idx_country_state - 1]

    # Randomzing resources data from resources-values.json
    with open('schema/resources-values.json', encoding="utf-8") as resource_values:
        resource_data = json.load(resource_values)
        resource_items = {"resources": []}
        resources_randomizer = len(resource_data["resources"])
        random.seed()

        # Pick a random number for generating resources data
        random_item = random.randint(10, 100)
        for _ in range(random_item):
            random_qty = random.randint(100, 10000)
            rand_prodcons = bool(random.getrandbits(1))
            if rand_prodcons:
                prod_cons = "produce"
            else:
                prod_cons = "consume"

            random_idx_area = random.randint(1, resources_randomizer)
            res_area_randomizer = len(resource_data["resources"][random_idx_area - 1])
            random_idx_item = random.randint(1, res_area_randomizer)
            data_res_area = resource_data["resources"][random_idx_area - 1]["area"]
            data_res_item = resource_data["resources"][random_idx_area - 1]["item"]\
                [random_idx_item - 1]
            data_res_unit = resource_data["resources"][random_idx_area - 1]["unit"]
            resource_items["resources"].append({"area": data_res_area,
                                                "prodcons": prod_cons,
                                                "item": data_res_item,
                                                "qty": random_qty,
                                                "unit": data_res_unit})

        print("Country: ", data_country_name)
        print("State: ", data_country_state_name)
        print("Resources: ", random_item)
        country_res_data["data"].append({"country": data_country_name})
        country_res_data["data"].append({"state": data_country_state_name})
        country_res_data["data"].append(resource_items)

        return country_res_data


def produce_to_kafka(bootstrap, data_topic, data):
    """
    Producing data to kafka
    :param bootstrap: bootstrap server
    :param data_topic: topic
    :param data: data payload
    :return:
    """
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                             bootstrap_servers=[bootstrap],
                             linger_ms=10)

    # Asynchronous by default
    future = producer.send(data_topic, data)

    # Block for 'synchronous' sends
    try:
        print("Attempting to send data to Kafka at", bootstrap)
        record_metadata = future.get(timeout=10)

    except KafkaError:
        logging.error("We got Kafka Error!")
        # pass
    else:
        # Successful result returns assigned partition and offset
        print("Data sent successfully!")
        print("     Topic:", record_metadata.topic)
        print("     Partition:", record_metadata.partition)
        print("     Offset:", record_metadata.offset)
        producer.flush

if __name__ == "__main__":
    print("Preparing Data Generator for Resources")
    bootstrap = "cdp.dct-tech.local:9092"
    kafka_topic = "resources"
    # ProduceRandomData(InitDataResource("United Arab Emirates"))
    produce_to_kafka(bootstrap,
                   kafka_topic,
                   randomize_data_resource())
