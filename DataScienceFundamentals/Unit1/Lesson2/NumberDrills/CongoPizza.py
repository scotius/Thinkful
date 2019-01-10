def box_capacity(length, width, height):
    # Determine the number of frozen pizza containers that can fit in
    # a warehouse given its dimensions in feet
    # Should return an integer value
    return (length * 12 // 16) * (width * 12 // 16) *  (height * 12 // 16)
