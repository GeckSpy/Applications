import random as rd


path_data_base = "words/BDD.txt"
class Game:
    def __init__(self, nb_words):
        f = open(path_data_base, "r")
        bdd_words = []
        for lignes in f:
            l = lignes[:-1]
            bdd_words.append(l)
        f.close()
        print("Nombre de mots dans la base de donée :", len(bdd_words))

        self.nb_words = nb_words
        rd.shuffle(bdd_words)
        self.words = bdd_words[:nb_words]
        self.todo = []


nb_words = int(input("Combien de mots ?:"))
game = Game(nb_words)

for i in range(3):
    print("Manche numéro", i+1, ":\n")
    game.todo = [x for x in game.words]
    rd.shuffle(game.todo)
    while(game.todo != []):
        w = game.todo[0]
        line = '['+ str(len(game.todo)) + '] ' + w
        print(line)
        ip = input()
        if ip =='':
            game.todo.append(w)
        del game.todo[0]
        print('\n'*10)
    