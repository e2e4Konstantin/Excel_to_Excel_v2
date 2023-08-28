import re
#
import pandas as pd
import numpy as np
# Для объектного типа используется numpy.nan. Для строкового типа используется pandas.NA.

df = pd.read_csv('pd_match.csv')
print(df.head(15))
print(df.info())
df['F'] = df['F'].astype(pd.StringDtype())

code = df['F'].str.contains(pat=r"\d+\.\d+(?:-\d+){4}", case=False, regex=True)
print(code)
#
# code = df['F'].str.extract(pat=r"(?:\s*)(\d+\.\d+(?:-\d+){4}?)(?:\s*)")
# print(code)


#
# # df=df[df['name'].str.contains(r'(?<!\d)\d{6}(?!\d)')]

s = "  3.1-1-1-0-4, aa 3.1-1-1-0-2  888"
p = re.compile(r"(?:\s*)(\d+\.\d+(?:-\d+){4}?)(?:\s*)")

print(p.findall(s))
print(p.match(s))
if p.match(s): print(p.match(s).span())
print(p.search(s), ' -- ', p.search(s).group(0))