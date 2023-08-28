from datautils import get_data_from_file, read_catalog
from excelutils import data_out_to_excel


def main():
    # path = r"C:\Users\kazak.ke\Documents\Задачи\3_Reverse_to_excel"
    # path = r"C:\Users\kazak.ke\PycharmProjects\Excel_To_Excel\src"

    path = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\Ex_to_Ex_v2\src"
    file = r"template_all_output.xlsx"


    # path = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\1_targets\3_Reverse_to_excel"
    # file = r"template_all_output.xlsx"

    get_data_from_file(file, path)
    print(f"<< {'-' * 70} >>")

    read_catalog(r"catalog.xlsx", path, 'Catalog')


    file = "template_x_xx.xlsx"
    data_out_to_excel(file, "./output", ["name", "stat"], grid=False)


if __name__ == "__main__":
    main()
