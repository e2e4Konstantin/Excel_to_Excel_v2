import pandas as pd

#create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
 'position': ['G', 'G', 'F', 'F', 'G', 'G', 'F', 'F'],
 'assists': [5, 7, 7, 9, 12, 9, 9, 4],
 'rebounds': [11, 8, 10, 6, 6, 5, 9, 12]})
#
print(df.info())

df.set_index(['position'])
print(df.index)

x = df.loc[df['position'] == 'G']
print(x)


ll = df.index[df['position'] == 'G'].tolist()
print(ll)


k = df.loc[df['position'] == 'G'].to_records()
print(type(k),k )


n = df.loc[df['position'] == 'G'].to_records().tolist()
print(type(n), n)


