import re

matcher = re.compile(r'^\d\d{2}-\d{11}')

if re.match(r'^\d\d{2}-\d{11}', '086-15538036797'):
    print(True)
else:
    print(False)
