"""
跳表的实现
"""
from typing import Optional
import random

class ListNode:

    def __init__(self, data: Optional[int] = None):
        self._data = data
        self._forwards = []

class SkipList:

    _MAX_LEVEL = 16

    def __init__(self):
        self._level_count = 1
        self._head = ListNode()
        self._head._forwards = [None] * type(self)._MAX_LEVEL

    def find(self, value: int) -> Optional[ListNode]:
        p = self._head
        for i in range(self._level_count -1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i] 

        return p._forwards[0] if p._forwards[0] and p._forwards[0]._data == value else None

    def insert(self, vlaue:int):
        level = self._random_level()
        if self._level_count < level:
            self._level_count = level
        new_node = ListNode(vlaue)
        new_node._forwards = [None] * level
        update = [self._head] * level

        p = self._head
        for i in range(level -1, -1, -1):
            while p._forwards[i] and p._forwards[i]._data < value:
                p = p._forwards[i]
            
            update[i] = p
        
        for i in range(level):
            new_node._forwards[i] = update[i]._forwards[i]
            update[i]._forwards[i] = new_node

    
    def _random_level(self, p: float = 0.5) -> int:
        level = 1
        while random.random() < p and level < type(self)._MAX_LEVEL:
            level += 1
        return level

    