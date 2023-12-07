#!/usr/bin/python3

"""
Determine if all the boxes can be opened.

:param boxes: A list of lists where each inner list represents a box.
:return: True if all boxes can be opened, else return False.
"""

def canUnlockAll(boxes):
"""
Determine if all the boxes can be opened.

:param boxes: A list of lists where each inner list represents a box.
:return: True if all boxes can be opened, else return False.
"""

    open_boxes = {0}

    keys = boxes[0]

    while keys:
        key = keys.pop()
        if 0 <= key < len(boxes) and key not in open_boxes:
            open_boxes.add(key)
            keys.extend(boxes[key])

    return len(open_boxes) == len(boxes)

