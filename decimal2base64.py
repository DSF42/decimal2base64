# coding: utf-8

import base64

data_type = int(input("Input 1 or 2 as the type of string (1:Hexadecimal, 2:Decimal) -> "))
data = input("Input the string to be encoded -> ")

if data_type == 1: 
  data_int = int( data, 16 )
elif data_type == 2:
  data_int = int( data, 10 )
else:
  print("!!!!ERROR!!!!")
  exit()

if data_int > 0xffffffffffffffff or data_int < 0:
  print("!!!!ERROR!!!!")
  exit()

#convert to little-endian
data_bytes = data_int.to_bytes(8, 'little')

data_bytes_64enc = base64.b64encode(data_bytes)
str_64enc = data_bytes_64enc.decode('utf-8')

print("The encoded string is '" + str_64enc + "'")

input("press ENTER key to exit")
