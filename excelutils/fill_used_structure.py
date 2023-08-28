from catalog_setting import catalog, used_structure
import re


def fill_used_structure(tables):
    """ Восстанавливает используемую в таблицах структуру данных """
    print(f"Восстанавливаем структуру данных по каталогу всего таблиц: {len(tables)}\n{tables[:3]}.....")

    code_chapter_re = re.compile(r"^\s*(\d+)(?:\.\d+)")
    code_collection_re = re.compile(r"^\s*(\d+\.\d+)(?:-\d+)")
    code_section_re = re.compile(r"^\s*(\d+\.\d+-\d+)(?:-\d+)")
    code_subsection_re = re.compile(r"^\s*(\d+\.\d+-\d+-\d+)(?:-\d+)")

    chapters_in_tables = []
    collections_in_tables = []
    sections_in_tables = []
    subsections_in_tables = []

    for table in tables:
        table_chapter_code = code_chapter_re.match(table[0]).groups()
        if table_chapter_code:
            chapter_code = table_chapter_code[0]
            chapters_in_tables.append((chapter_code, catalog['chapters'][chapter_code]))
        else:
            print(f"в коде таблицы: {table} код 'Главы' выделить не удалось")

        table_collection_code = code_collection_re.match(table[0]).groups()
        if table_collection_code:
            collection_code = table_collection_code[0]
            collections_in_tables.append((collection_code, catalog['collections'][collection_code]))
        else:
            print(f"в коде таблицы: {table} код 'Сборника' выделить не удалось")

        table_section_code = code_section_re.match(table[0]).groups()
        if table_section_code:
            section_code = table_section_code[0]
            section = catalog['sections'].get(section_code, None)
            if section:
                sections_in_tables.append((section_code, section))
            # else:
            #     print(f"для таблицы: {table[0]} код 'Отдел' {section_code} в каталоге не найден")
        else:
            print(f"в коде таблицы: {table} код 'Отдела' выделить не удалось")

        table_subsection_code = code_subsection_re.match(table[0]).groups()
        if table_subsection_code:
            subsection_code = table_subsection_code[0]
            subsection = catalog['subsections'].get(subsection_code, None)
            if subsection:
                subsections_in_tables.append((subsection_code, subsection))
            # else:
            #     print(f"для таблицы: {table[0]} код 'Раздел' {subsection_code} в каталоге не найден")
        else:
            print(f"в коде таблицы: {table} код 'Раздела' выделить не удалось")


    # print(f"{catalog['chapters'] = }")
    used_structure['chapters'] = {x[0]: x[1] for x in set(chapters_in_tables)}
    print(f"Главы: {len(used_structure['chapters'])} {used_structure['chapters'].values() = }")

    # print(f"{catalog['collections'] = }")
    used_structure['collections'] = {x[0]: x[1] for x in set(collections_in_tables)}
    print(f"Сборники: {len(used_structure['collections'])} {used_structure['collections'] = }")

    # print(f"{catalog['sections'] = }")
    used_structure['sections'] = {x[0]: x[1] for x in set(sections_in_tables)}
    print(f"Отделы: {len(used_structure['sections'])} {used_structure['sections'] = }")

    # print(f"{catalog['subsections'] = }")
    used_structure['subsections'] = {x[0]: x[1] for x in set(subsections_in_tables)}
    print(f"Разделы: {len(used_structure['subsections'])} {used_structure['subsections'] = }")
