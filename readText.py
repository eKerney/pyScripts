import pandas as pd
import re

f = open(r"allstations.txt","r")
lines = f.readlines()
apt = lines[8648:9870]
#slic = apt[0:100]
col=['id','lat','lon','elevation','state','desc']
df = pd.DataFrame(columns=col)

for a in apt:
    r = re.split('     |    |   |  | ', a)
    r1 = re.split('  |-', a)
    #print(r)
    if not any(map(str.isdigit, r[len(r)-9])):
        j = (f'{r[len(r)-9]} {r[len(r)-8]} {r[len(r)-7]} {r[len(r)-6]} {r[len(r)-5]}')
        jls = j.lstrip('0123456789.- ')
        jrs = jls.rstrip()
    else:
        j = (f'{r[len(r)-10]} {r[len(r)-9]} {r[len(r)-8]} {r[len(r)-7]} {r[len(r)-6]} {r[len(r)-5]}')
        jls = j.lstrip('0123456789.- ')
        jrs = jls.rstrip()
    df.loc[len(df.index),:] = [r[0],r[1],r[2],r[3],r[4],jrs]

df.to_csv('noaaApt.csv')
print(df.tail(50))


