def calculate_box_size(index):
    if index <= 1:
        return 8

    return calculate_box_size(index - 1) + (4 * 2 * index)

def calculate_width(index):
    if index <= 1:
        return 3

    return calculate_width(index - 1) + 2