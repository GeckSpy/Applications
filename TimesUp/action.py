
f = open("BDD.txt", "r")
f2 = open("BDD_android.txt", "w")
liste = []
for l in f:
    f2.write('"' + l[:-1] + '", ')

