filename='c:\\temp\\output.txt'

line='Europe'

cities=['London','Berlin','Paris','Warsaw','Madrid','Rome']

file=open(filename,'w')

file.write(line)
file.write("\n")

#file.writelines(cities)

for city in cities:
    file.write(city+'\n')

file.close()
