from itertools import count
import queue
from typing import List, Dict, Any

class PID_node:
  def __init__(self, id: int, available_attrs: List[str]):
    self.partition_id = id
    self.quasi_identifier = []
    self.split_attr = None
    self.split_value = None
    self.a_ava = available_attrs
    self.partition_size = 0
    self.children = []

  def is_leaf(self):
    return len(self.children) == 0

class PID_tree:
  def __init__(self, k: int, targets: List[str], taxonomy_trees: List[Dict[str, Any]]):
    self.root = None
    self.taxonomy_trees = taxonomy_trees
    self.anonymity_criterion = k
    self.cols_to_anonymize = targets
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


  def insert(self, split_attr: str, split_value):
    if self.root is None:
      self.root = PID_node(next(self.pid_generator), self.cols_to_anonymize)
      self.root.quasi_identifier = [None] * len(self.cols_to_anonymize)

    parent = self.__find_parent_node(self.root)

    if parent is not None:
      new_node = PID_node(next(self.pid_generator), parent.a_ava)
      new_node.split_attr = split_attr
      new_node.split_value = split_value
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