from openpyxl.utils.cell import coordinate_from_string, column_index_from_string


def column_number_generate() -> dict[str: int]:
    """ Генерирует словарь вида {'AZ': 52, 'a': 1, 'b': 2} для определения номера столбца по букве """

    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    alphabet.extend([alphabet[0] + v for v in alphabet])
    lc_alphabet = list('abcdefghijklmnopqrstuvwxyz')
    lc_alphabet.extend([lc_alphabet[0] + v for v in lc_alphabet])
    letter_column_number = {v: i + 1 for i, v in enumerate(alphabet)}
    letter_column_number.update({v: i + 1 for i, v in enumerate(lc_alphabet)})
    return letter_column_number



if __name__ == "__main__":
    x = column_number_generate()
    print(x)
    print(coordinate_from_string('B12'))
    print(column_index_from_string('BB'))