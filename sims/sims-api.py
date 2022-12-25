from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'you have landed safely'


import random

# List of data set elements
data_set = [1, 2, 3, 4, 5]

# Select a random element from the data set
random_element = random.choice(data_set)
print(random_element)

