from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.behaviors import BackgroundColorBehavior, CommonElevationBehavior, RectangularRippleBehavior
from kivymd.uix.widget import MDWidget
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import GridLayout

import random as rd

# Constantes:
nb_card = 30

class Player():
    def __init__(self, name):
        self.name = name
        self.shots = 0

    def reset(self):
        self.shots = 0

player1 = Player("Macéo")
player2 = Player("Maëlle")
player_list = [player1, player2]

questions = []
BDD_card = [{'cat':'Sport','type':'_', 'shots':4, 'text':'$A$, fait 2 pompes'}, {'cat':'Sport','type':'_', 'shots':8, 'text':'$A$, fait 5 pompes'}, {'cat':'Sport','type':'_', 'shots':2, 'text':'$A$, fait 3 squats'}, {'cat':'Sport','type':'_', 'shots':3, 'text':'$A$, fait une traction'}, {'cat':'Alcool','type':'_', 'shots':2, 'text':'$A$, boit 2 gorgées'}, {'cat':'Alcool','type':'_', 'shots':4, 'text':'$A$, boit 4 gorgées'}, {'cat':'Alcool','type':'_', 'shots':10, 'text':'Cul Sec !'}, {'cat':'Alcool','type':'_', 'shots':1, 'text':'$A$, donne 2 gorgées à qui tu veux'}, {'cat':'Alcool','type':'_', 'shots':3, 'text':'$A$, donne 4 gorgées à qui tu veux'}, {'cat':'Alcool','type':'g', 'shots':1, 'text':'ShiFouMi, celui qui perd boit'}, {'cat':'Alcool','type':'_', 'shots':2, 'text':'$A$, boit une gorgée du verre de $B$'}, {'cat':'Alcool','type':'g', 'shots':1, 'text':'La derniere personne à avoir fais du sport distribue 1 gorgée'}, {'cat':'Alcool','type':'g', 'shots':2, 'text':'La derniere personne à avoir pisser sous la douche boit 2 gorgé'}, {'cat':'Other','type':'_', 'shots':2, 'text':'$A$, échange de place avec $B$'}, {'cat':'Hot','type':'_', 'shots':2, 'text':'$A$, embrasse $B$'}, {'cat':'Hot','type':'_', 'shots':4, 'text':'$A$, monte sur les genoux de $B$ pendant 2 tours'}
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

    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .1,.1,.1

    MDCard:
        size_hint: 1, 0.15
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
        max: root.numberOfCards()
        value: min(root.numberOfCards(), 40)

    ElevatedWidget:
        pos_hint: {'center_x':0.5, 'center_y':0.12}
        size_hint: 0.9,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_release:
            app.InitSettings(slider_cards.value)
            root.manager.transition.direction = 'left'
            root.manager.current = 'settings'
    
    MDLabel:
        text: "Play"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.12}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
    
        
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
            root.initGame()
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

    ElevatedWidget:
        id: validated_button
        pos_hint: {'center_x':0.75, 'center_y':0.17}
        size_hint: 0.47,0.3
        elevation: 2
        radius: 18
        shadow_offset: (2,-2)
        md_bg_color: .15,.15,.15
        on_press: root.checked()
    
    ElevatedWidget:
        id: passed_button
        pos_hint: {'center_x':0.25, 'center_y':0.17}
        size_hint: 0.47,0.3
        elevation: 2
        radius: 18
        shadow_offset: (2,-2)
        md_bg_color: .15,.15,.15
        on_press: root.passed()

    Label:
        id: text_passed
        text: ""
        pos_hint: {"x":0.2, "y":0.13}
        size_hint: 0.1,0.1
        font_size: "40sp"

    Label:
        id: text_validated
        text: ""
        pos_hint: {"x":0.7, "y":0.13}
        size_hint: 0.1,0.1
        font_size: "40sp"

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

    def initialize(self):
        self.ids.j1_name.text = player1.name
        self.ids.j2_name.text = player2.name

    def playerName(self, id):
        return player_list[id].name
    
    def numberOfCards(self):
        return len(BDD_card)
    

has_init_settings_screen = False
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def initialize(self):
        global has_init_settings_screen
        if not has_init_settings_screen:
            has_init_settings_screen = True
            size_base = 0.85
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

    def selectCat(self, box):
        category[box.id] = not category[box.id]
        if category[box.id]:
            box.md_bg_color = BASIC_COLOR
        else:
            box.md_bg_color = WRONG_COLOR
        print(category)

    def initGame(self):
        global id_player
        global questions
        questions = []
        id_player = rd.randint(0,1)
        for i in BDD_card:
            if category[i['cat']]:
                questions.append(i)
        rd.shuffle(questions)
        questions = questions[:nb_card]
        print(questions)

    

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id_card = -1
        self.card = None
        self.id_player = rd.randint(0,1)
        self.is_game = False

    def initialize(self):
        self.id_card = -1
        self.card = None
        self.id_player = rd.randint(0,1)
        self.actu()

    def actu(self):
        self.id_player = 1 - self.id_player
        self.id_card += 1

        if self.id_card < len(questions):
            self.card = questions[self.id_card]

            sentence = self.card['text'].split("$")
            text = ""
            for i in sentence:
                if i == 'A':
                    text += player_list[self.id_player].name
                elif i == 'B':
                    text += player_list[1-self.id_player].name
                else:
                    text += i

            self.ids.question_text.text = text
            self.ids.question_icon.text = icon[self.card['cat']]
            self.ids.question_shots.text = str(self.card['shots'])

            if self.card['type'] == 'g':
                self.is_game = True
                self.ids.text_passed.text = player1.name
                self.ids.text_validated.text = player2.name
            else:
                self.is_game = False
                self.ids.text_passed.text = "X❌"
                self.ids.text_validated.text = "\/✅"
        else:
            self.manager.current = 'end'
        

    def checked(self):
        if self.is_game:
            player2.shots += self.card['shots']
        self.actu()

    def passed(self):
        if self.is_game:
            player1.shots += self.card['shots']
        else:
            player_list[self.id_player].shots += self.card['shots']
        self.actu()
        



class EndScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize(self):
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
    
    def InitSettings(self, numbers_of_cards):
        global nb_card
        nb_card = numbers_of_cards
        for i in player_list:
            i.reset()


ma = MainApp()
ma.run()