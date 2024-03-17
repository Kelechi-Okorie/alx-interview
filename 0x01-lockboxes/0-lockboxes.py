#!/usr/bin/python3
"""
Lockboxes implementation
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened

    parameters:
    - boxes (list): list of all the boxes

    Returns
    - True if all boxes can be opened, False otherwise
    """

    visited = [False] * len(boxes)
    visited[0] = True
    keys = [0]

    while keys:
        cur_key = keys.pop()
        cur_box = boxes[cur_key]

        for key in cur_box:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                keys.append(key)

    # Check if all boxes have been visited
    return all(visited)
