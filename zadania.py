# import datetime

# now = datetime.datetime.now()
# print("current date and time")
# print(now.strftime("%Y-%m-%d-%H:%M:%S"))


# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# fname = input("Input your First Name : ")
# lname = input("Input your Last Name : ")
# print ("Hello  " + lname + " " + fname)

# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)



# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])

# exam_st_date = (11,12,2014)
# print( "The examination will start from : %i / %i / %i"%exam_st_date)

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
