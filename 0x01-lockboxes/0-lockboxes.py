#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list of list): A list of lists where each inner list represents a box.

    Returns:
        bool: True if all boxes can be opened, else return False.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if not boxes_checked:
            return boxes_checked
    
    return True

if __name__ == "__main__":
    pass  # Add any script-specific execution logic here if needed

