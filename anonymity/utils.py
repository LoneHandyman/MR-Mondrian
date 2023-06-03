import json

class TaxTree:
  def __init__(self, path):
    with open(path, 'r') as f:
      self.data = json.load(f)
    self.tax_tree_keys = self.data.keys()

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