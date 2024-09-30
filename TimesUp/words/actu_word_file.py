path_file = "General/humain.txt"

f = open(path_file, "r")
l = []
for lignes in f:
    nl = lignes.split(", ")
    for i in nl:
        l.append(i)
f.close()
l.sort()
print(l)
f = open(path_file, "w")
for i in l:
    if i != '\n':
        f.write(i)
        if i[-1]!='\n':
            f.write('\n')
f.close()
