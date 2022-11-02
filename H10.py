# Karl Robert Masing
# 25.10.2022
# Harjutus 10
import re

#kuva korralikud paroolid
a=open("IP.txt")
for line in a:
    if re.search("^[a-z,0-9]+[A-Z]{1}", line):
        print(line,end="")



print("---------------------------------------")
#kuva failist korralikud IP-d
#^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$
#^\d[0-9.]{1,3}\d[0-9.]{1,3}\d[0-9.]{1,3}\d[0-9.]{1,3}
a=open("IP.txt")
for line in a:
    if re.search("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", line):
        print(line,end="")