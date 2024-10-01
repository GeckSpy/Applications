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

import random as rd

# Constantes:
nb_card = 30

class Player():
    def __init__(self, name):
        self.name = name
        self.shots = 0

player1 = Player("P1_name")
player2 = Player("P2_name")
id_player = 0
player_list = [player1, player2]

questions = []
BDD_card = [{'cat':'Alcool', 'shots':2, 'text':'$A$ boit 2 gorgées'}, {'cat':'Jeux', 'shots':2, 'text':'Thème: les alcools'}
            ]


category = {}
icon = {}
for i in BDD_card:
    category[i['cat']] = True
    icon[i['cat']] = 'o'

icon['Alcool'] = '🥃'

validated = {True: 'Oui', False: 'Non'}

# KV:
KV = '''
ScreenManager:
    MenuScreen:
    SettingsScreen:
    GameScreen:

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
        step: 1
        min: 2
        max: 80
        value: 40

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
        md_bg_color: .3,.3,.3
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
        md_bg_color: .3,.3,.3
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
        md_bg_color: .2,.2,.2
    
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

    
    ScrollView:
        MDList:
            id: category_list
        

<GameScreen>:
    id: game_screen
    name: 'game'

    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .2,.2,.2


'''

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    pass



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
    


has_init_settings_screen = False
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def initialize(self):
        global has_init_settings_screen
        if not has_init_settings_screen:
            has_init_settings_screen = True
            for cat_name in category.keys():
                self.ids.category_list.add_widget(ListItemWithCheckbox(
                        id = cat_name,
                        text = icon[cat_name] + ' ' + cat_name,
                        on_release = self.selectCat
                    )
                )

    def selectCat(self, box):
        category[box.id] = not category[box.id]
        print(category)

    def initGame(self):
        global id_player
        id_player = rd.randint(0,1)
    
    

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GameScreen(name='settings'))
sm.add_widget(GameScreen(name='game'))


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


ma = MainApp()
ma.run()