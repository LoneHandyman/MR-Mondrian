import json

class TaxTree:
  def __init__(self, path: str):
    with open(path, 'r') as f:
      self.data = json.load(f)
    self.tax_tree_keys = list(self.data.keys())
    self.tax_states = {}

  def down_level_in_tax(self, tax_id: str, branch_id: str):
    path = self.curr_node_path_in_tax(tax_id)

    if path is not None:
      next_lvl = self.data[tax_id]['values']

      for key_attr in path:
        assert(key_attr in next_lvl.keys())
        next_lvl = next_lvl[key_attr]

      assert(branch_id in next_lvl.keys())

      next_lvl = next_lvl[branch_id]
      self.tax_states[tax_id].append(branch_id)

      return next_lvl
      
  def curr_node_path_in_tax(self, tax_id: str):
    if tax_id in self.tax_tree_keys:
      prompt_tax = self.data[tax_id]

      if tax_id not in self.tax_states.keys():
        tax_keys_l = list(prompt_tax['values'].keys())
        self.tax_states[tax_id] = [tax_keys_l[0]]#node path

      return self.tax_states[tax_id]
    
    return None

  def curr_where_in_tax(self, tax_id: str):
    path = self.curr_node_path_in_tax(tax_id)
    if path is not None:
      return path[-1]
    
    return None

  def get_onetype_tax(self, type: str):
    dict_tax = {}
    for key in self.tax_tree_keys:
      tax = self.data[key]
      if tax['type'] == type:
        dict_tax[key] = tax

    return dict_tax

o = TaxTree(path="../data/taxonomy_adult.json")

print(o.get_onetype_tax('discrete'))
print(o.get_onetype_tax('continuous'))
print(o.curr_where_in_tax('workclass'))
print('=================================================================')
print(o.down_level_in_tax('workclass', 'Worked'))
print(o.curr_node_path_in_tax('workclass'))
print(o.down_level_in_tax('workclass', 'With-Pay'))
print(o.curr_node_path_in_tax('workclass'))
print(o.down_level_in_tax('workclass', 'Private'))
print(o.curr_node_path_in_tax('workclass'))
print(o.curr_where_in_tax('workclass'))