import numpy as np
import pandas as pd

def anonymize_df(df, partitions, quasi_identifiers, sensitive_data, cat_dict, mode = 'range'):
    anon_df = []
    categorical = [k for k, v in cat_dict.items()]

    for ip, p in enumerate(partitions):
        aggregate_values_for_partition = []
        partition = df[p]

        for column in quasi_identifiers:
            if column in categorical:
                values = list(np.unique(partition[:,column]))
                aggregate_values_for_partition.append(','.join(values))
            else:
                if mode == 'range':
                    col_min = np.min(partition[:,column])
                    col_max = np.max(partition[:,column])
                    if col_min == col_max:
                        aggregate_values_for_partition.append(col_min)
                    else:
                        aggregate_values_for_partition.append('{}-{}'.format(col_min,col_max))
                elif mode == 'mean':
                    aggregate_values_for_partition.append(np.mean(partition[:,column]))
        
        for i in range(len(p)):
            sensitive_value = df[p[i],sensitive_data][0]
            anon_df.append([int(p[i])]+aggregate_values_for_partition+[sensitive_value])
    
    df_anon = pd.DataFrame(anon_df)
    dfn1 = df_anon.sort_values(df_anon.columns[0])
    dfn1 = dfn1.iloc[:,1:]
    return np.array(dfn1)