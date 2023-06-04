from itertools import count
import queue
from typing import List, Tuple, Any

class PID_node:
  def __init__(self, pid: int, a_ava: List[str]):
    self.partition_id = pid
    self.quasi_identifier = []
    self.split_attr = None
    self.split_value = None
    self.a_ava = a_ava
    self.partition_size = 0
    self.children = []

  def set_split_index(self, split_attr: str, split_value):
    self.split_attr = split_attr
    self.split_value = split_value

  def is_leaf(self):
    return len(self.children) == 0
  
  def delete_from_A_ava(self, attr):
    self.a_ava.remove(attr)

class PID_tree:
  def __init__(self, k: int, targets: List[str]):
    self.root = PID_node(next(self.pid_generator), self.cols_to_anonymize)
    self.root.quasi_identifier = targets
    self.anonymity_criterion = k
    self.pid_generator = self.__generate_partition_ids(start_id=0)

  def __generate_partition_ids(start_id=0):
    generator = count(start=start_id)
    while True:
      yield next(generator)

  def search_partition(self, attr: str, value):
    assert(self.root != None)
    bfs = queue.Queue()
    bfs.put(self.root)
    while not bfs.empty():
      node = bfs.get()

      if node.split_attr == attr and node.split_value == value:
        return node.partition_id
      
      if len(node.children) > 0:
        for child in node.children:
          bfs.put(child)

    return None
  
  def insert(self, new_meta : List[Tuple[str, Any]], tax_leaf=True):
    parent = self.__find_parent_node(self.root)

    if parent is not None:
      for (split_attr, split_value) in new_meta:
        new_node = PID_node(next(self.pid_generator), parent.a_ava)

        if tax_leaf == True:
          new_node.delete_from_A_ava(split_attr)

        new_node.set_split_index(split_attr, split_value)
        new_node.quasi_identifier = parent.quasi_identifier.copy()
        new_node.quasi_identifier[parent.a_ava.index(split_attr)] = split_value
        parent.children.append(new_node)

        return new_node.partition_id
    
    return None
  
  def __find_parent_node(self, node: PID_node) -> PID_node:
    bfs = queue.Queue()
    bfs.put(node)
    while not bfs.empty():
      curr_node = bfs.get()

      if curr_node.is_leaf():
        return curr_node
      
      for child in curr_node.children:
        bfs.put(child)

    return None