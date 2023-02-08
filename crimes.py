import pandas as pd
import re

f = open(r"crimesNospace.txt","r")
lines = f.readlines()
headers = lines[0:7]
# for l in headers:
#     print(l)
# print(headers[0].split("\n"))
col = []
for l in headers:
    col.append(l.split("\n")[0])

row = {'Class':'' , 'Incident #':'', 'Crime':'', 'Date/Time':'', 'Address':'', 'Accuracy':'', 'Agency':''}
dataList = []

count = 0
row = {'Class':'' , 'Incident #':'', 'Crime':'', 'Date_Time':'', 'Address':'', 'Accuracy':'', 'Agency':''}
for i, l in enumerate(lines[7:-1]):
    row['Class'] = l.split("\n")[0] if count == 0 else row['Class']
    row['Incident #'] = l.split("\n")[0] if count == 1 else row['Incident #']
    row['Crime'] = l.split("\n")[0] if count == 2 else row['Crime']
    row['Date_Time'] = l.split("\n")[0] if count == 3 else row['Date_Time']
    row['Address'] = l.split("\n")[0] if count == 4 else row['Address']
    row['Accuracy'] = l.split("\n")[0] if count == 5 else row['Accuracy']
    row['Agency'] = l.split("\n")[0] if count == 6 else row['Agency']
    
    dataList.append(row) if count == 6 else ''
    row = {'Class':'','Incident #':'','Crime':'','Date_Time':'','Address':'','Accuracy':'','Agency':''} if count==6 else row
    count+=1 if count < 6 else 0
df = pd.DataFrame.from_dict(data=dataList)
print(df.head())
df.to_csv('crimes.csv')

# apt = lines[8648:9870]
#slic = apt[0:100]
# col=['id','lat','lon','elevation','state','desc']
# df = pd.DataFrame(columns=col)
#
# for a in apt:
#     r = re.split('     |    |   |  | ', a)
#     r1 = re.split('  |-', a)
#     #print(r)
#     if not any(map(str.isdigit, r[len(r)-9])):
#         j = (f'{r[len(r)-9]} {r[len(r)-8]} {r[len(r)-7]} {r[len(r)-6]} {r[len(r)-5]}')
#         jls = j.lstrip('0123456789.- ')
#         jrs = jls.rstrip()
#     else:
#         j = (f'{r[len(r)-10]} {r[len(r)-9]} {r[len(r)-8]} {r[len(r)-7]} {r[len(r)-6]} {r[len(r)-5]}')
#         jls = j.lstrip('0123456789.- ')
#         jrs = jls.rstrip()
#     df.loc[len(df.index),:] = [r[0],r[1],r[2],r[3],r[4],jrs]
#
# df.to_csv('noaaApt.csv')
# print(df.tail(50))

