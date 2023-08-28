import pandas as pd
from pandas import DataFrame
from filesutils import check_full_file_name, out_error_message_and_exit
from catalog_setting import catalog, classifier
import gc


def data_frame_info(df: DataFrame, mode: str = 'short'):
    print(df.info(verbose=False, show_counts=True, memory_usage='deep'))
    print(f"использовано памяти: {df.memory_usage(index=True, deep=True).sum():_} bytes")
    print(f"размерность: {df.shape}")
    # print(f"индексы: {df.index}")
    print(f"названия столбцов: {list(df.columns)}")
    print(f"типы данных столбцов: '{df.dtypes.values.tolist()}'")
    print(f"{df.head(5)}") if mode != 'short' else print('<-->')


def get_items_from_data_frame(data: DataFrame, item_name: str, mode: str = 'CODE'):
    item_pattern = {
        # 3,    3.1,    3.1-1,  3.1-1-1,    3.1-1-1-0-1
        'chapters': {'title': r"^\s*Глава\s*\d+\.", 'code': r"^\s*\d+\s*$"},
        'collections': {'title': r"^\s*Сборник\s*\d+\.", 'code': r"^\s*\d+\.\d+\s*$"},
        'sections': {'title': r"^\s*Отдел\s*\d+\.", 'code': r"^\s*\d+\.\d+-\d+\s*$"},
        'subsections': {'title': r"^\s*Раздел\s*\d+\.", 'code': r"^\s*\d+\.\d+(?:-\d+){2}\s*$"},
        'tables': {'title': r"^\s*Таблица\s*\d+\.", 'code': r"^\s*\d+\.\d+(?:-\d+){4}\s*$"}
    }
    if mode != 'CODE':
        pattern_re = item_pattern.get(item_name, None)['title']
    else:
        pattern_re = item_pattern.get(item_name, None)['code']
    if pattern_re:
        cut = data[data[mode].str.contains(pat=pattern_re, case=False, regex=True)]
        data_frame_info(cut)
        catalog[item_name] = {item[0]: item[1] for item in cut.to_records(index=False).tolist()}
        # print(f"{catalog[item_name]=}")
    else:
        out_error_message_and_exit('получение данных из Catalog', item_name)


def read_catalog(file_name: str = None, file_path: str = None, sheet_name: str = None):
    parquet_file = f"{file_name[:-4]}gzip"
    full_name = check_full_file_name(parquet_file, file_path)
    df = DataFrame()
    if full_name:
        try:
            df: DataFrame = pd.read_parquet(full_name)
        except Exception as err:
            out_error_message_and_exit(str(err), full_name)
    else:
        full_name = check_full_file_name(file_name, file_path)
        if full_name:
            try:
                df: DataFrame = pd.read_excel(io=full_name, sheet_name=sheet_name)
                df.to_parquet(f"{full_name[:-4]}gzip", compression='gzip')
            except Exception as err:
                out_error_message_and_exit(str(err), full_name)
    if not df.empty:
        df = df[['CODE', 'TITLE']].astype(pd.StringDtype())
        data_frame_info(df, mode='full')
        for i in classifier:
            get_items_from_data_frame(df, i)

        del df
        gc.collect()

    else:
        raise TypeError(OSError)

    # Глава
    # code = df[df['TITLE'].str.contains(r"^\s*Глава\s*\d+\.", case=False, regex=True)]
    # cut = df[df['CODE'].str.contains(pat=r"^\s*\d+\s*$", case=False, regex=True)]
    # data_frame_info(cut)
    # catalog['collections'] = {item[0]: item[1] for item in cut.to_records(index=False).tolist()}
    # print(f"{catalog['collections']=}")

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


if __name__ == "__main__":
    path = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\Ex_to_Ex_v2\src"
    file = r"catalog.xlsx"
    sheet = 'Catalog'
    read_catalog(file, path, sheet)
    for item in classifier:
        print(f"{item}: {list(catalog[item].keys())[:5]}")
