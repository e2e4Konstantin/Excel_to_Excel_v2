# p1 = lambda x: x.isdigit() and int(x)
# p2 = lambda x: len(set('.,').intersection(x))==1 and bool(x.replace(',', '.', 1)) and float(x)
#
#
# # numbers = '125,55'
# # numbers = 125.55
# numbers = ' '
#
# def string_to_number(number:str):
#     match number:
#         case int() | float() as num:
#             return num
#         case str() as num if num.isdigit():
#             return int(num)
#         case str() as num if num.replace(',', '', 1).replace('.', '', 1).isdigit():
#             return float(num.replace(",", ".", 1))
#         case _:
#             return None
#
#
# print(string_to_number(numbers))
#
# #
# # x = '125,55'
# #
# # # print(p1('125'), p1('125.55'))
# # # print(p2('951.33'), p2('125,55'))
# #
# #
# # print(x.replace(',', '.', 1))

s = {('5', 'Глава  5. Пусконаладочные работы'), ('3', 'Глава  3. Строительные работы')}
for x in s:
    print(x)