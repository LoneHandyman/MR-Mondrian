import pandas as pd

col_names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship',
         'race','gender','capital-gain','capital-loss','hours-per-week','native-country','income']
categorical = ['workclass','education','marital-status','occupation','relationship','gender','native-country','race','income']
to_keep = ['age','workclass','education','marital-status','occupation','race','gender','native-country','income'] # columns used in the paper
categorical_to_keep = [x for x in categorical if x in to_keep]
df = pd.read_csv("adult.all.txt", sep=",", header=None, names=col_names, 
                 index_col=False, engine='python')


# put column names in a dict for span computing using indices
zip_iterator = zip([x for x in range(9)], to_keep)
col_dict = dict(zip_iterator)

cat_dict = {k: v for k, v in col_dict.items() if v in categorical_to_keep}
