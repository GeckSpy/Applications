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

path_data_base = "./words/BDD.txt"
f = open(path_data_base, "r")
global bdd_words
bdd_words = []
for lignes in f:
    l = lignes[:-1]
    bdd_words.append(l)
f.close()
print("Nombre de mots dans la base de donée :", len(bdd_words))

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