from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.video import Video
from kivy.clock import Clock

Window.clearcolor = (255/255, 255/255, 255/255)
Window.size = (360, 640)

class homeBox(Screen):
    def __init__(self, **kwargs):
        super(homeBox, self).__init__(**kwargs)
        
    def terima_variabel(self, bolen):
        self.bolen = bolen

        layout1 = BoxLayout(orientation='vertical', spacing=20)
        layout2 = BoxLayout(orientation='vertical', padding=10, spacing=20)
        layout3 = BoxLayout()
        layout4 = BoxLayout()
        layout5 = BoxLayout()

        self.background_video = Video(
            source="video/background.mp4",
            state='play',
            options={'eos': 'loop'},
            allow_stretch=True,
            keep_ratio=False
        )

        self.soundButton = SoundLoader.load('sound/button.wav')
        self.backsound = SoundLoader.load('sound/backsound.mp3')

        self.title = Image(
            source ="images/title.png",
            size_hint=(0.8, 0.8),
        )
        self.title.pos_hint = {'center_x': 0.5, 'center_y': 0.5}


        self.button1 = ClickableImage(
            source='images/play.png'
        )
        self.button1.bind(on_press=lambda instance: self.pilih_tema(instance, "play"))



        self.button2 = ClickableImage(
            source='images/study.png'
        )
        self.button2.bind(on_press=lambda instance: self.pilih_tema(instance, "tutor"))

        label = Label(
            text=''
        )
        

        layout2.add_widget(self.button1)
        layout2.add_widget(self.button2)
        layout2.add_widget(label)
        layout1.add_widget(self.title)
        layout1.add_widget(layout2)

        self.add_widget(self.background_video)
        self.add_widget(layout1)

        print(self.bolen)
    def on_enter(self, *args):
        self.background_video.state = 'play'
        if self.bolen == 0:
            self.manager.get_screen('splash').backsound
            self.manager.get_screen('splash').backsound.stop()
            self.manager.get_screen('splash').backsound.play()
            self.manager.get_screen('splash').backsound.volume = 1
            print("mkm")
        elif self.bolen == 1:
            self.manager.get_screen('selebration').backsound
            self.manager.get_screen('selebration').backsound.stop()
            self.manager.get_screen('splash').backsound
            self.manager.get_screen('splash').backsound.play()
            self.bolen = 0
        else:
            print("halah")

    def play_sound(self, *args):
        self.backsound.play()
        print("mulai")

    def stop_sound(self, *args):
        self.backsound.stop()
        print("berhenti")

    def on_leave(self, *args):
        print("stop")
        # self.soundButton.stop()
        self.background_video.state = 'stop'

    def pilih_tema(self, instance, tutor):
        print("teessss")
        self.soundButton.play()
        self.manager.get_screen('pilih_tema').terima_variabel(tutor,self.bolen)
        self.manager.current = 'pilih_tema'
    
    
class ClickableImage(ButtonBehavior, Image):
    def on_pre(self):
       print(1)
