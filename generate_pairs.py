import pandas as pd

folder_nc = '/media/socialmedia/OONI_Russia_2022_Summary/'

filename = 'Russia_2022_Matrix_MAX_ASN_resolverIP.csv'
df = pd.read_csv(folder_nc + filename, index_col=0)
row_size = len(df.index)
cols = df.columns

for idx_row, (_, row) in enumerate(df.iterrows()):
    for idx_col, col in enumerate(cols):
        if row[col] != -100:
            print(1+idx_row, 1+row_size+idx_col)