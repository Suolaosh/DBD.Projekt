import sys
# -*- coding: UTF-8 -*-
payload=[187,254,2,9,50,55,32,54,48,32,49,57,56]
print(payload)
message =[]
for i in payload[4:13]:
    message.append(chr(i))
print message
temp   = message[0] + message[1]
hum    = message[3] + message[4]
intens = message[6] + message[7] + message[8]
print temp

# print(payload)
# for i in range(len(payload)):
#     print chr(payload[i])
