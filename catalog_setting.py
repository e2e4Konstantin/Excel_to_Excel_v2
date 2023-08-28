
classifier = ['chapters', 'collections', 'sections', 'subsections', 'tables']

catalog_item = dict[str: str]

""" каталог из файла catalog.xlsx """
catalog: dict[str: catalog_item] = {
    'chapters': None,
    'collections': None,
    'sections': None,
    'subsections': None,
    'tables': None
}

""" структура каталога построенная по данным из файла template_all_output.xlsx """
used_structure: dict[str: catalog_item] = {
    'chapters': None,
    'collections': None,
    'sections': None,
    'subsections': None,
}

