import sys
from sys import stdout
from time import sleep

a = [0,1,1,2,3]
b = [5,6,7,8,9]
c = ['g','y','j','t','t']

d = []


d.append(a)
d.append(b)
d.append(c)
for i in range(1,5):
    stdout.write("\r%d" % i)
    stdout.flush()
    sleep(1)
stdout.write("\n")
for j in range(1,5):
    stdout.write("\r%d" % j)
    stdout.flush()
    sleep(1)
stdout.write("\n")

for k in range(1,5):
    stdout.write("\r%d" % k)
    stdout.flush()
    sleep(1)
stdout.write("\n")