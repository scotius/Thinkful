def process_data(data):
    number = 0
    product = 1
    for item in data:
        number = item[0] - item[1]
        product *= number
    return product
