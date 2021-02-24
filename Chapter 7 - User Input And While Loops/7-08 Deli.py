# C7-08 p.131 see instructions on page

# Making the list of sandwiches

sandwich_orders = ['bologna', 'chicken', 'cold cut', 'steak', 'grilled cheese', ]

finished_sandwiches = []

while sandwich_orders:

    current_order = sandwich_orders.pop(0)

    print(f'{current_order} sandwich is being made!\n')

    finished_sandwiches.append(current_order)

print(', '.join(finished_sandwiches) + ' sandwiches were all made!')