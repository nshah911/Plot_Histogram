import numpy as np
import csv
import matplotlib.pyplot as plt
import glob
import os
import random
import cgi
import MySQLdb
import sys
import math
from collections import defaultdict
binwidth = 1
list1=[]
sortedlist = []
actualfrequence =[]
list2 = []
list3=[]
list4=[]

db = MySQLdb.connect(host="localhost",  user="root", passwd="root", db="database")

cur = db.cursor()
cur.execute("DROP TABLE IF EXISTS alldata")

path1 = "C:/xampp/htdocs/PHP/"+ sys.argv[1] + '/'
path = 'C:/xampp/htdocs/PHP/uploads/'
os.chdir(path1)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
oldest = files[0]
newest = files[-1]

with open(newest) as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        list1.append(row)
        list3.append(row[0])
y = len(list3)
list2 = list1[0]
for i in list2:
    k=i.replace('#','No')
    j=k.translate(None, ' -.:@/(%)')
    list4.append(j)
print list4
sql = "CREATE TABLE alldata("+list4[0]+" NVARCHAR(45));"
cur.execute(sql)
m = 1

while(m<len(list2)):
    k = "ALTER TABLE alldata ADD " + list4[m] + " NVARCHAR(45)"
    cur.execute(k)
    m = m + 1
s = 1
if len(list2)>1:
    while(s!=len(list1)):
        cur.execute("INSERT INTO alldata VALUES %r;" % (tuple(list1[s]),))
        s=s+1
    db.commit()

else:
    c = "INSERT INTO alldata ("+ list4[0] + ") VALUES (%s)"

    while (s != len(list1)):
        cur.execute(c,list1[s])
        s = s + 1
    db.commit()

z = 0
i = 0
j=0
n=0
list6=[]
actualfrequence=[]
notanumber = False

while(z<len(list2)):
    notanumber = False
    sql1 = "SELECT " + list4[z] + " FROM alldata"
    cur.execute(sql1)
    data = cur.fetchall()
    # print data
    data = [i[0] for i in data]
    data = filter(None, data)
    # print data
    if not data:
        print "no data available in this column"
    else:
        for value in data:
            try:
                fvalue = float(value)
                list6.append(fvalue)
            except ValueError:
                notanumber = True
                break
        if(notanumber == False):
            mini = int(math.floor(min(list6)))
            maxi = int(math.ceil(max(list6)))
            sortedlist = sorted(list6)
            length = (len(sortedlist))
            print list2[z]
            print length
            if(length!=1):
                i = 1 / float(length)
                j = 1 / float(length) + i
                actualfrequence.insert(0, i)
                actualfrequence.insert(1, j)
                while (length != 2):
                    n = i + j
                    j = n
                    actualfrequence.append(n)
                    length = length - 1
                plt.figure(figsize=(6, 5))
                plt.hist(list6, bins=range(mini, maxi + binwidth, binwidth))
                plt.xlabel(str(list2[z]))
                plt.ylabel("BINS")
                plt.twinx()
                plt.ylabel("actual frequency", color="r")
                plt.tick_params(axis="y", labelcolor="r")
                plt.scatter(sortedlist, actualfrequence, color="y")
                plt.plot(sortedlist, actualfrequence, "r-", linewidth=2)
                filename = os.path.join(path1, str(z))

                del actualfrequence[:]

                # plt.show()
                plt.savefig(filename)
                plt.clf()
            else:
                print "one num"
                i = 1 / float(length)
                plt.figure(figsize=(6,5))
                plt.hist(list6, bins=range(mini, maxi + binwidth, binwidth))
                plt.xlabel(str(list2[z]))
                plt.ylabel("BINS")
                plt.twinx()
                plt.ylabel("actual frequency", color="r")
                plt.tick_params(axis="y", labelcolor="r")
                plt.scatter(sortedlist, i, color="y")
                plt.plot(sortedlist, i, "r-", linewidth=2)
                filename = os.path.join(path1, str(z))
                plt.savefig(filename)
                plt.clf()
            del list6[:]
            del sortedlist[:]



    z=z+1




































    # z = 0
# g = 0
# list6=[]
# notanumber = False
# # plt.savefig(kurs, format='png')
# while(z<len(list2)):
#     notanumber = False
#     sql1 = "SELECT " + list4[z] + " FROM alldata"
#     cur.execute(sql1)
#
#     data = cur.fetchall()
#     data = [i[0] for i in data]
#     data = filter(None, data)
#     if not data:
#         print "no data available in this column"
#     else:
#         for value in data:
#             try:
#                 fvalue = float(value)
#                 list6.append(fvalue)
#             except ValueError:
#                 notanumber = True
#                 break
#         if (notanumber == False):
#             #print list6
#             mini = int(math.floor(min(list6)))
#             #print mini
#             maxi = int(math.ceil(max(list6)))
#             #print maxi
#             plt.hist(list6, bins=range(mini, maxi + binwidth, binwidth))
#             plt.xlabel(str(list2[z]))
#             plt.ylabel("BINS")
#             filename = os.path.join(path1, str(z))
#             plt.show()
#             # plt.savefig(filename)
#             plt.clf()
#             del list6[:]
#     z = z + 1
    # data1 = map(float, data)
    # data = map(int, data1)
    # if not data:
    #     print ("no data available in this column")
    # else:
    #     plt.hist(data1, bins=range(min(data), max(data) + binwidth, binwidth))
    #     plt.xlabel(str(list2[z]))
    #     plt.ylabel("BINS")
    #     filename = os.path.join(path1, str(z))
    #     plt.savefig(filename)
    #     plt.clf()
    # z = z + 1


# sortedlist=sorted(list1)
# #print(sortedlist)
# length = (len(sortedlist))
#
# i = 1/length
#
# j = 1/length+i
# while (length!=1):
#     n=i+j
#     j = n
#     actualfrequence.append(n)
#     length = length-1;
#
# actualfrequence.insert(0,i)
# #print(actualfrequence)
# plt.scatter(sortedlist,actualfrequence,color='c')
# plt.plot(sortedlist,actualfrequence)
# plt.hist(list1, bins, histtype='bar', rwidth=0.8)
#
# print(sys.exc_info())
# #os.chdir(path1)
#
# #n=random.random()
# #print(n)
# #m=os.mkdir(str(n))
#
#
# plt.xlabel("WEIGHT")
# plt.ylabel("ACTUAL FREQUENCY %")
# plt.savefig(path1)