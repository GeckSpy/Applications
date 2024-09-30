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



KV = '''
ScreenManager:
    MenuScreen:

<MenuScreen>:
    id: menu_screen
    name: 'menu'

    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        radius: 0
        md_bg_color: .2,.2,.2
        

    MDCard:
        id: card_2
        pos_hint: {'center_x':0.075, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 

    MDCard:
        id: card_3
        pos_hint: {'center_x':0.16, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 

    MDCard:
        id: card_4
        pos_hint: {'center_x':0.245, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 

    MDCard:
        id: card_5
        pos_hint: {'center_x':0.33, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 

    MDCard:
        id: card_6
        pos_hint: {'center_x':0.415, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 
        
    MDCard:
        id: card_7
        pos_hint: {'center_x':0.5, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 

    MDCard:
        id: card_8
        pos_hint: {'center_x':0.585, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 

    MDCard:
        id: card_9
        pos_hint: {'center_x':0.67, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2

    MDCard:
        id: card_10
        pos_hint: {'center_x':0.755, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 
    
    MDCard:
        id: card_11
        pos_hint: {'center_x':0.84, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 
        
    MDCard:
        id: card_12
        pos_hint: {'center_x':0.925, 'center_y':0.72}
        size_hint: 0.06, 0
        elevation: 1
        md_bg_color: 1, .5, .0
        radius: 2 



    MDCard:
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.24}
        radius: 0
        md_bg_color: .2,.2,.2
        

    ElevatedWidget:
        pos_hint: {'center_x':0.125, 'center_y':0.575}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(2)

    MDLabel:
        text: "2"
        halign: "center"
        pos_hint: {'center_x':0.125, 'center_y':0.575}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"

    MDLabel:
        id: pourcen_2
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.125, 'center_y':0.51}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.375, 'center_y':0.575}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(3)

    MDLabel:
        text: "3"
        halign: "center"
        pos_hint: {'center_x':0.375, 'center_y':0.575}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
        
    MDLabel:
        id: pourcen_3
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.375, 'center_y':0.51}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.625, 'center_y':0.575}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(4)
    
    MDLabel:
        text: "4"
        halign: "center"
        pos_hint: {'center_x':0.625, 'center_y':0.575}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
    
    MDLabel:
        id: pourcen_4
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.625, 'center_y':0.51}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.875, 'center_y':0.575}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(5)

    MDLabel:
        text: "5"
        halign: "center"
        pos_hint: {'center_x':0.875, 'center_y':0.575}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"

    MDLabel:
        id: pourcen_5
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.875, 'center_y':0.51}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.125, 'center_y':0.35}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(6)

    MDLabel:
        text: "6"
        halign: "center"
        pos_hint: {'center_x':0.125, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
    
    MDLabel:
        id: pourcen_6
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.125, 'center_y':0.285}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.375, 'center_y':0.35}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(7)

    MDLabel:
        text: "7"
        halign: "center"
        pos_hint: {'center_x':0.375, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
    
    MDLabel:
        id: pourcen_7
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.375, 'center_y':0.285}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.625, 'center_y':0.35}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(8)
    
    MDLabel:
        text: "8"
        halign: "center"
        pos_hint: {'center_x':0.625, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
    
    MDLabel:
        id: pourcen_8
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.625, 'center_y':0.285}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.875, 'center_y':0.35}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(9)

    MDLabel:
        text: "9"
        halign: "center"
        pos_hint: {'center_x':0.875, 'center_y':0.35}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
    
    MDLabel:
        id: pourcen_9
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.875, 'center_y':0.285}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.125, 'center_y':0.125}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(10)

    MDLabel:
        text: "10"
        halign: "center"
        pos_hint: {'center_x':0.125, 'center_y':0.125}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"

    MDLabel:
        id: pourcen_10
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.125, 'center_y':0.06}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    ElevatedWidget:
        pos_hint: {'center_x':0.375, 'center_y':0.125}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(11)

    MDLabel:
        text: "11"
        halign: "center"
        pos_hint: {'center_x':0.375, 'center_y':0.125}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"
    
    MDLabel:
        id: pourcen_11
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.375, 'center_y':0.06}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"
        
    ElevatedWidget:
        pos_hint: {'center_x':0.625, 'center_y':0.125}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .2,.6,1
        radius: 18
        on_press:
            root.actu(12)

    MDLabel:
        text: "12"
        halign: "center"
        pos_hint: {'center_x':0.625, 'center_y':0.125}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"

    MDLabel:
        id: pourcen_12
        text: "0.00%"
        halign: "center"
        pos_hint: {'center_x':0.625, 'center_y':0.06}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"
        
    ElevatedWidget:
        pos_hint: {'center_x':0.875, 'center_y':0.125}
        size_hint: 0.2,0.2
        elevation: 2
        md_bg_color: .3,.3,.3
        radius: 18
        on_press:
            root.undo()

    MDLabel:
        text: "x"
        halign: "center"
        pos_hint: {'center_x':0.875, 'center_y':0.125}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "50sp"

        
    MDCard:
        pos_hint: {'center_x':0.5, 'center_y':0.72}
        size_hint: 0.95, 0.04
        elevation: 1
        md_bg_color: .7, .7, .7
        radius: 2


    MDLabel:
        text: "2"
        halign: "center"
        pos_hint: {'center_x':0.075, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "3"
        halign: "center"
        pos_hint: {'center_x':0.16, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "4"
        halign: "center"
        pos_hint: {'center_x':0.245, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "5"
        halign: "center"
        pos_hint: {'center_x':0.33, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "6"
        halign: "center"
        pos_hint: {'center_x':0.415, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "7"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "8"
        halign: "center"
        pos_hint: {'center_x':0.585, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "9"
        halign: "center"
        pos_hint: {'center_x':0.67, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "10"
        halign: "center"
        pos_hint: {'center_x':0.755, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "11"
        halign: "center"
        pos_hint: {'center_x':0.84, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        text: "12"
        halign: "center"
        pos_hint: {'center_x':0.925, 'center_y':0.72}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

        

    MDLabel:
        id: compt_2
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.075, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_3
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.16, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_4
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.245, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_5
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.33, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_6
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.415, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_7
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_8
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.585, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_9
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.67, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_10
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.755, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_11
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.84, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"

    MDLabel:
        id: compt_12
        text: "0"
        halign: "center"
        pos_hint: {'center_x':0.925, 'center_y':0.76}
        theme_text_color: "Custom"
        text_color: "white"
        font_size: "20sp"
    
'''

undo_list = []
stat_list = {}
stat_list[0] = 0
for i in range(2,13):
    stat_list[i] = 0
nb_jet = 0


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
    def actu(self, number):
        if number != 0:
            stat_list[number] += 1
            undo_list.append(number)
            global nb_jet
            nb_jet += 1

        maxi = 0
        for i in stat_list.keys():
            maxi = max(stat_list[i], maxi)

        for i in range(2,13):
            size = 0.0000000001 if maxi==0 or stat_list[i]==0 else stat_list[i]*0.5/maxi
            self.ids['card_' + str(i)].size_hint[1] = size
            self.ids['compt_' + str(i)].text = str(stat_list[i])
            #self.ids['compt_' + str(i)].pos_hint['center_y'] = max(size/2 + 0.74, 0.76)
            self.ids['pourcen_' + str(i)].text = "0.00%" if nb_jet==0 else str(int(stat_list[i]*10000/nb_jet)/100) + '%'


    def undo(self):
        ll = len(undo_list)
        if ll > 0:
            global nb_jet
            nb_jet -= 1
            x = undo_list[ll-1]
            del undo_list[ll-1]
            stat_list[x] -= 1
            self.actu(0)




sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

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