import re
from catalog_setting import classifier, catalog
from datautils import read_catalog

if __name__ == "__main__":
    # path = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\Ex_to_Ex_v2\src"
    path = r"C:\Users\kazak.ke\PycharmProjects\Excel_to_Excel_v2\src"
    file = r"catalog.xlsx"
    sheet = 'Catalog'
    read_catalog(file, path, sheet)
    for item in classifier:
        print(f"{item}: {list(catalog[item].keys())[:5]}")

    chapters = catalog['chapters']
    ranked_chapters = [x for x in chapters.keys()]
    ranked_chapters.sort(key=lambda x: int(x))
    print(ranked_chapters)

    # chapter_re = re.compile(r"^\s*(\d+)(?:\.).*")

    chapter_re = re.compile(r"^\s*(\d+\.0(-0){2}).*") # только глава и таблица

    for chapter in ranked_chapters:
        tables = [table
                  for table in catalog['tables'].keys()
                  if chapter_re.match(table) and chapter_re.match(table).groups()[0] == chapter]

        print(f"{chapter!r}", chapters[chapter], tables[:5])
