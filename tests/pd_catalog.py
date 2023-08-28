import pandas as pd

f = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\Ex_to_Ex_v2\src\Catalog.xlsx"
sheet_name = 'Catalog'

parquet_f = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\Ex_to_Ex_v2\src\df_catalog.gzip"

# df = pd.read_excel(io=f, sheet_name=sheet_name)
# df = df[['CODE', 'TITLE']].astype(pd.StringDtype())
# print(df.info(verbose=False, show_counts=True, memory_usage=True))
# print(df.columns)
# print(df.dtypes)
# print(df.head(15))
# df.to_parquet(parquet_f,   compression='gzip')

df = pd.read_parquet(parquet_f)
df = df[['CODE', 'TITLE']].astype(pd.StringDtype())
print(df.info(verbose=False, show_counts=True, memory_usage='deep',))
print(df.columns)
print(df.dtypes)
print(df.head(15))


# code = df[df['CODE'].str.contains(pat=r"\d+\.\d+(?:-\d+){4}", case=False, regex=True)] # таблица

# Глава
# code = df[df['TITLE'].str.contains(r"^\s*Глава\s*\d+\.", case=False, regex=True)]
code = df[df['CODE'].str.contains(pat=r"^\s*\d+\s*$", case=False, regex=True)]
print(code.head(10))
print(f"размерность: {code.shape}")
print(code.to_records().tolist())  # index=False

# Сборник
# # code = df[df['TITLE'].str.contains(r"^\s*Сборник\s*\d+\.", case=False, regex=True)]
# code = df[df['CODE'].str.contains(pat=r"^\s*\d+\.\d+\s*$", case=False, regex=True)]
# print(code.head(10))
# print(f"размерность: {code.shape}")
# print(code.to_records(index=False).tolist())

# Отдел
# # code = df[df['TITLE'].str.contains(r"^\s*Отдел\s*\d+\.", case=False, regex=True)]
# code = df[df['CODE'].str.contains(pat=r"^\s*\d+\.\d+-\d+\s*$", case=False, regex=True)]
# print(code.head(10))
# print(f"размерность: {code.shape}")
# print(code.to_records(index=False).tolist())

# # Раздел
# # code = df[df['TITLE'].str.contains(r"^\s*Раздел\s*\d+\.", case=False, regex=True)]
# code = df[df['CODE'].str.contains(pat=r"^\s*\d+\.\d+(?:-\d+){2}\s*$", case=False, regex=True)]
# print(code.head(10))
# print(f"размерность: {code.shape}")
# print(code.to_records(index=False).tolist())

# Таблица
# code = df[df['TITLE'].str.contains(r"^\s*Таблица\s*\d+\.", case=False, regex=True)]
# code = df[df['CODE'].str.contains(pat=r"^\s*\d+\.\d+(?:-\d+){4}\s*$", case=False, regex=True)]
# print(code.head(10))
# print(f"размерность: {code.shape}")
# print(code.to_records(index=False).tolist()[:5])

