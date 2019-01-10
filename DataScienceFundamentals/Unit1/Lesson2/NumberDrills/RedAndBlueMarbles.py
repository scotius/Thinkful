def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Guesses the probability of guessing blue on the remaining marbles in a bag
    # of blue and red marbles
    start_total = blue_start + red_start
    pulled_total = blue_pulled + red_pulled
    current_blue = blue_start - blue_pulled
    current_total = start_total - pulled_total
    return current_blue / current_total
