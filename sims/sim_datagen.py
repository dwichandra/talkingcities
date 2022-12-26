# Data Generator for Simulating input or output of a city
# Brief:
#  - The 'input' is the resource consumption of a city
#  - The 'output' is the resource production from a city

import random
import json
from kafka import KafkaProducer

def InitDataResource(**kwargs):
    # Initialize data generator from various data sources
    # Possible data_sets parameters are:
    # - all - get all resources listed in resources-values*.json
    # TODO: make 'all' parameter to read the resources-values*.json

    print("Initializing data sources")

    # open data for resource-values.json for list of resources
    match kwargs:
        case "country":
            print("Randomizing country data")
        case "restype":
            print("Randomizing resource type data")

    with open('schema/resources-values.json') as resource_values:
        resource_data = json.load(resource_values)
        if resource in resource_data['resource'][0]:
            print("found")
        else:
            print("not found")
        #print(resource_data)

    # open data for resource-values-countries.json for list of countries
    with open('schema/resources-values-countries.json') as resource_values_countries:
        resource_data_countries = json.load(resource_values_countries)
        if country in resource_data_countries['countries'][0]:
            print("found")
            country_state = random.choice(resource_data_countries[country])
        else:
            print('not found')
            country_state = "test"
        #print(resource_data_countries)

    #return resource_data, resource_data_countries
    print(country_state)
    return country_state

def ProduceRandomData(dataset):
    random_selection = random.choice(dataset)
    print(random_selection)
    return(random_selection)
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

    print(InitDataResource(country="United Arab Emirates",restype="agriculture"))

    producer = KafkaProducer(bootstrap_servers='cdp.dct-tech.local:9092')
    #ProduceRandomData(InitDataResource("United Arab Emirates"))