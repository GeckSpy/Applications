from os import walk
  
folder_path = "BDD" #(format:) nb_shots|blablabla $A$ blabla $B$ blabla
BDD_py_path = "BDD_py.txt" #(format:list of dic) {cat:"cat1", shots:shots1, text: "text1"}, ...,
past_file = open(BDD_py_path, "w")


for (dirpath, dirnames, filenames) in walk(folder_path):
    for file_path in filenames:
        file = open(folder_path + '/' + file_path, "r")
        for lignes in file:
            l = lignes.split('|')
            sentence = "{'cat':'" + file_path[:-4] + "', 'shots':" + l[0] + ", 'text':'" +l[1] + "'}, "
            past_file.write(sentence)
        file.close()

past_file.close()