# C7-10 p.131

responses = {}

# set a flag for the polling to be active

polling_active = True

while polling_active:
    # Store name and response
    name = input('What is your name?')

    response = input('What would be your dream vacation?')

    # Store response in a dict that was named at the start
    responses[name] = response

    # See if anyone else is taking the poll
    repeat = input('Remaining Participants? (y/n)')

    if repeat.lower() == 'n':
        polling_active = False

    # Poll complete show results
print('\n---Poll Results---')
for name, response in responses.items():
    print(f'{name} would like to go to {response}')

