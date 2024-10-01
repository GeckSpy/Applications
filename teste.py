from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.behaviors import BackgroundColorBehavior, CommonElevationBehavior, RectangularRippleBehavior
from kivymd.uix.widget import MDWidget
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import GridLayout


class check_box(GridLayout):
    def __init__(self, **kwargs):
        super(check_box, self).__init__(**kwargs)
        self.rows = 3
        
        self.add_widget(Label(text='OUI TEXT', pos_hint= {'center_x':0.2, 'center_y':0.5}))
        self.active = CheckBox(active = False, pos_hint= {'center_x':0.5, 'center_y':0.5})
        self.add_widget(self.active)

    
    
class CBApp(App):
    def build(self):
        return check_box()
    
CBApp().run()