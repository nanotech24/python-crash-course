# C8-06 p.146 Write city_country() function that takes name city and country
# Print city name then the country the city is in. call 3 times with differet pairs.

def city_country(city, country):
    """Name a city and the country it resides in seperated by a comma."""
    print(f'"{city.title()}, {country.title()}"\n')


city_country("St. John's", 'Canada')

city_country("ottawa", "Ontario")

city_country('cairo', 'egypt')