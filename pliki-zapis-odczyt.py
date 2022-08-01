file=open("countres_capitals.txt", "w+")

countres_capitals={"Poland":"Warsaw", "Germany":"Berlin"}

for country, capital in countres_capitals.items():
    file.write(country+ "-" + capital + "\n")

file.close()

###

file=open("countres_capitals.txt")

for line in file.readlines():
    print(line.strip())

file.close()
