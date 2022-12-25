# Data Generator for Simulating input or output of a city
# Brief:
#  - The 'input' is the resource consumption of a city
#  - The 'output' is the resource production from a city

import random
import json

def init_data_gen():
    # Initialize data generator from various data sources
    # Possible data_sets parameters are:
    # - all - get all resources listed in resources-values*.json
    # TODO: make 'all' parameter to read the resources-values*.json

    # open data for resource-values.json for list of resources
    with open('schema/resources-values.json') as resource_values:
        resource_data = json.load(resource_values)
        print(resource_data)

    # open data for resource-values-countries.json for list of countries
    with open('schema/resources-values-countries.json') as resource_values_countries:
        resource_data_countries = json.load(resource_values_countries)
        print(resource_data_countries)

if __name__ == "__main__":
    init_data_gen()

    # List of data set elements
    #data_set = [1, 2, 3, 4, 5]

    # Select a random element from the data set
    #random_element = random.choice(data_set)
    #print(random_element)