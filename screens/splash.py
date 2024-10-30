from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.audio import SoundLoader


Window.clearcolor = (255/255, 255/255, 255/255)
Window.size = (360, 640)

class splash(Screen):
    def __init__(self, **kwargs):
        super(splash, self).__init__(**kwargs)
        
        layout1 = BoxLayout(orientation='vertical', spacing=20)
        self.backsound = SoundLoader.load('sound/backsound.mp3')

        background = Image(
            source="images/splashBG.png",
            allow_stretch=True,
            keep_ratio=False
        )


        self.title = Image(
            source ="images/splashLogo.png",
            size_hint=(1, 1),
        )
        self.title.pos_hint = {'center_x': 0.5, 'center_y': 0.5}


        self.loading_label = Label(
            text='Loading...',
            font_size=40,
            pos_hint={'center_x': 0.5},
            color=(1, 1, 1, 1)
        )

        layout1.add_widget(self.title)
        layout1.add_widget(self.loading_label)

        self.add_widget(background)
        self.add_widget(layout1)

    def start_animation(self):
        loading_animation = Animation(color=(1, 1, 1, 0), duration=0.5) + Animation(color=(1, 1, 1, 1), duration=0.5)
        loading_animation.repeat = True
        loading_animation.start(self.loading_label)

    def on_enter(self, *args):
        Clock.schedule_once(self.go_to_main_screen, 3)
        self.start_animation()

    def go_to_main_screen(self, instance):
        print("teessss")
        bolen = 0
        self.manager.get_screen('homeBox').terima_variabel(bolen)
        self.manager.current = 'homeBox'
        self.backsound.play()
    
    
class ClickableImage(ButtonBehavior, Image):
    def on_pre(self):
       print(1)
