Address = input("Enter an IP address: ")
Array = Address.split(".")
Values = [int(i) for i in Array]
print("Network ID: {0:d}, {1:d} and {2:d}".format(Values[0], Values[1], Values[2]))
print("Host ID: {0:d}".format(Values[3]))