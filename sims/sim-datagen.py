import random
import json

def init-data-gen():
    # open data for resource-values.json for list of resources
    with open('schema/resources-values.json') as resource_values:
        resource_data = json.load(resource_values)
        #print(resource_data)

    # open data for resource-values-countries.json for list of countries
    with open('schema/resources-values-countries.json') as resource_values_countries:
        resource_data_countries = json.load(resource_values_countries)
        #print(resource_data_countries)

if __name__ == "__main__":


# List of data set elements
#data_set = [1, 2, 3, 4, 5]

# Select a random element from the data set
#random_element = random.choice(data_set)
#print(random_element)

