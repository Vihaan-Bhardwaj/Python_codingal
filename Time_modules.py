import time

#print(time.gmtime())

tuple_time = (time.gmtime())



print(tuple_time.tm_mday,"/",tuple_time.tm_mon,"/",tuple_time.tm_year)


print("The time since the epoch is: ", tuple_time.tm_year - 1970, " years", tuple_time.tm_mon - 1, " months, and ", tuple_time.tm_mday - 1, " days")