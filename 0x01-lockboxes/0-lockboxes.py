#!/usr/bin/python3
"""Lockboxes Puzzle Solution"""


def canUnlockAll(boxes):
    """Determines whether all the boxes can be unlocked"""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    for key_to_check in range(1, len(boxes) - 1):
        unlocked = False
        for box_index in range(len(boxes)):
            unlocked = (
                key_to_check in boxes[box_index] and
                key_to_check != box_index
            )
            if unlocked:
                break
        if not unlocked:
            return unlocked

    return True