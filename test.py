from datetime import datetime
s = "24.05.2022"
o = datetime.strptime(s,'%d.%m.%Y')
print(o)