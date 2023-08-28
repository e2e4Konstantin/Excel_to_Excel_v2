import re

s = "3.0-0-0-0-1, 3.00-1-1-0-1, 3.51-1-1-0-2,"

code_collection_re = re.compile(r"^\s*(\d+)(?:\.\d+)")
code_section_re = re.compile(r"^\s*(\d+\.\d+)(?:\-\d+)")

r1 = code_collection_re.match(s).groups()
r2 = code_section_re.match(s).groups()

print(r1)
print(r2)