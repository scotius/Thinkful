def color_probability(color, texture):
    # Return the probability of a marble's color based on its texture.
    if texture == 'smooth':
        return '0.33'
    elif texture == 'bumpy' and color == 'green':
        return '0.14'
    elif texture == 'bumpy' and color == 'yellow':
        return '0.28'
    elif texture == 'bumpy' and color == 'red':
        return '0.57'
