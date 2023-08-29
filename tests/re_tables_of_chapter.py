import re

s = "3.0-0-0-0-1, 3.00-1-1-0-1, 3.51-1-1-0-2,"
l = ['9.1-1-1-0-2', ' 9.1-1-1-0-1', '999-885', '8.2-1-1-0-3', ' 8.2-1-1-0-2', '8.2-1-1-0-1']

code = re.compile(r"^\s*(\d+)(?:\.).*")

for x in l:
    r = code.match(x)
    g = None
    if r:
        g = r.groups()
    print(x, r, g)


c = lambda x: "True" if (x%2 == 0) else "False"

c = lambda x: "True" if (x%2 == 0) else "False"

