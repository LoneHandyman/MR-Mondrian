# Mondrian-Driver impl.

from pid_tree import PID_tree
from typing import List, Tuple, Any

def mr_mondrian_driver(k: int, sensitive_cols: List[str]):
  pid_tree = PID_tree(k, sensitive_cols)
  