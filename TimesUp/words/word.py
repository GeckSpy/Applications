from os import walk

liste_folder = ["Celebrity", "Fiction", "General"]

words = []
for folder in liste_folder:
    for (dirpath, dirnames, filenames) in walk(folder):
        for file in filenames:
            path = folder + '/' + file
            print(path)

            f = open(path, "r")
            l = []
            for lignes in f:
                l.append(lignes)
            f.close()
            l.sort()
            f = open(path, "w")
            for i in l:
                if i != '\n':
                    f.write(i)
                    if i[-1]!='\n':
                        f.write('\n')
            f.close()

            f = open(path, 'r')
            for lignes in f:
                words.append(lignes)
            f.close()


path_data_base = "BDD.txt"
f = open(path_data_base, "w")
words.sort()
for w in words:
    print(w, end='')
    f.write(w)
f.close()
print('\n', 'nombre de mots:', len(words))