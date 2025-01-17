from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.video import Video
import json


Window.clearcolor = (255/255, 255/255, 255/255)
Window.size = (360, 640)

class ColoredLabel(BoxLayout):
    def __init__(self, tema, level, **kwargs):
        super(ColoredLabel, self).__init__(**kwargs)
        self.tema = tema
        self.level = level

        with self.canvas.before:
            Color(108/255, 56/255, 117/255, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        title = self.get_field_data(self.tema, self.level, "title", 0)
        label = Label(
            text=f"{title}", 
            font_size=20, 
            halign='center',
            size_hint=(1, 1)
        )
        label.color = (1, 1, 1, 1)
        self.add_widget(label)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    json_file='data.json'
    def get_field_data(self, tema,data_key, field, index):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
            nama_data1 = data[tema][data_key][field][index]
            return nama_data1

class quis1(Screen):
    def __init__(self, **kwargs):
        super(quis1, self).__init__(**kwargs)

    def terima_variabel(self, temaa, level, bolen):
        self.tema = temaa
        self.level = level
        self.bolen = bolen

        voice=self.get_field_data(self.tema, self.level, "voice", 0)
        self.voice= SoundLoader.load(voice)
        self.soundButton = SoundLoader.load('sound/button.wav')

        layout1 = BoxLayout(orientation='vertical')
        layout2 = BoxLayout()
        layout3 = BoxLayout(orientation='vertical')
        layout4 = BoxLayout(orientation='vertical', padding=15, spacing=10)
        layout5 = BoxLayout()
    
        self.background_video = Video(
            source="video/quisBG1.mp4",
            state='play',
            options={'eos': 'loop'},
            allow_stretch=True,
            keep_ratio=False
        )
        self.background_video.volume = 0.8

        label = self.get_field_data(self.tema, "label", "label1", 0)
        Label1 = Image(
            source=label
        )

        self.jawaban = self.get_field_data(self.tema, self.level, "jawaban", 0)

        soal = self.get_field_data(self.tema, self.level, "soal", 0)
        self.soal = ClickableImage(
            source=soal
        )
        self.soal.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.soal.bind(on_press=lambda instance: self.guid())

        pilganA = self.get_field_data(self.tema, self.level, "pilgan1", 0)
        self.button1 = ClickableImage(
            source=pilganA,
            size_hint=(1, 2),
        )
        self.button1.bind(on_press=lambda instance: self.quis2(instance, self.tema, self.level, pilganA))
        

        pilganB = self.get_field_data(self.tema, self.level, "pilgan1", 1)
        self.button2 = ClickableImage(
            source=pilganB,
            size_hint=(1, 2),
        )
        self.button2.bind(on_press=lambda instance: self.quis2(instance, self.tema, self.level, pilganB))


        pilganC = self.get_field_data(self.tema, self.level, "pilgan1", 2)
        self.button3 = ClickableImage(
            source=pilganC,
            size_hint=(1, 2),
        )
        self.button3.bind(on_press=lambda instance: self.quis2(instance, self.tema, self.level, pilganC))


        speaker = Image(
            source='images/speaker.png',
            size_hint=(0.25, 1)
        )

        label3 = Label(
        )
        
        colored_label = ColoredLabel(self.tema, self.level, size_hint=(1, 0.1))
        
        layout1.add_widget(colored_label)

        layout2.add_widget(self.soal)

        layout3.add_widget(Label1)
        layout3.add_widget(layout2)

        layout4.add_widget(self.button1)
        layout4.add_widget(self.button2)
        layout4.add_widget(self.button3)
        layout4.add_widget(label3)

        layout1.add_widget(layout3)
        layout1.add_widget(layout4)
        self.add_widget(self.background_video)
        self.add_widget(layout1)
        # return layout1



    def guid(self, *args):
        self.voice.stop()
        self.voice.play()
        Clock.schedule_once(self.anim3, 2.5)
        Clock.schedule_once(self.anim4, 5.5)
        Clock.schedule_once(self.anim5, 5.5)
        Clock.schedule_once(self.anim6, 8.5)
        Clock.schedule_once(self.anim7, 8.5)
        Clock.schedule_once(self.anim8, 11.5)

    def on_leave(self, *args):
        print("stop")
        # self.soundButton.stop()
        self.voice.stop()
        self.background_video.state = 'stop'

    def on_enter(self, *args):
        self.voice.play()
        if self.bolen == 0:
            self.manager.get_screen('splash').backsound
            self.manager.get_screen('splash').backsound.stop()
        elif self.bolen == 1:
            self.manager.get_screen('selebration').backsound
            self.manager.get_screen('selebration').backsound.stop()
        else:
            print("halah")


        self.anim_out = Animation(size_hint=(1, 4), duration=0.2)
        self.anim_in = Animation(size_hint=(1, 2), duration=0.2)
        self.animL_out = Animation(font_size=70, duration=0.2)
        self.animL_in = Animation(font_size=64, duration=0.2)

        
        # Clock.schedule_once(self.anim1, 2)
        # Clock.schedule_once(self.anim2, 4)
        Clock.schedule_once(self.anim3, 2.5)
        Clock.schedule_once(self.anim4, 5.5)
        Clock.schedule_once(self.anim5, 5.5)
        Clock.schedule_once(self.anim6, 8.5)
        Clock.schedule_once(self.anim7, 8.5)
        Clock.schedule_once(self.anim8, 11.5)

    # def anim1(self, *args):
    #     self.animL_out.start(self.soal)
    # def anim2(self, *args):
    #     self.animL_in.start(self.soal)
    def anim3(self, *args):
        self.anim_out.start(self.button1)
    def anim4(self, *args):
        self.anim_in.start(self.button1)
    def anim5(self, *args):
        self.anim_out.start(self.button2)
    def anim6(self, *args):
        self.anim_in.start(self.button2)
    def anim7(self, *args):
        self.anim_out.start(self.button3)
    def anim8(self, *args):
        self.anim_in.start(self.button3)


    def quis2(self, instance, temaa, level, pilgan):
        self.soundButton.play()
        if self.jawaban == pilgan:
            print("benar")
            poin = 100
            self.manager.get_screen('quis2').terima_variabel(temaa, level, poin)
            self.manager.current = 'quis2'
        else:
            print("salah")
            poin = 10
            self.manager.get_screen('quis2').terima_variabel(temaa, level, poin)
            self.manager.current = 'quis2'

    json_file='data.json'
    def get_field_data(self, tema,data_key, field, index):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
            nama_data1 = data[tema][data_key][field][index]
            return nama_data1
        
class ClickableImage(ButtonBehavior, Image):
    def on_pre(self):
        print(1)
# mainApp().run()
