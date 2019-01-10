def categorize_study(p_value, requirements):
    bs_factor = 0
    if requirements == 6:
        bs_factor = 1
    elif requirements == 5:
        bs_factor = 2
    elif requirements == 4:
        bs_factor = 4
    elif requirements == 3:
        bs_factor = 8
    elif requirements == 2:
        bs_factor = 16
    elif requirements == 1:
        bs_factor = 32
    elif requirements == 0:
        bs_factor = 64
    result = p_value * bs_factor
    if result >= 0.15:
        return "Pants on fire"
    elif result >= 0.05 and result < 0.15:
        return "Needs review"
    elif result < 0.05 and requirements == 0:
        return "Needs review"
    elif result < 0.05:
        return "Fine"
