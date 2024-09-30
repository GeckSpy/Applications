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

# Constantes:
nb_card = 30



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
 
    MDLabel:
        text: "Number of cards"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: "black"

    MDSlider:
        id: slider_cards
        thumb_color_active: "red"
        thumb_color_inactive: "red"
        size_hint: 0.8,0.5
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        step: 1
        min: 0
        max: 80
        value: 40

    ElevatedWidget:
        pos_hint: {'center_x':0.5, 'center_y':0.12}
        size_hint: 0.9,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_release:
            app.InitGame(slider_cards.value)
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

    

<GameScreen>:
    id: game_screen
    name: 'game'


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
    

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


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
    
    def InitGame(self, nb_carte):
        pass
    

ma = MainApp()
ma.run()