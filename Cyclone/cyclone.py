from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.behaviors import CommonElevationBehavior, RectangularRippleBehavior
from kivymd.uix.widget import MDWidget
from kivymd.uix.label import MDLabel

import random as rd

# Constantes:
nb_card = 30

class Player():
    def __init__(self, name):
        self.name = name
        self.shots = 0

    def reset(self):
        self.shots = 0

player1 = Player("J1")
player2 = Player("J2")
player_list = [player1, player2]

questions = []
BDD_card = [{'cat':'Sport','type':'_', 'shots':4, 'text':'$A$, fait 2 pompes'}, {'cat':'Sport','type':'_', 'shots':8, 'text':'$A$, fait 5 pompes'}, {'cat':'Sport','type':'_', 'shots':2, 'text':'$A$, fait 3 squats'}, {'cat':'Sport','type':'_', 'shots':3, 'text':'$A$, fait une traction'}, {'cat':'Sport','type':'g', 'shots':2, 'text':'le premier à faire 4 pompes distribue 2 gorgées'}, {'cat':'Sport','type':'g', 'shots':0, 'text':'Shifoumi: le perdant ce prend une frite'}, {'cat':'Alcool','type':'_', 'shots':1, 'text':'$A$, boit'}, {'cat':'Alcool','type':'_', 'shots':2, 'text':'$A$, boit 2 gorgées'}, {'cat':'Alcool','type':'_', 'shots':4, 'text':'$A$, boit 4 gorgées'}, {'cat':'Alcool','type':'_', 'shots':6, 'text':'$A$, fini ton verre'}, {'cat':'Alcool','type':'g', 'shots':2, 'text':'$A$, donne 2 gorgées à qui tu veux'}, {'cat':'Alcool','type':'g', 'shots':4, 'text':'$A$, donne 4 gorgées à qui tu veux'}, {'cat':'Alcool','type':'g', 'shots':1, 'text':'ShiFouMi, celui qui perd boit'}, {'cat':'Alcool','type':'_', 'shots':2, 'text':'$A$, boit une gorgée du verre de $B$'}, {'cat':'Alcool','type':'g', 'shots':1, 'text':'La derniere personne à avoir fais du sport distribue 1 gorgées'}, {'cat':'Alcool','type':'g', 'shots':2, 'text':'La derniere personne à avoir pisser sous la douche boit 2 gorgées'}, {'cat':'Alcool','type':'g', 'shots':4, 'text':'La derniere personne à avoir reagrder Wankil distribue 4 gorgées'}, {'cat':'Other','type':'_', 'shots':2, 'text':'$A$, échange de place avec $B$'}, {'cat':'Other','type':'_', 'shots':6, 'text':'$A$, tu es au ordre de $B$ pendant un tour'}, {'cat':'Other','type':'_', 'shots':2, 'text':'$A$, $B$, faites vous un calin'}, {'cat':'Other','type':'_', 'shots':6, 'text':'$A$, prends la place la plus incomfortable'}, {'cat':'Other','type':'g', 'shots':1, 'text':'$A$, raconte une anecdote vraie ou fausse, si $B$ devine correctement tu bois, sinon c$g$est $B$'}, {'cat':'Other','type':'_', 'shots':1, 'text':'$A$, donne un ordre à $B$ (dans les limites du respects)'}, {'cat':'Other','type':'_', 'shots':4, 'text':'$B$ te donne un ordre'}, {'cat':'Other','type':'_', 'shots':4, 'text':'$A$, fais un dessin (en 30 secondes)'}, {'cat':'Other','type':'_', 'shots':5, 'text':'$A$, propose une activité pour nous un jour'}, {'cat':'Other','type':'_', 'shots':4, 'text':'$A$, organise un date !'}, {'cat':'Other','type':'_', 'shots':2, 'text':'Laisse $B$ te lancer un action ou verité'}, {'cat':'Other','type':'_', 'shots':2, 'text':'Laisse $B$ te lancer un action ou verité'}, {'cat':'Other','type':'_', 'shots':2, 'text':'Laisse $B$ te lancer un action ou verité'}, {'cat':'Other','type':'_', 'shots':2, 'text':'Laisse $B$ te lancer un action ou verité'}, {'cat':'Other','type':'_', 'shots':7, 'text':'$A$, ferme les yeux pendant 2 tours et ai confiance en l$g$autre'}, {'cat':'Other','type':'_', 'shots':4, 'text':'Laisse $B$ te lancer un pour combien'}, {'cat':'Other','type':'_', 'shots':4, 'text':'Laisse $B$ te lancer un pour combien'}, {'cat':'Other','type':'_', 'shots':4, 'text':'Laisse $B$ te lancer un pour combien'}, {'cat':'Hot','type':'_', 'shots':4, 'text':'$A$, embrasse $B$'}, {'cat':'Hot','type':'_', 'shots':4, 'text':'$A$, embrasse $B$'}, {'cat':'Hot','type':'_', 'shots':2, 'text':'$A$, embrasse le coup $B$'}, {'cat':'Hot','type':'_', 'shots':1, 'text':'$A$, mordille l$g$oreille de $B$'}, {'cat':'Hot','type':'_', 'shots':3, 'text':'$A$, embrasse la nuque de $B$'}, {'cat':'Hot','type':'_', 'shots':4, 'text':'$A$, monte sur les genoux de $B$ pendant 2 tours'}, {'cat':'Hot','type':'_', 'shots':1, 'text':'$A$, fait embrasse le ventre de $B$'}, {'cat':'Hot','type':'_', 'shots':6, 'text':'$A$, fais toi léchouiller par $B$'}, {'cat':'Hot','type':'_', 'shots':5, 'text':'$A$, enlève un vetement'}, {'cat':'Hot','type':'_', 'shots':5, 'text':'$A$, enlève un vetement'}, {'cat':'Hot','type':'_', 'shots':4, 'text':'$A$, enlève ton haut'}, {'cat':'Hot','type':'_', 'shots':4, 'text':'$A$, enlève ton bas'}, {'cat':'Hot','type':'_', 'shots':6, 'text':'$A$, enlève tes sous vetements'}, {'cat':'Hot','type':'_', 'shots':8, 'text':'$B$, enlève autant de vetement que tu veux, $A$ doit en enlever autant'}, {'cat':'Hot','type':'_', 'shots':5, 'text':'$B$ choisi un vetemnt que $A$ doit enlever'}, {'cat':'Hot','type':'_', 'shots':2, 'text':'$B$ choisi un endroit que $A$ doit embrasser'}, {'cat':'Hot','type':'g', 'shots':1, 'text':'$A$, raconte une anecdote sexuel vraie ou fausse, si $B$ devine correctement tu bois, sinon c$g$est $B$'}, {'cat':'Hot','type':'_', 'shots':4, 'text':'$A$, dit nous un de tes projets pour ce soir'}, {'cat':'Hot','type':'_', 'shots':3, 'text':'$A$, lèche la joue de $B$'}, {'cat':'Hot','type':'_', 'shots':4, 'text':'$A$, fait un suçon à $B$ à l$g$endroit de son choix'}, {'cat':'Hot','type':'s', 'shots':2, 'text':'Tout ceux qui sont déjà allé dans un sex-shop boivent'}
            ]


category = {}
icon = {}
for i in BDD_card:
    category[i['cat']] = True
    icon[i['cat']] = 'o'
nb_category = len(category)

icon['Alcool'] = '🥃'
icon['Sport'] = '💪'
icon['Other'] = '😉'
icon['Hot'] = '🫦'




BASIC_COLOR = [.2,.6,.1]
WRONG_COLOR = [.9,.3,.1]

# KV:
KV = '''
ScreenManager:
    MenuScreen:
    SettingsScreen:
    GameScreen:
    EndScreen:

<MenuScreen>:
    id: menu_screen
    name: 'menu'
    
    MDLabel:
        id: initializer
        text: root.initialize()
    
    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .1,.1,.1

    MDCard:
        size_hint: 1, 0.1
        pos_hint: {'center_x':0.5, 'center_y':0.925}
        radius: 0
        md_bg_color: .2,.6,1
        elevation: 2
        shadow_offset: (0, -2)

    MDLabel:
        text: "Cyclone - M.O.'s version"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.925}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "30sp"
 

    ElevatedWidget:
        pos_hint: {'center_x':0.5, 'center_y':0.12}
        size_hint: 0.9,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_release:
            root.initSettings()
            root.manager.transition.direction = 'left'
            root.manager.current = 'settings'
    
    MDLabel:
        text: "Play"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.12}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
    

        

<SettingsScreen>:
    id: settings_screen
    name: 'settings'
    on_enter: self.initialize()

    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .1,.1,.1
    
    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'left':1, 'top':1}
        on_release:
            root.manager.transition.direction = 'right'
            root.manager.current = 'menu'

    ElevatedWidget:
        pos_hint: {'center_x':0.5, 'center_y':0.12}
        size_hint: 0.9,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_release:
            root.initGame(slider_cards.value)
            root.manager.transition.direction = 'left'
            root.manager.current = 'game'
    
    MDLabel:
        id: play_text
        text: "Play"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.12}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"

    MDLabel:
        text: "Number of cards"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: "white"

    MDSlider:
        id: slider_cards
        thumb_color_active: "red"
        thumb_color_inactive: "red"
        size_hint: 0.8,0.5
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        step: 2
        min: 2
        max: 4
        value: 2

    MDCard:
        size_hint: 0.8, 0.15
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        radius: 20
        md_bg_color: .2,.2,.2
        elevation: 2
        shadow_offset: (0, -2)
    
    MDLabel:
        id: j1_name
        text: root.playerName(0)
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "40sp"
    
    MDCard:
        size_hint: 0.8, 0.15
        pos_hint: {'center_x':0.5, 'center_y':0.52}
        radius: 20
        md_bg_color: .2,.2,.2
        elevation: 2
        shadow_offset: (0, -2)
    
    MDLabel:
        id: j2_name
        text: root.playerName(1)
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.52}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "40sp"

    
        

<GameScreen>:
    id: game_screen
    name: 'game'
    on_enter: self.initialize()

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
        id: question_text
        halign: 'center'
        text: ""
        pos_hint: {"center_x":0.5, "center_y":0.65}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
    
    Label:
        id: question_shots
        text: "0"
        halign: 'center'
        pos_hint: {"center_x":0.85, "center_y":0.88}
        size_hint: 0.1,0.1
        font_size: "40sp"

    Label:
        id: question_icon
        text: ""
        halign: 'center'
        pos_hint: {"center_x":0.15, "center_y":0.88}
        size_hint: 0.1,0.1
        font_size: "40sp"

    
    Screen:
        id: layout

    Label:
        id: nb_card_left
        text: ""
        halign: 'center'
        pos_hint: {"center_x":0.5, "center_y":0.965}
        size_hint: 0.1,0.1
        font_size: "40sp"

        

<EndScreen>:
    id: end_screen
    name: 'end'
    on_enter: self.initialize()

    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .1,.1,.1

    MDRectangleFlatButton:
        text: "Back"
        pos_hint: {'left':1, 'top':1}
        on_release:
            root.manager.transition.direction = 'right'
            root.manager.current = 'menu'

    
    MDCard:
        size_hint: 0.8, 0.15
        pos_hint: {'center_x':0.5, 'center_y':0.7}
        radius: 20
        md_bg_color: .2,.2,.2
        elevation: 2
        shadow_offset: (0, -2)

    MDCard:
        size_hint: 0.8, 0.15
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 20
        md_bg_color: .2,.2,.2
        elevation: 2
        shadow_offset: (0, -2)

    MDLabel:
        id: j1_name
        text: ""
        halign: "center"
        pos_hint: {'center_x':0.3, 'center_y':0.7}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "40sp"
    
    MDLabel:
        id: j2_name
        text: ""
        halign: "center"
        pos_hint: {'center_x':0.3, 'center_y':0.5}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "40sp"

    MDLabel:
        id: j1_shots
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.8, 'center_y':0.7}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "40sp"

    MDLabel:
        id: j2_shots
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.8, 'center_y':0.5}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "40sp"

    Label:
        id: nb_card_done
        text: ""
        halign: 'center'
        pos_hint: {"center_x":0.5, "center_y":0.2}
        size_hint: 0.1,0.1
        font_size: "40sp"


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




has_init_settings_screen = False
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize(self):
        global has_init_settings_screen
        if not has_init_settings_screen:
            has_init_settings_screen = True
            size_base = 0.78
            size_y = 0.15
            i=0
            for cat_name in category.keys():
                hauteur = size_base -i*size_y
                self.add_widget(ElevatedWidget(
                    id= cat_name,
                    pos_hint= {'center_x':0.5, 'center_y':hauteur},
                    size_hint= [0.9, size_y-0.025],
                    elevation= 2,
                    md_bg_color= BASIC_COLOR,
                    radius= 18,
                    on_release= self.selectCat
                ))
                self.add_widget(MDLabel(
                    text= icon[cat_name] + '   ' + cat_name,
                    halign= "center",
                    pos_hint= {'center_x':0.5, 'center_y':hauteur},
                    theme_text_color= "Custom",
                    text_color= "white",
                    font_size= "50sp"
                ))
                i += 1
        return " "

    def selectCat(self, box):
        category[box.id] = not category[box.id]
        if category[box.id]:
            box.md_bg_color = BASIC_COLOR
        else:
            box.md_bg_color = WRONG_COLOR
        print(category)

    
    def initSettings(self):
        for i in player_list:
            i.reset()

        global questions
        questions = []
        for i in BDD_card:
            if category[i['cat']]: # and i['type'] == "s":
                questions.append(i)
        rd.shuffle(questions)
    
    
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def initialize(self):
        global questions
        self.ids.slider_cards.max = len(questions)
        self.ids.slider_cards.value = min(len(questions), 40)
        return len(questions)

    def initGame(self, nb_of_card):
        global nb_card
        nb_card = nb_of_card
        global id_player
        global questions
        id_player = rd.randint(0,1)
        questions = questions[:nb_card]
    
    def playerName(self, id):
        return player_list[id].name

    

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id_card = -1
        self.card = None
        self.id_player = rd.randint(0,1)
        
        self.selected_player = [False, False]
        self.liste_id_widget = []
        self.liste_widgets = []

    def initialize(self):
        self.selected_player = [False, False]
        self.liste_id_widget = []
        self.liste_widgets = []
        self.id_card = -1
        self.card = None
        self.id_player = rd.randint(0,1)
        self.actu()

    def actu(self):
        self.ids.layout.clear_widgets()

        self.id_player = 1 - self.id_player
        self.id_card += 1

        self.ids.nb_card_left.text = str(len(questions) - self.id_card)

        if self.id_card < len(questions):
            self.card = questions[self.id_card]

            sentence = self.card['text'].split("$")
            text = ""
            for i in sentence:
                if i == 'A':
                    text += player_list[self.id_player].name
                elif i == 'B':
                    text += player_list[1-self.id_player].name
                elif i == 'g':
                    text += "'"
                else:
                    text += i

            self.ids.question_text.text = text
            self.ids.question_icon.text = icon[self.card['cat']]
            self.ids.question_shots.text = str(self.card['shots'])

            self.create_button_game(self.card['type'])
        else:
            self.manager.current = 'end'
        
    def create_button_game(self, card_type):
        if card_type == 'g':
            hight = 0.2
            self.liste_id_widget = ["p1_button", "p2_button", "p1_button_label", "p2_button_label"]
            self.liste_widgets = [
                ElevatedWidget(
                    id = self.liste_id_widget[0],
                    pos_hint= {'center_x':0.75, 'center_y':hight},
                    size_hint= [0.47, 0.37],
                    elevation= 2,
                    md_bg_color= [.2,.2,.2],
                    radius= 18,
                    on_release= self.g_p1_selected
                ),ElevatedWidget(
                    id = self.liste_id_widget[1],
                    pos_hint= {'center_x':0.25, 'center_y':hight},
                    size_hint= [0.47, 0.37],
                    elevation= 2,
                    md_bg_color= [.2,.2,.2],
                    radius= 18,
                    on_release= self.g_p2_selected
                ),MDLabel(
                    id = self.liste_id_widget[2],
                    text = player_list[0].name,
                    halign = "center",
                    pos_hint = {'center_x':0.75, 'center_y':hight},
                    theme_text_color = "Custom",
                    text_color = "white",
                    font_size = "40sp"
                ),MDLabel(
                    id = self.liste_id_widget[3],
                    text = player_list[1].name,
                    halign = "center",
                    pos_hint = {'center_x':0.25, 'center_y':hight},
                    theme_text_color = "Custom",
                    text_color = "white",
                    font_size = "40sp"
                )]

        elif card_type == 's':
            hight = 0.28
            hight2 = 0.08
            self.liste_id_widget = ["p1_button", "p2_button", "p1_button_label", "p2_button_label", "next_button", "next_button_label"]
            self.liste_widgets = [
                ElevatedWidget(
                    id = self.liste_id_widget[0],
                    pos_hint= {'center_x':0.75, 'center_y':hight},
                    size_hint= [0.47, 0.22],
                    elevation= 2,
                    md_bg_color= WRONG_COLOR,
                    radius= 18,
                    on_release= self.s_p1_select
                ),ElevatedWidget(
                    id = self.liste_id_widget[1],
                    pos_hint= {'center_x':0.25, 'center_y':hight},
                    size_hint= [0.47, 0.22],
                    elevation= 2,
                    md_bg_color= WRONG_COLOR,
                    radius= 18,
                    on_release= self.s_p2_select
                ),MDLabel(
                    id = self.liste_id_widget[2],
                    text = player_list[0].name,
                    halign = "center",
                    pos_hint = {'center_x':0.75, 'center_y':hight},
                    theme_text_color = "Custom",
                    text_color = "white",
                    font_size = "40sp"
                ),MDLabel(
                    id = self.liste_id_widget[3],
                    text = player_list[1].name,
                    halign = "center",
                    pos_hint = {'center_x':0.25, 'center_y':hight},
                    theme_text_color = "Custom",
                    text_color = "white",
                    font_size = "40sp"
                ),ElevatedWidget(
                    id = self.liste_id_widget[1],
                    pos_hint= {'center_x':0.5, 'center_y':hight2},
                    size_hint= [0.95, 0.15],
                    elevation= 2,
                    md_bg_color= [.2,.2,.2],
                    radius= 18,
                    on_release= self.s_pass
                ),MDLabel(
                    id = self.liste_id_widget[2],
                    text = "Next",
                    halign = "center",
                    pos_hint = {'center_x':0.5, 'center_y':hight2},
                    theme_text_color = "Custom",
                    text_color = "white",
                    font_size = "40sp"
                )]

        elif card_type == '_':
            hight = 0.2
            self.liste_id_widget = ["validated_button", "not_validated_button", "validated_button_label", "not_validated_button_label"]
            self.liste_widgets = [
                ElevatedWidget(
                    id = self.liste_id_widget[0],
                    pos_hint= {'center_x':0.75, 'center_y':hight},
                    size_hint= [0.47, 0.37],
                    elevation= 2,
                    md_bg_color= [.2,.2,.2],
                    radius= 18,
                    on_release= self.validated
                ),ElevatedWidget(
                    id = self.liste_id_widget[1],
                    pos_hint= {'center_x':0.25, 'center_y':hight},
                    size_hint= [0.47, 0.37],
                    elevation= 2,
                    md_bg_color= [.2,.2,.2],
                    radius= 18,
                    on_release= self.not_validated
                ),MDLabel(
                    id = self.liste_id_widget[2],
                    text = "\/✅",
                    halign = "center",
                    pos_hint = {'center_x':0.75, 'center_y':hight},
                    theme_text_color = "Custom",
                    text_color = "white",
                    font_size = "40sp"
                ),MDLabel(
                    id = self.liste_id_widget[3],
                    text = "X❌",
                    halign = "center",
                    pos_hint = {'center_x':0.25, 'center_y':hight},
                    theme_text_color = "Custom",
                    text_color = "white",
                    font_size = "40sp"
                )]
            
        for i in range(len(self.liste_widgets)):
            self.ids.layout.add_widget(self.liste_widgets[i])


    def validated(self, _):
        # print("validated")
        self.actu()

    def not_validated(self, _):
        # print("not_validated")
        player_list[self.id_player].shots += self.card['shots']
        self.actu()

    def g_p1_selected(self,_):
        self.g_selected(0)

    def g_p2_selected(self,_):
        self.g_selected(1)
        
    def g_selected(self, id):
        player_list[id].shots += self.card['shots']
        self.actu()

    def s_p1_select(self, _):
        self.s_select(0)
        
    def s_p2_select(self, _):
        self.s_select(1)

    def s_select(self, id):
        self.selected_player[id] = not self.selected_player[id]
        color = None
        if self.selected_player[id]:
            color = BASIC_COLOR
        else:
            color = WRONG_COLOR
        self.liste_widgets[id].md_bg_color = color

    def s_pass(self, _):
        for i in range(len(self.selected_player)):
            if self.selected_player[i]:
                player_list[i].shots += self.card['shots']
        self.actu()


class EndScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize(self):
        self.ids.nb_card_done.text = "With " + str(len(questions)) + " cards done"
        m = 0
        if player_list[0].shots > player_list[1].shots:
            m = 1
        for i in range(0,2):
            self.ids['j' + str(i+1) + '_name'].text = player_list[(i+m)%2].name
            self.ids['j' + str(i+1) + '_shots'].text = str(player_list[(i+m)%2].shots)




sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GameScreen(name='settings'))
sm.add_widget(GameScreen(name='game'))
sm.add_widget(GameScreen(name='end'))


class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen
    


ma = MainApp()
ma.run()