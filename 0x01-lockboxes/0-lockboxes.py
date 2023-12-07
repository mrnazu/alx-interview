def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    :param boxes: A list of lists where each inner list represents a box.
    :return: True if all boxes can be opened, else return False.
    """

    # Set to keep track of opened boxes
    open_boxes = {0}

    # List to keep track of keys
    keys = boxes[0]

    # Iterate through the keys and update the open boxes
    while keys:
        key = keys.pop()
        if 0 <= key < len(boxes) and key not in open_boxes:
            open_boxes.add(key)
            keys.extend(boxes[key])

    # Check if all boxes are opened
    return len(open_boxes) == len(boxes)

