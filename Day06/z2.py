from args import INPUT_FILE
from queue import Queue
from collections import defaultdict

class KWindow:
    """structure implementing sliding, quick distinct element count and quick lookup"""

    def __init__(self, starting_window):
        self.k = len(starting_window)
        self.queue = Queue()
        self.map = defaultdict(int)
        for el in starting_window:
            self._add_element(el)

    def __contains__(self, element):
        return element in self.map

    def get_total_distinct(self):
        return len(self.map)

    def move_next(self, element):
        old_element = self.queue.get()
        self.map[old_element] -= 1
        if self.map[old_element] == 0:
            del self.map[old_element]
    
        self._add_element(element)

    def _add_element(self, el):
        self.map[el] += 1
        self.queue.put(el)
        

def solution():
    with open(INPUT_FILE, 'r') as file:
        datastream = next(file)
    
    MARK_LEN = 14
    window = KWindow(datastream[:MARK_LEN])
    i = MARK_LEN
    while(window.get_total_distinct() != MARK_LEN):
        window.move_next(datastream[i])
        i += 1
    
    return i
        


print(solution())