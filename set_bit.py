n = int(input("num : "))
i = int(input("set : "))
bin_val = str(bin(n)).lstrip('0b')
if(bin_val[-i] == '1'):
    print("SET")
else:
    print("UN SET")
print("BINARY : ",bin_val)