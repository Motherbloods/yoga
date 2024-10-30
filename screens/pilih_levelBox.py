from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.video import Video
from kivy.core.audio import SoundLoader
import json


Window.clearcolor = (255/255, 255/255, 255/255)
Window.size = (360, 640)

class pilih_levelBox(Screen):
    def __init__(self, **kwargs):
        super(pilih_levelBox, self).__init__(**kwargs)

    def terima_tema(self, variabel, bolen):
        self.tema = variabel
        self.bolen = bolen
    
        self.soundButton = SoundLoader.load('sound/button.wav')

        layout1 = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(spacing=10,padding=15)
        layout3 = BoxLayout(spacing=10,padding=15)
        layout4 = BoxLayout(spacing=10,padding=15)

        self.background_video = Video(
            source="video/background.mp4",
            state='play',
            options={'eos': 'loop'},
            allow_stretch=True,
            keep_ratio=False
        )

        self.back = ClickableImage(
            source ="images/back.png",
            size_hint=(0.15, 0.4,)
        )
        self.back.bind(on_press=self.kembali)

        self.title = Image(
            source='images/title_pilih_level.png',
        )
        self.title.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        tombol1 = self.get_field_data(self.tema,'level1','tombol',0)
        status1 = self.get_field_data(self.tema,'level1','status',0)
        self.button1 = ClickableImage(
            source=tombol1,
        )
        self.button1.bind(on_press=lambda instance: self.quis1(instance, self.tema, "level1", status1))


        tombol2 = self.get_field_data(self.tema,'level2','tombol',0)
        status2 = self.get_field_data(self.tema,'level2','status',0)
        self.button2 = ClickableImage(
            source=tombol2
        )
        self.button2.bind(on_press=lambda instance: self.quis1(instance, self.tema, "level2", status2))
        

        tombol3 = self.get_field_data(self.tema,'level3','tombol',0)
        status3 = self.get_field_data(self.tema,'level3','status',0)
        self.button3 = ClickableImage(
            source=tombol3
        )
        self.button3.bind(on_press=lambda instance: self.quis1(instance, self.tema, "level3", status3))


        tombol4 = self.get_field_data(self.tema,'level4','tombol',0)
        status4 = self.get_field_data(self.tema,'level4','status',0)
        self.button4 = ClickableImage(
            source=tombol4
        )
        self.button4.bind(on_press=lambda instance: self.quis1(instance, self.tema, "level4", status4))


        tombol5 = self.get_field_data(self.tema,'level5','tombol',0)
        status5 = self.get_field_data(self.tema,'level5','status',0)
        self.button5 = ClickableImage(
            source=tombol5
        )
        self.button5.bind(on_press=lambda instance: self.quis1(instance, self.tema, "level5", status5))


        tombol6 = self.get_field_data(self.tema,'level6','tombol',0)
        status6 = self.get_field_data(self.tema,'level6','status',0)
        self.button6 = ClickableImage(
            source=tombol6
        )
        self.button6.bind(on_press=lambda instance: self.quis1(instance, self.tema, "level6", status6))


        tombol7 = self.get_field_data(self.tema,'level7','tombol',0)
        status7 = self.get_field_data(self.tema,'level7','status',0)
        self.button7 = ClickableImage(
            source=tombol7
        )
        self.button7.bind(on_press=lambda instance: self.quis1(instance, self.tema, "level7", status7))


        tombol8 = self.get_field_data(self.tema,'level8','tombol',0)
        status8 = self.get_field_data(self.tema,'level8','status',0)
        self.button8 = ClickableImage(
            source=tombol8
        )
        self.button8.bind(on_press=lambda instance: self.quis1(instance, self.tema, "level8", status8))


        tombol9 = self.get_field_data(self.tema,'level9','tombol',0)
        status9 = self.get_field_data(self.tema,'level9','status',0)
        self.button9 = ClickableImage(
            source=tombol9
        )
        self.button9.bind(on_press=lambda instance: self.quis1(instance, self.tema, "level9", status9))


        label=Label(
            text=''
        )

        layout1.add_widget(self.back)
        layout1.add_widget(self.title)
        layout2.add_widget(self.button1)
        layout2.add_widget(self.button2)
        layout2.add_widget(self.button3)
        layout3.add_widget(self.button4)
        layout3.add_widget(self.button5)
        layout3.add_widget(self.button6)
        layout4.add_widget(self.button7)
        layout4.add_widget(self.button8)
        layout4.add_widget(self.button9)
        
        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        layout1.add_widget(layout4)
        layout1.add_widget(label)
        self.add_widget(self.background_video)
        self.add_widget(layout1)
        # return layout1

    def on_enter(self, *args):
        self.background_video.state = 'play'

    def on_leave(self, *args):
        print("stop")
        # self.soundButton.stop()
        self.background_video.state = 'stop'

    def kembali(self, instance):
        self.soundButton.play()
        print("teessss")
        self.manager.get_screen('pilih_tema').terima_variabel("play", self.bolen)
        self.manager.current = 'pilih_tema'

    def quis1(self, instance, temaa, level, status):
        self.soundButton.play()
        print("teessss")
        if status == "lock":
            print("lock")
        else:
            self.manager.get_screen('quis1').terima_variabel(temaa, level, self.bolen)
            self.manager.current = 'quis1'

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
