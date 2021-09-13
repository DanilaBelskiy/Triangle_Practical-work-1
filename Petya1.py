555666a=[]
from math import sqrt
for i in range(1,51):
    a.append(i)
a.sort(reverse=True)
print (a)
max=(0)
for i in range(1,51):
    str1=a[max]
    str2=a[max+1]
    str3=a[max+2]
    if (str1<str2+str3) and (str2<str1+str3) and (str3<str1+str2):
        p=((str1+str2+str3)//2)
        s=sqrt(p*(p-str1)*(p-str2)*(p-str3))
        print(s)
        print(str1,str2,str3)
        break



