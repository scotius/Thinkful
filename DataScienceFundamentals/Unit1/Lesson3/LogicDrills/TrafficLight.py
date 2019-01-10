def update_light(current):
    # Function to determine current traffic light color
    # and decide what the next light color should be.
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'
