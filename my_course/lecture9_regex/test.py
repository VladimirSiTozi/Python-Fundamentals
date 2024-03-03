import re

txt = "The r:ain in Sp:ain"
pattern = '(:)(ai)'
x = re.search(pattern, txt)
print(x.group(2))