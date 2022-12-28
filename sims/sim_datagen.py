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

    # Randomizing country and state/emirate/province from resources-values-countries.json
    with open('schema/resources-values-countries.json') as resource_values_countries:
        resource_data_countries = json.load(resource_values_countries)
        country_res_data = {"data":[]}
        random.seed()
        resource_country_randomizer=len(resource_data_countries["countries"])
        random_idx_country = random.randint(1,resource_country_randomizer)
        #print("Country Index")
        #print(random_idx_country-1)
        data_country_name = resource_data_countries["countries"][random_idx_country-1]["country"]
        country_state_randomizer = len(resource_data_countries["countries"][random_idx_country-1]["states"])
        if country_state_randomizer == 0:
            data_country_state_name = ""
        else:
            random_idx_country_state = random.randint(1,country_state_randomizer)
            data_country_state_name = resource_data_countries["countries"][random_idx_country-1]["states"]\
                [random_idx_country_state-1]
        #print("Country State Index")
        #print(random_idx_country_state-1)
        country_res_data["data"].append({"country":data_country_name,
                                        "state":data_country_state_name})

    # Randomzing resources from resources-values.json
    with open('schema/resources-values.json') as resource_values:
        resource_data = json.load(resource_values)
        resource_items = {"resources":[]}
        resources_randomizer=len(resource_data["resources"])
        random.seed()

        random_item = random.randint(1,42)
        for _ in range(random_item):
            random_qty = random.randint(100,10000)
            rand_prodcons = bool(random.getrandbits(1))
            if rand_prodcons:
                prod_cons = "produce"
            else:
                prod_cons = "consume"

            random_idx_area = random.randint(1,resources_randomizer)
            #print(random_idx_area)
            res_area_randomizer = len(resource_data["resources"][random_idx_area-1])
            random_idx_item = random.randint(1,res_area_randomizer)
            #print(resource_data["resources"][random_idx_item-1][random_idx_area-1])
            #print(random_idx_item)
            #print({"area":resource_data["resources"][random_idx_area-1]["area"],
            #      "prodcons":prod_cons,
            #      "item":resource_data["resources"][random_idx_area-1]["item"][random_idx_item-1],
            #      "qty":random_qty,
            #      "unit":resource_data["resources"][random_idx_area-1]["unit"]})
            #country_res_data["data"]["resources"].append({"area":resource_data["resources"][random_idx_area-1]["area"],
            #                                              "prodcons":prod_cons,
            #                                              "item":resource_data["resources"][random_idx_area-1]["item"][random_idx_item-1],
            #                                              "qty":random_qty,
            #                                              "unit":resource_data["resources"][random_idx_area-1]["unit"]})
            data_res_area = resource_data["resources"][random_idx_area-1]["area"]
            data_res_item = resource_data["resources"][random_idx_area-1]["item"][random_idx_item-1]
            data_res_unit = resource_data["resources"][random_idx_area-1]["unit"]
            resource_items["resources"].append({"area": data_res_area,
                                               "prodcons":prod_cons,
                                               "item": data_res_item,
                                               "qty":random_qty,
                                               "unit": data_res_unit})
            #resource_items["resources"].append({"area":resource_data["resources"][random_idx_area-1]["area"],
            #                      "prodcons":prod_cons,
            #                      "item":resource_data["resources"][random_idx_area-1]["item"][random_idx_item-1],
            #                      "qty":random_qty,
            #                      "unit":resource_data["resources"][random_idx_area-1]["unit"]})

        #print(resource_items)
        print("Country: ", data_country_name)
        print("State: ", data_country_state_name)
        print("Resources: ", random_item)
        country_res_data["data"].append(resource_items)
        #print(country_res_data)
        return(country_res_data)


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
    producer = KafkaProducer(bootstrap_servers = bootstrap)
    producer.send(topic,data)
    producer.flush

if __name__ == "__main__":
    print("Preparing Data Generator")

    #print(InitDataResource(country="United Arab Emirates", restype="agriculture"))
    print(RandomizeDataResource())

    bootstrap = "cdp.dct-tech.local:9092"
    #ProduceRandomData(InitDataResource("United Arab Emirates"))
    ProduceToKafka(bootstrap,"resource",RandomizeDataResource())