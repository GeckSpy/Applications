from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.behaviors import BackgroundColorBehavior, CommonElevationBehavior, RectangularRippleBehavior
from kivymd.uix.widget import MDWidget
from kivymd.uix.label import MDLabel

import random as rd

global nb_words
nb_words = 30
global time_per_round
time_per_round = 30
global id_round
id_round = 1
global time_left
time_left = time_per_round
global bdd_words
bdd_words = ["2048", "AC/DC", "Abeille", "Aboyer", "Abricot", "Acteur", "Acteur porno", "Adamaï", "Adolf Hitler", "Adèle Exarchopoulos", "Agar.io", "Agenda", "Agent immobilier", "Agriculteur", "Ail", "Aladin", "Albert Einstein", "Albus Dumbledore", "Alfred Hitchcock", "Alice au pays des merveilles", "Aline dessine", "All Might", "Allumer un feu", "Allumette", "Alpinisme", "Amazon", "Amin", "AmineMaTue", "Amixem", "Amlia Sheram Sharm", "Ampoule", "Amputer", "Amy Winehouse", "Ananas", "Andy Raconte", "Ange", "Angelo la débrouille", "Angry birds", "Angèle", "Ankylosaure", "Anneau", "Ant-Man", "Antoine ", "Anus", "Aphrodite", "Appareil photo", "Aquaman", "Aragorn", "Araignée", "Arbre", "Architecte", "Archéologue", "Ares", "Arrosoir", "Arsen Lupin", "Arthus", "Aspirateur", "Assassin Creed", "Assenceur", "Assiette", "Asteorïde", "Astérix & Obélix", "Athlérisme", "Attache", "Attraper", "Autruche", "Avatar", "Avion", "Aviron", "Avocat", "Avoir mal", "BTS", "Bac à sable", "Badminton", "Baghera Jones", "Bague", "Baguette", "Baignoire", "Baiser", "Balance", "Balancoir", "Baldur's Gate", "Balrog", "Bander", "Banque", "Banquise", "Barbe", "Barman", "Barrack Obama", "Baseball", "Basket", "Bateau", "Batman", "Bazooka", "Ben Ten", "Berger", "Beyblade", "Biche", "Big Bang theory", "Big Mom", "Bilbon Sacquet", "Bill Gates", "Billie Eillish", "Bison", "Black Panther", "Black Widow", "BlackPink", "Blanche neige", "Bob Marley", "Bob l'éponge", "Bodrier", "Boire", "Boom Beach", "Borderlands", "Botte", "Boucher", "Boucle d'oreille", "Bouclier", "Bougie", "Boulanger", "Bouteille", "Bowling", "Bowser", "Boxe", "Brad Pitt", "Brawl stars", "Brawlhalla", "Breaking Bad", "Briquet", "Britney Spears", "Brocoli", "Brosse à dents", "Bubble Tea", "Bucky Barns", "Buisson", "Bulbizare", "BumbleBee", "Burrito", "Buzz l'éclair", "Bûcheron", "Cable", "Cactus", "Cadreur", "Cafard", "Cafetière", "Cahier", "Caissière", "Call of Duty", "Calvin Harris", "Caméléon", "Caméra", "Canapé", "Canard", "Candy Crush", "Cantine", "Captain America", "Captain Marvel", "Cardiologue", "Carnage", "Carnet", "Carrelage", "Cars", "Casserole", "Catch", "Cave", "Cendrillion", "Cerise", "Chaise", "Chambre", "Chameau", "Changer une couche", "Chanter", "Chanteur", "Chanteur d’opéra", "Charlie Chaplin", "Chasles", "Chat", "Chauve", "Chauve souris", "Chercheur", "Cheveux", "Chien", "Chier", "Chips", "Chirurgien", "Chris Evans", "Chris Pratt", "Christophe Colombe", "Christopher Nolan", "Chuchoter", "Cigarette", "Citron", "Clash Royal", "Clash of Clan", "Clavier", "Cloche", "Clown", "Clown", "Coccinelle", "Coco", "Cocovoit (Sympa Cool)", "Code Yoko", "Coffre", "Coiffeur", "Colier", "Colle", "Coluche", "Commicieriat", "Comptable", "Congélateur", "Corde", "Corde à sauter", "Corneil & Berni", "Cornichon", "Couette", "Couloir", "Courir", "Cours de Récréation", "Coussin", "Couteau", "Crabe", "Cravate", "Creeper", "Crier", "Crossy Road", "Crâne", "Cuillère", "Cuisine", "Cuisinier", "Curling", "Cyberpunk", "Cyclope", "Cyprien", "Cyprine", "Daenerys", "Damso", "Danse", "Danseuse", "Dark Souls", "Dark Vador", "Dauphin", "David Guetta", "Deadpool", "Dealer", "Dentier", "Dentifrice", "Dentiste", "Dents", "Desert", "Designer", "Dessiner", "Diable", "Diego", "Dindon", "Dio Brando", "Dobby", "Doctor House", "Doctor Strange", "Doctor Who", "Doigby", "Doight", "Donald Duck", "Donald Trump", "Donut", "Doodle Jump", "Dora l'exploratrice", "Dori", "Dormir", "Douche", "Doudou", "Dracula", "Dragon", "Draps", "Druide", "DysneyLand", "Démon", "Déménageur", "Déodorant", "Détective", "Eau", "Echarpe", "Echecs", "Ecole", "Ejaculer", "Elden Ring", "Eleven", "Elf", "Elon Musk", "Embrasser", "Eminem", "Emma Bovary", "Emma Stone", "Emmanuel Macron", "Encanto", "EnjoyPhoenix", "Enveloppe", "Epic Games", "Epinard", "Equitation", "Eren Jäger", "Eric Zemmour", "Escalade", "Escalator", "Escalier", "Escargot", "Escorte", "Escrime", "Esport", "Eternuer", "Etre anorexie", "Etre en retard", "Etre etonné", "Etre gros", "Etre maigre", "Etre malade", "Etre obése", "Etre stressé", "Evangelyne de Percedal", "Eve", "Evoli", "Extraterrestre", "FIFA", "Facebook", "Facteur", "Factorio", "Faire la vaisselle", "Faire ses devoirs", "Faire un 69", "Faire un badtrip", "Faire un bisous", "Faire un câlin", "Faire une caresse", "Faire une overdose", "Faisan", "Family Guys", "Fantôme", "Faucon", "Fauteuil", "Fer à repasser", "Flamant Rose", "Flappy birds", "Flash Mcqueen", "Fleuriste", "Foot", "Foot de rue", "Formule 1", "Fortnite", "Forêt", "Fourche", "Fourchette", "Fourmi", "Francois Civil", "Francois Holland", "Freezer", "Frida Kalo", "Friends", "Frodon Sacquet", "Fromage", "Fueille", "Fumer", "Fumer un joint", "Fusi", "Fusée", "Fée", "Félix Lebrun", "Gad Elmaleh", "Game of Thrones", "Gandalf", "Garagiste", "Garde forestier", "Gaston Lagaffe", "Gate", "Gaëlle Garcia Diaz", "Genos", "Geometry Dash", "Gimly", "Girafe", "Glace", "Glaçon", "Glaçon", "Gobelin", "God", "Godzilla", "Golem", "Golf", "Gollum", "Google", "Gorillaz", "Gotaga", "Goultard", "Goélan", "Greg Guillotin", "Grenade", "Grenier", "Grenouille", "Grey's anatomy", "Grinder", "Grotte", "Grutier", "Gundam", "Gymnastique", "Géant", "Gémir", "Générale de Gaule", "Géologue", "Hache", "Hades", "Hamburger", "Hamster", "Handball", "Harry Potter", "Hawkeye", "Hella", "Hera", "Hermione Granger", "Hibou", "Hipopotam", "Hippocampe", "Hockey", "Hodor", "Hopital", "Horizon zeor Dawn", "Horloge", "Hot-Dog", "Hotesse de l'air", "How I met your mother", "Hulk", "Hyène", "Ichigo Kurosaki", "Illustrateur", "Imprimante", "Infirmière", "Informaticien", "Inoxtag", "Instagram", "Iron Man", "It", "Izuku Midoriya", "Jack Sparrow", "Jack l'eventreur", "Jardin", "Jardinier", "Jasmin", "Javelot", "Jean-Luc Melanchon", "Jennifer Lawrence", "Jetpack Joyride", "Jhonny Depp", "Jhonny Halliday", "Jimbe", "Jimmy fait le con", "Jinx", "Joaquin Phoenix", "Joe Biden", "Join", "Jon Snow", "Jongler", "Joseph Staline", "Jotaro Kujo", "Jouer", "Jouet", "Joueur Du Grenier", "Jouir", "Journaliste", "Joyca", "Jul", "Junkrat", "Jupe", "Jupiter", "Kaido", "Kakashi Hatake", "Kameto", "Kangourou", "Karting", "Kastuki Bakugo", "Katniss Everdeen", "Kebabier", "Ketchup", "Kim Jong Un", "KingKong", "Kirito", "Kiwi", "Koala", "Kung Fu Panda", "L'exorciste", "L'âne Trotro", "La Faucheuse", "La Joconde", "La Terre", "La belle au boit dormant", "La belle et la bête", "La colére", "La depression", "La famille pirate", "La haine", "La joie", "La petite Sirene", "La petite souris", "La planéte des singes", "La princesse et la grenouille", "La reine d'Angleterre", "La reine des neiges", "Lac", "Laink & Terracid", "Laisse", "Lama", "Lampe", "Lancer de Javelot", "Lanfeust de Troy", "Lapin", "Lara Croft", "Lavabo", "Lavande", "Lave-linge", "Le Rire Jaune", "Le Soleil", "Le chat Botté", "Le chateau ambulant", "Le chateau dans le ciel", "Le compte de Monte-Cristo", "Le croque mitaine", "Le lapin de Paques", "Le marchant de sable", "Le monde de Narnia", "Le mont Everest", "Le père Noël", "Le père fouettard", "Le voyage de Chihiro", "League of Legend", "Lebron James", "Led Zeppelin", "Legolas", "Lena Situation", "Leonardo DiCaprio", "Les 4 Fantastiques", "Les 5 légendes", "Les Avengers", "Les Gardiens de la Galaxie", "Les Indestructibles", "Les LooneyToons", "Les Légendaires", "Les Noces Funébres", "Les Ratz", "Les Schtroumpfs", "Les Simpsons", "Les Tortues Ninjas", "Les Totally Spies", "Les chevaliers du Zodiac", "Les minis justiciers", "Les zinzins de l'espace", "Libellule", "Libraire", "Lil Nas X", "Lillix", "Limace", "Lion", "Lionel Messy", "Lit", "Livaï Ackerman", "Livreur de pizza", "Locklear", "Louis Vuitton", "Loup-Garou", "Loutre", "Lubrifiant", "Lucifer", "Lucky Luke", "Luigi", "Lunettes", "Lutte", "Léon Marchand", "M&M's", "MMA", "Macaron", "Macfly & Carlito", "Madagascar", "Magicien", "Maglha", "Manger", "Manny", "Marathon", "Marcher", "Marine Lepen", "Marine Tondelier", "Mario", "Mario Kart", "Marionnettiste", "Marmotte", "Marque-page", "Martin", "Martin Luher King", "Martin Mystères", "Martin Scorsese", "Mashmallow", "Massacre à la tronçonneuse", "Mastu", "Math se fait des films", "Mayonnaise", "Maçon", "Maître-nageur", "Maï Thaï", "Medezeanine", "Medusa", "Menottes", "Mer", "Mercy", "Mesenger", "Metallica", "Metamorphe", "Meteorite", "Meuble", "Miaouss", "Michael Angelo", "Michael Jackson ", "Michou", "Mickey Mouse", "Miles Morales", "Mille-pattes", "Mimi Mathy", "Minecraft", "Minotaure", "Miraculous", "Mirroir", "Mister V", "Mohamed Ali", "Mokey D. Luffy", "Momie", "Mon voisin Totoro", "Moniteur de ski", "Montagne", "Montre", "Mordre", "Morgan Freeman", "Morse", "Mort-vivants", "Motocross", "Mouche", "Mouchoir", "Mouiller", "Moustache", "Moustique", "Moutarde", "Mouton", "Mr Bean", "Mr Beast", "Mufassa", "Musculation", "My talking Tom", "Mâcher un chewing-gum", "Mécanicien", "Médecin", "Mégalodon", "Nager", "Nain", "Nappe", "Naruto Uzumaki", "Nastu Dragnir", "Natation", "Nathalie Portman", "Natoo", "Nausicaä la Vallée du Vent", "Nelson Mandela", "Nemo", "Newt (Le Labyrinthe)", "Nicolas Sarcozy", "Nicolas Tesla", "Ninja", "Nirvana", "Nombril", "Nombrille", "Norman", "Nouilles", "Océan", "Oeuf", "Office du tourisme", "Oggy et les cafards", "Ogre", "Oignon", "One Punch Man", "Opticien", "Optimus Prime", "Orange", "Ordinateur", "Oreiller", "Orelsan", "Organisateur", "Orthophoniste", "Oui-Oui", "Overwatch", "PUBG", "Pablo Escobar", "Pablo Picasso", "PacMan", "Pacific Rim", "Pain", "Palmashow", "Palmier", "Pamplemouse", "Panda", "Pantalon", "Paon", "Papillon", "Parachutisme", "Parapluie", "Parc", "Parc Aquatique", "Parc d'attraction", "Paresseux", "Parkour", "Parler", "Passage piéton", "Passer l'aspirateur", "Passoire", "Pate", "Patin à roulette", "Pattinage", "Paul Mirabel", "Peach", "Peindre", "Peintre", "Peluche", "Penis", "Peppa Pig", "Pesto", "Peter Pan", "Petit Biscuit", "Pewdipie", "Pharmacien", "Phoque", "Photographe", "Piano", "Pick Pocket", "Pierre Niney", "Pieuvre", "Pigeon", "Pikachu", "Pilote d’avion", "Pince", "Ping-Pong", "Pingouin", "Pinterest", "Piou Piou", "Pipe", "Piranha", "Pirates des Caraïbes", "Piscine", "Pisser", "Pistolet", "Pizza", "Placard", "Plage", "Planche à découper", "Planche à voile", "PlayStore", "Pleurer", "Plombier", "Plonger", "Plongée", "Po (Kung Fu Panda)", "Pocahontas", "Poil", "Poisson", "Pokemon", "Policier", "Pompier", "PornHub", "Portags D. Ace", "Portefeuille", "Poseïdon", "Poubelle", "Poule", "Poulpe", "Prendre un rail de coq", "Princesse Mononoke", "Prison", "Prison Break", "Professeur", "Prostituer", "Président", "Psycolgue", "Ptérodactyle", "Pythagor", "Péter", "Pétin", "Pêcher", "Quasimodo", "Quentin Tarantino", "Quille", "Radio", "Radis", "Raiponce", "Rallye", "Ramasser", "Ramoneur", "Ranger", "Ratata", "Rayman", "Rayquaza", "Red Dead Redemption", "Red Hot Chilli Pepper", "Regarder la télé", "Reinhardt", "Requin", "Rhinocéros", "Rick et Morty", "Rider", "Riz", "Robert Downey Jr.", "Robin", "Robinet", "Ron Weasley", "Ronald McDonald", "Roronoa Zoro", "Rose", "Roter", "Route", "Rugby", "Ryan Reynolds", "Réalisateur", "Réfléchir", "Réfrigérateur", "Sabo", "Sage-femme", "Saigner", "Sakura Haruno", "Salade", "Salaméche", "Salle de bain", "Sally", "Salon", "Sam Gamegie", "Samouraï", "Samuel Etienne", "Samuel L. Jackson", "Sangoku", "Sarah Connor", "Sarouman", "Sasuke Uchiwa", "Satan", "Saturne", "Saturo Gojo", "Saucisse", "Sauron", "Saut en hauteur", "Saut en longueur", "Saut à la perche", "Sauter à la corde", "Scarabée", "Scarlett Johansson", "Schrek", "Scorpion", "Scotch", "Scrat", "Sculpter", "Se baigner", "Se battre", "Se cacher", "Se confeser", "Se masturber", "Se moucher", "Se noyer", "Se promener", "Seb LaFrite", "Selena Gomez", "Sentaure", "Serpent", "Serrurier", "Serveur", "Seuls", "Sex-Toys", "Shang-Chi", "Shera", "Sherlock Holmes", "Sid", "Simba", "Singe", "Sirène", "Ski", "Skrillex", "Skyrim", "Slenderman", "Smash Bros", "Snapchat", "Snowboard", "Société Radio-Canada", "Sofyan", "Sonic", "Sorcière", "Soucoupe vollante", "Sourire", "Souris", "Souris", "Sperm", "Spider-Man", "Spider-Man New Generation", "Spinosaure", "Spirou", "Spéléologie", "Squeezie", "Squelette", "Steam", "Steve Jobs", "Steven Spielberg", "Stranger Things", "Street Fighter", "Stromae", "Stupeflip", "Styliste", "Stylo", "Subway Surfer", "Succube", "Sucer", "Superman", "Surf", "Suriken School", "Surligneur", "Sushi", "Sèche-cheveux", "THomas Edison", "Table", "Tacos", "Taikwendo", "Tapis", "Tasse", "Taupe", "Taxi", "Taylor Swift", "Technicien", "Teddy Riner", "Tekken", "Temple Run", "Tennis de table", "Terminator", "Tetris", "Thalès", "The 100", "The Beatles", "The witcher", "Thomas et ses amis", "Thon", "Thor", "Tibo in shape", "Tigre", "Timmy Trumpet", "Tinder", "Tintin", "Tiploufe", "Tire à l’arc", "Tirelire", "Tirer la langue", "Toad", "Tobogant", "Toiletteur", "Toillet", "Tom Hardy", "Tom Holland", "Tom-Tom & Nana", "Tomate", "Tortue", "Toys Story", "Tracer", "Trackmania", "Traducteur", "Train", "Traire une vache", "Transpirer", "Travailler", "Traversin", "Triathlon", "Tristepin de Percedal", "Trotinette", "Trottoir", "Trousse", "Twilight", "Twitter", "Tyrannosaure", "Télécommande", "Téléphone", "Téléphoner", "Têtard", "Uber", "Ultimate", "Ultron", "Un monstre à Paris", "Undertale", "Until Dawn", "Urologue", "Usain Bolt", "Valerian", "Vampire", "Vapoter", "Vegeta", "Vendeur", "Vendredi 13", "Venom", "Ventilateur", "Verre", "Vi", "Vickings", "Vigile", "Ville", "Vinsumōku Sanji", "Vinyle", "Vladimir Poutine", "Voiture", "Voldemort", "Volley Ball", "Vomir", "Vélo", "Vétérinaire", "Wagon", "Walibi", "Wall-E", "Walt Disney", "Walter White", "Waluigi", "Wanski", "War Machine", "Wario", "Whatsapp", "Widow Maker", "Wii Sports", "Winnie l'ourson", "Wolverine", "Wonder Woman", "Woody", "Woody Woodpecker", "World of Warcraft", "Xavier Niel", "Yoshi", "YouPorn", "Youtube", "Yugo", "Yuji Itadori", "Yéti", "Zelda", "Zerator", "Zeus", "Zinedine Zidane", "Zombie", "Zombie stunami", "Zoo", "Zumba", "Zèbre", "Éboueur", "Écouter de la musique", "Écran", "Écureuil", "Élécticien", "Éléphant", "Éplucher des légumes", "Épée", "Étendre du linge", "Étoile de mer", "Éventail", "Être Heureux", "Être addict", "Être alcoolisé", "Être bourré", "Être drogué", "Être pauvre", "Être riche", "Être triste"]


global words
global words_todo
words = []
words_todo = []

KV = '''
ScreenManager:
    MenuScreen:
    GameScreen:
    WaitingScreen:
    RoundScreen1:
    RoundScreen2:

<MenuScreen>:
    id: menu_screen
    name: 'menu'

    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .2,.2,.2
    
    MDCard:
        size_hint: 1, 0.15
        pos_hint: {'center_x':0.5, 'center_y':0.925}
        radius: 0
        md_bg_color: .2,.6,1
        elevation: 2
        shadow_offset: (0, -2)

    MDLabel:
        text: "Time's Up - M.O.'s version"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.925}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "30sp"

    MDLabel:
        id: label_number_of_cards
        text: root.content_label_number_of_cards
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.775}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "30sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint: 0.9,0.3
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_release:
            app.InitGame(slider_cards.value)
            root.manager.transition.direction = 'left'
            root.manager.current = 'round1'
    
    MDLabel:
        text: "Play"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
        
    MDCard:
        size_hint: 0.9, 0.15
        pos_hint: {'center_x':0.5, 'center_y':0.125}
        elevation: 1
        shadow_offset: (2, -2)

    MDLabel:
        text: "Number of cards"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.15}
        theme_text_color: "Custom"
        text_color: "black"

    MDSlider:
        id: slider_cards
        thumb_color_active: "red"
        thumb_color_inactive: "red"
        size_hint: 0.8,0.5
        pos_hint: {'center_x':0.5, 'center_y':0.1}
        step: 1
        min: 0
        max: 150
        value: 40

        
<RoundScreen1>:
    name: 'round1'
    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .1,.1,.1

    MDCard:
        size_hint: .85, .85
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 10
        md_bg_color: .2,.2,.2

    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'left':1, 'top':1}
        on_release:
            root.manager.transition.direction = 'right'
            root.manager.current = 'menu'

    ElevatedWidget:
        pos_hint: {'center_x':0.5, 'center_y':0.17}
        size_hint: 0.97,0.3
        elevation: 2
        radius: 18
        shadow_offset: (2,-2)
        md_bg_color: .2,.6,1
        on_release: 
            app.StartGame(slider_time.value)
            root.manager.current = 'game'

    MDLabel:
        text: "Start"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.15}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "40sp"
    
    MDLabel:
        text: "Number of times :"
        theme_text_color: "Custom"
        text_color: "white"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.55}

    MDSlider:
        id: slider_time
        thumb_color_active: "red"
        thumb_color_inactive: "red"
        size_hint: 0.8,0.5
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        step: 5
        min: 5
        max: 90
        value: 30

    MDLabel:
        text: "First round :"
        theme_text_color: "Custom"
        text_color: "white"
        halign: "center"
        font_size: "30sp"
        pos_hint: {'center_x':0.5, 'center_y':0.8}

    MDLabel:
        text: "Describe your word !"
        theme_text_color: "Custom"
        text_color: "white"
        halign: "center"
        font_size: "30sp"
        pos_hint: {'center_x':0.5, 'center_y':0.7}

        
<WaitingScreen>:
    id: waiting_screen
    name: 'waiting'
    on_enter: root.actu()

    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .1,.1,.1
    
    MDCard:
        size_hint: .85, .85
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 10
        md_bg_color: .2,.2,.2

    ElevatedWidget:
        pos_hint: {'center_x':0.5, 'center_y':0.17}
        size_hint: 0.97,0.3
        elevation: 2
        radius: 18
        shadow_offset: (2,-2)
        md_bg_color: .2,.6,1
        on_release:
            root.manager.current = 'game'

    MDLabel:
        text: "Ready ?"
        theme_text_color: "Custom"
        text_color: "white"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.17}
        font_size: "40sp"
    
    Label:
        id: label_time_per_round
        text: "You will have x second"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.85}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "30sp"

        
<RoundScreen2>:
    name: 'round2'
    on_enter: root.actu()
    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .1,.1,.1
    
    MDCard:
        size_hint: .85, .85
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 10
        md_bg_color: .2,.2,.2

    MDLabel:
        id: round_label_sentence1
        text: "Round n°"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "40sp"

    MDLabel:
        id: round_label_sentence2
        text: "Sentence"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "30sp"

    ElevatedWidget:
        text: "Start"
        pos_hint: {'center_x':0.5, 'center_y':0.17}
        size_hint: 0.97,0.3
        elevation: 2
        radius: 18
        shadow_offset: (2,-2)
        md_bg_color: .2,.6,1
        on_release: 
            app.InitRound()
            root.manager.current = 'game'
    
    MDLabel:
        text: "Start"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.15}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "40sp"


<GameScreen>:
    id: game_screen
    name: 'game'
    on_enter:
        root.actu()
        root.start()
    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .1,.1,.1
    
    MDCard:
        size_hint: .85, .85
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 10
        md_bg_color: .2,.2,.2

    ElevatedWidget:
        text: "Pass"
        pos_hint: {'center_x':0.75, 'center_y':0.17}
        size_hint: 0.47,0.3
        elevation: 2
        radius: 18
        shadow_offset: (2,-2)
        md_bg_color: 1,.5,0
        on_press: root.passed()
    
    ElevatedWidget:
        text: "Guessed"
        pos_hint: {'center_x':0.25, 'center_y':0.17}
        size_hint: 0.47,0.3
        elevation: 2
        radius: 18
        shadow_offset: (2,-2)
        md_bg_color: .4,.8,0
        on_press: root.guessed()

    Label:
        text: "Guessed"
        pos_hint: {"x":0.2, "y":0.13}
        size_hint: 0.1,0.1
        font_size: "40sp"

    Label:
        text: "Pass"
        pos_hint: {"x":0.7, "y":0.13}
        size_hint: 0.1,0.1
        font_size: "40sp"

    MDCard:
        size_hint: .7, .25
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        radius: 10
        md_bg_color: .3,.3,.3    
        elevation: 4

    MDLabel:
        id: game_word
        text: root.content_game_word
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"

    MDLabel:
        id: number_of_todo_card
        text: "0"
        halign: 'center'
        pos_hint: {'center_x':0.5, 'center_y':0.37}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "30sp"

    MDSpinner:
        id: timer_spinner
        size_hint: 0.15,0.15
        size: dp(47), dp(47)
        color: .2,.6,1
        pos_hint: {'center_x': .5, 'center_y': .83}
        active: True
        line_width: dp(3)

    MDLabel:
        id: temps_restant
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.83}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "30sp"
'''


class ElevatedWidget(CommonElevationBehavior, RectangularRippleBehavior,
    ButtonBehavior, MDWidget):
    _elev = 0  # previous elevation value

    def on_press(self, *args):
        if not self._elev:
            self._elev = self.elevation
        Animation(elevation=self.elevation + 2, d=0.4).start(self)

    def on_release(self, *args):
        Animation.cancel_all(self, "elevation")
        Animation(elevation=self._elev, d=0.1).start(self)



class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global bdd_words
        self.content_label_number_of_cards = str(len(bdd_words)) + " words"

class RoundScreen1(Screen):
    pass

class RoundScreen2(Screen):
    def actu(self):
        global id_round
        sentence1 = ''
        sentence2 = ''
        if id_round == 2:
            sentence1 = "Second Round :"
            sentence2 = "Says only one word !"
        elif id_round == 3:
            sentence1 = "Third Round :"
            sentence2 = "Mimic the word !"
        self.ids.round_label_sentence1.text = sentence1
        self.ids.round_label_sentence2.text = sentence2


class WaitingScreen(Screen):
    def actu(self):
        global time_per_round
        self.ids.label_time_per_round.text = "You will have " + str(time_per_round) + " seconds"


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global words_todo
        self.content_game_word = 'NON'
    
    def actu(self):
        global words_todo
        self.ids.number_of_todo_card.text = str(len(words_todo))
        if(len(words_todo) != 0):
            self.ids.game_word.text = words_todo[0]
        else:
            global id_round
            id_round += 1
            if(id_round <= 3):
                self.manager.transition.animation = 'left'
                self.manager.current = "round2"
            else:
                self.manager.transition.animation = 'right'
                self.manager.current = "menu"
        global time_per_round

    def passed(self):
        global words_todo
        w = words_todo[0]
        words_todo.append(w)
        del words_todo[0]
        self.actu()

    def guessed(self):
        global words_todo
        del words_todo[0]
        self.actu()

    def start(self):
        global time_left
        global time_per_round
        time_left = time_per_round +1 

        def decrease_timer(dt):
            global time_left
            if time_left > 0:
                time_left = time_left - 1
                self.ids.temps_restant.text = str(time_left)
                Clock.schedule_once(decrease_timer, 1)
            else:
                if self.manager.current == "game":
                    self.manager.current = "waiting"
                    self.passed()
        decrease_timer(1)


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GameScreen(name='game'))
sm.add_widget(WaitingScreen(name='waiting'))
sm.add_widget(RoundScreen1(name='round1'))
sm.add_widget(RoundScreen2(name='round2'))
class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen

    def InitGame(self, value):
        global nb_words
        global words
        global bdd_words
        rd.shuffle(bdd_words)
        nb_words = int(value)
        words = bdd_words[:nb_words]
        #print(words)

    def StartGame(self, value):
        global time_per_round
        time_per_round = int(value)
        #print("Time per round:", time_per_round)
        self.InitRound()

    def InitRound(self):
        global words_todo
        words_todo = [x for x in words]
        rd.shuffle(words_todo)
        #print(words_todo)
    
ma = MainApp()
ma.run()