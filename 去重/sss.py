import re

a = 'https://www.baidts.com%kkk'

a = re.sub(r'[https://]', '', a)

print(a)