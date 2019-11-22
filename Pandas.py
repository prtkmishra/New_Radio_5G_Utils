from itertools import product
import pandas as pd
import numpy as nps


display_settings = {
    'max_columns': 10,
    'expand_frame_repr': True,  # Wrap to multiple pages
    'max_rows': 10,
    'precision': 2,
    'show_dimensions': True
}

# Vertical concat
# pd.concat([october_df, november_df, december_df], axis=0)

# Horizontal concat
# pd.concat([features_1to5_df, features_6to10_df, features_11to15_df], axis=1)

# pd.merge(left=ids_and_time_df,
         # right=ids_and_videos_df,
         # on="id")
         
         
for op, value in display_settings.items():
    pd.set_option("display.{}".format(op), value)
    
players_data = {'Player': ['Superman', 'Batman', 'Thanos', 'Batman', 'Thanos',
   'Superman', 'Batman', 'Thanos', 'Black Widow', 'Batman', 'Thanos', 'Superman'],
   'Year': [2000,2000,2000,2001,2001,2002,2002,2002,2003,2004,2004,2005],
   'Points':[23,43,45,65,76,34,23,78,89,76,92,87]}
   
df = pd.DataFrame(players_data)

print(df)

df = df.T
print(df)



"""Groupby"""
groups_df = df.groupby('Player')

for player, group in groups_df:
   print("----- {} -----".format(player))
   print(group)
   print("")
   
"""Stacking """
df = df.stack()

print(df)