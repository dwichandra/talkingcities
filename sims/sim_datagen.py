# Data Generator for Simulating input or output of a city
# Brief:
#  - The 'input' is the resource consumption of a city
#  - The 'output' is the resource production from a city

import random
import json
from kafka import KafkaProducer

def RandomizeDataResource():
    # Initialize data generator from various data sources
    # Possible data_sets parameters are:
    # - all - get all resources listed in resources-values*.json
    # TODO: make 'all' parameter to read the resources-values*.json

    print("Generating random data")

    with open('schema/resources-values.json') as resource_values:
        resource_data = json.load(resource_values)
        resource_items = []
        resources_randomizer=len(resource_data["resources"])
        #print(resources_randomizer)
        random.seed()

        #for resource in resource_data["resources"]:
        #    if resource["area"] == kwargs["restype"]:
        #        resource_items.append(resource["item"])
        for _ in range(10):
            random_qty = random.randint(100,10000)
            rand_prodcons = bool(random.getrandbits(1))
            if rand_prodcons: prod_cons = "produce"
            else: prod_cons = "consume"

            random_idx_area = random.randint(1,resources_randomizer)
            #print(random_idx_area)
            res_area_randomizer = len(resource_data["resources"][random_idx_area-1])
            random_idx_item = random.randint(1,res_area_randomizer)
            #print(resource_data["resources"][random_idx_item-1][random_idx_area-1])
            #print(random_idx_item)
            print(resource_data["resources"][random_idx_area-1]["area"],
                  prod_cons,
                  resource_data["resources"][random_idx_area-1]["item"][random_idx_item-1],
                  random_qty,
                  resource_data["resources"][random_idx_area-1]["unit"])


        #print(resource_items)

            #print(len(resource_data["resources"]))

            #for array_idx in len(resource_data["resources"]):
                #if kwargs["restype"] == resource_data["resources"][array_idx-1]:
                #    print(resource_data[resource_data][array_idx])
            #if kwargs["restype"] in resource_data["resources"]["area"]:
            #    print("found")
            #else:
            #    print("not found")
            #print(resource_data)

    # open data for resource-values-countries.json for list of countries
    #with open('schema/resources-values-countries.json') as resource_values_countries:
    #    resource_data_countries = json.load(resource_values_countries)
    #    if country in resource_data_countries['countries'][0]:
    #        print("found")
    #        country_state = random.choice(resource_data_countries[country])
    #    else:
    #        print('not found')
    #        country_state = "test"
        #print(resource_data_countries)

    #return resource_data, resource_data_countries
    #print(country_state)
    #return country_state

#def ProduceRandomData(dataset):
#    random_selection = random.choice(dataset)
#    print(random_selection)
#    return(random_selection)
    # List of data set elements
    #data_set = [1, 2, 3, 4, 5]

    # Select a random element from the data set
    #random_element = random.choice(data_set)
    #print(random_element)

def ProduceToKafka(bootstrap,topic,data):
    producer = KafkaProducer(bootstarp_server=bootstrap)
    producer.send(topic,data)
    producer.flush

if __name__ == "__main__":
    print("Preparing Data Generator")

    #print(InitDataResource(country="United Arab Emirates", restype="agriculture"))
    print(RandomizeDataResource())

    #producer = KafkaProducer(bootstrap_servers='cdp.dct-tech.local:9092')
    #ProduceRandomData(InitDataResource("United Arab Emirates"))