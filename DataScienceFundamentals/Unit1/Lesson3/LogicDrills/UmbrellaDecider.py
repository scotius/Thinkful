def take_umbrella(weather, rain_chance):
    # Function to determine whether to take an umbrella with you
    if (weather == 'sunny' and rain_chance < .50):
        return False
    elif (weather == 'cloudy' and rain_chance > .20):
        return True
    elif (weather == 'cloudy' and rain_chance <= .20):
        return False
    elif weather == 'rainy':
        return True
    else:
        return True
