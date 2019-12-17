def describe_city(city, country='america'):
    """Displays a message with a city and the country it resides in."""
    print("\n" + city.title() + " is in " + country.title() + ".")

# default message
describe_city(city='Los Angelos')

# city number 2
describe_city(city="new york")

#city number 3
describe_city(city='tokyo', country='japan')