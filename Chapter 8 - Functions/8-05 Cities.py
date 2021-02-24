# C8-05 p.141 write a func called describe_city() that accepts
# The name and country of a ciy. print a sentence such as "dildo is in canada"
# Give the country parameter a default value, and call your func for 3
# different cities, with at least 1 not being in the defailt country

def describe_city(city, country='Canada'):
    """Names a city and the country it is located in."""

    print(f'{city} is a city located in {country}.')

describe_city('Ottawa')

describe_city('New York', 'United States')

describe_city('London')