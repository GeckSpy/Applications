from os import walk

folder_path = "BDD" #(format:) nb_shots|blablabla $A$ blabla $B$ blabla
BDD_py_path = "BDD_py.txt" #(format:list of dic) {cat:"cat1", shots:shots1, text: "text1"}, ...,
past_file = open(BDD_py_path, "w")


for (dirpath, dirnames, filenames) in walk(folder_path):
    for file_path in filenames:
        file = open(folder_path + '/' + file_path, "r")
        for lignes in file:
            l = lignes.replace("'", "$g$").split('|')
            sentence = "{'cat':'" + file_path[:-4] + "','type':'" + l[0] + "', 'shots':" + l[1] + ", 'text':'" +l[2][:-1] + "'}, "
            print(sentence)
            past_file.write(sentence)
        file.close()

past_file.close()