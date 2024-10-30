from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.video import Video


Window.clearcolor = (255/255, 255/255, 255/255)
Window.size = (360, 640)

class pilih_tema(Screen):
    def __init__(self, **kwargs):
        super(pilih_tema, self).__init__(**kwargs)
        self.manager = kwargs.get('manager')

    def terima_variabel(self, tutor, bolen):
        self.tutor=tutor
        self.bolen = bolen

        layout1 = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(orientation='vertical',spacing=20, padding=20)

        self.background_video = Video(
            source="video/background.mp4",  
            state='play', 
            options={'eos': 'loop'},
            allow_stretch=True,
            keep_ratio=False
        )

        self.soundButton = SoundLoader.load('sound/button.wav')

        self.back = ClickableImage(
            source ="images/back.png",
            size_hint=(0.14, 0.14,)
        )
        self.back.bind(on_press=self.kembali)

        self.title=Image(
            source='images/title_pilih_tema.png',
            size_hint=(0.8, 0.4)
        )
        self.title.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.button1=ClickableImage(
            source='images/number.png'
        )
        self.button1.bind(on_press=lambda instance: self.pilih_level(instance, "number"))


        self.button2=ClickableImage(
            source='images/fruits.png'
        )
        self.button2.bind(on_press=lambda instance: self.pilih_level(instance, "fruits"))


        self.button3=ClickableImage(
            source='images/animal.png'
        )
        self.button3.bind(on_press=lambda instance: self.pilih_level(instance, "animal"))


        self.label=Label(
            text="",
            size_hint=(1,0.3)
        )

        layout1.add_widget(self.back)
        layout1.add_widget(self.title)
        layout2.add_widget(self.button1)
        layout2.add_widget(self.button2)
        layout2.add_widget(self.button3)
        layout1.add_widget(layout2)
        layout1.add_widget(self.label)

        self.add_widget(self.background_video)
        self.add_widget(layout1)

    # def on_enter(self):
    #     if self.manager.get_screen('homeBox').backsound:
    #         self.manager.get_screen('homeBox').backsound.stop()

    def kembali(self, instance):
        print("teessss")
        self.soundButton.play()
        self.manager.get_screen('homeBox').terima_variabel(self.bolen)
        self.manager.current = 'homeBox'

    def pilih_level(self, instance, tema):
        self.soundButton.play()
        if self.tutor == "play":
            self.manager.get_screen('pilih_levelBox').terima_tema(tema, self.bolen)
            self.manager.current = 'pilih_levelBox'
        elif self.tutor == "tutor":
            if tema == "number":
                self.manager.get_screen('tutor_number').terima_variabel(self.bolen)
                self.manager.current = 'tutor_number'
            elif tema == "fruits":
                self.manager.get_screen('tutor_fruits').terima_variabel(self.bolen)
                self.manager.current = 'tutor_fruits'
            elif tema == "animal":
                self.manager.get_screen('tutor_animal').terima_variabel(self.bolen)
                self.manager.current = 'tutor_animal'

    def on_enter(self, *args):
        self.background_video.state = 'play'
        self.manager.get_screen('splash').backsound.volume = 1

    def on_leave(self, *args):
        print("stop")
        # self.soundButton.stop()
        self.background_video.state = 'stop'
        
        # return layout1

class ClickableImage(ButtonBehavior, Image):
    def on_pre(self):
        print(1)
    
# pilih_tema().run()
