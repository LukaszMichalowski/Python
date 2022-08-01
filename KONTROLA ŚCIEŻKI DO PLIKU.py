import os

while True:

    filename=input('Enter path to results file: ')

    if os.path.isfile(filename):
        break
    else:
        print('File nam is not correct,try again!')
        

print("The result file is %s"%(filename))
