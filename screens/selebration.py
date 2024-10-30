from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.video import Video
from kivy.graphics import Color, Rectangle
import json

# Window.clearcolor = (218/255, 218/255, 218/255)
# Window.clearcolor = (0, 0, 0)
Window.size = (360, 640)

class selebration(Screen):
    def __init__(self, **kwargs):
        super(selebration, self).__init__(**kwargs)

    
    def terima_variabel(self, temaa, level, poin):
        self.tema = temaa
        self.level = level
        self.poin = poin

        self.soundButton = SoundLoader.load('sound/button.wav')
        self.backsound = SoundLoader.load('sound/backsound.mp3')

        print(self.poin)
        poin = self.get_field_data(self.tema, self.level, "poin", 0)
        self.open_level()
        if self.poin in range(0, 149):
            self.vidio = 'video/bintang1.mp4'
            if poin <= self.poin:
                print("bintang1")
                self.update_field_by_index(self.tema, self.level, "tombol", 0, "1.png")
                self.update_poin(self.tema, self.level, "poin", 0, self.poin)
        elif self.poin in range(150, 202):
            self.vidio = 'video/bintang2.mp4'
            if poin <= self.poin:
                print("bintang2")
                self.update_field_by_index(self.tema, self.level, "tombol", 0, "2.png")
                self.update_poin(self.tema, self.level, "poin", 0, self.poin)
        elif self.poin in range(210, 310):
            self.vidio = 'video/bintang3.mp4'
            if poin <= self.poin:
                print("bintang3")
                self.update_field_by_index(self.tema, self.level, "tombol", 0, "3.png")
                self.update_poin(self.tema, self.level, "poin", 0, self.poin)

        layout = BoxLayout(orientation='vertical')

        with self.canvas.before:
            Color(218/255, 218/255, 218/255, 1) 
            self.rect = Rectangle(size=Window.size)


        video = Video(
            source=self.vidio, 
            state='play',  
            allow_stretch=True 
        )

        button = ClickableImage(
            source='images/menu.png',
            size_hint=(0.8, 0.8)
        )
        button.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        button.bind(on_press=lambda instance: self.pilih_level(instance, self.tema))

        

        layout.add_widget(video)
        layout.add_widget(button)

        self.add_widget(layout)

        Window.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = Window.size

    def open_level(self):
        level = self.get_field_data(self.tema, self.level, "open", 0)
        poin1 = self.get_field_data(self.tema, level, "poin", 0)
        if poin1 > 0:
            print("none")
        else:
            self.update_field_by_index(self.tema, level, "tombol", 0, "0.png")
            self.update_poin(self.tema, level, "status", 0, "open")
            print("open level")

    def pilih_level(self, instance, tema):
        print("teessss")
        self.backsound.play()
        self.soundButton.play()
        variabel = tema
        bolen = 1
        self.manager.get_screen('pilih_levelBox').terima_tema(variabel, bolen)
        self.manager.current = 'pilih_levelBox'

    json_file='data.json'
    def update_field_by_index(self, tema ,data_key, field ,index, add):
        # Membaca file JSON
        with open(self.json_file, 'r') as file:
            data = json.load(file)

            data1=data[tema][data_key][field][index]
            data1=data1[:-5]
            new_data1=f"{data1}{add}"
    
    # Memodifikasi nama pada indeks yang ditentukan
        if 0 <= index < len(data[tema][data_key][field]):
            data[tema][data_key][field][index] = (new_data1)
        else:
            print("Indeks tidak valid.")
            return

    # Menyimpan kembali perubahan ke file JSON
        with open(self.json_file, 'w') as file:
            json.dump(data, file, indent=1)

    def update_poin(self, tema ,data_key, field ,index, new_data, add=""):
        if add=="":
            new_data1=new_data
        else:
            data1=new_data[:-5]
            new_data1=f"{data1}{add}"

        # Membaca file JSON
        with open(self.json_file, 'r') as file:
            data = json.load(file)
    
    # Memodifikasi nama pada indeks yang ditentukan
        if 0 <= index < len(data[tema][data_key][field]):
            data[tema][data_key][field][index] = (new_data1)
        else:
            print("Indeks tidak valid.")
            return

    # Menyimpan kembali perubahan ke file JSON
        with open(self.json_file, 'w') as file:
            json.dump(data, file, indent=1)

    def get_field_data(self, tema,data_key, field, index):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
            nama_data1 = data[tema][data_key][field][index]
            return nama_data1
    
class ClickableImage(ButtonBehavior, Image):
    def on_pre(self):
       print(1)
