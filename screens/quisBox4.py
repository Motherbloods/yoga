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
import json


Window.clearcolor = (255/255, 255/255, 255/255)
Window.size = (360, 640)

class ColoredLabel(BoxLayout):
    def __init__(self, tema, level, **kwargs):
        super(ColoredLabel, self).__init__(**kwargs)
        self.tema = tema
        self.level = level

            # Add background color
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

class quis4(Screen):
    def __init__(self, **kwargs):
        super(quis4, self).__init__(**kwargs)

    def terima_variabel(self, temaa, level, poin):
        self.tema = temaa
        self.level = level
        self.poin = poin

        layout1 = BoxLayout(orientation='vertical')
        layout2 = BoxLayout()
        layout3 = BoxLayout(orientation='vertical')
        layout4 = BoxLayout(orientation='vertical', padding=15, spacing=10)
        layout5 = BoxLayout()

        Label1 = Label(
            text="apakah arti dari",
            color=(0, 0, 0),
            size_hint=(1, 1),
            font_size=24,
        )

        self.jawaban = self.get_field_data(self.tema, self.level, "jawaban", 1)

        soal = self.get_field_data(self.tema, self.level, "soal", 1)
        Label2 = Label(
            text=f"{soal}",
            color=(187/255, 183/255, 84/255),
            size_hint=(1, 1),
            font_size=64,
        )

        pilganA = self.get_field_data(self.tema, self.level, "pilgan2", 0)
        self.button1 = ClickableImage(
            source=pilganA,
            size_hint=(1, 2),
        )
        self.button1.bind(on_press=lambda instance: self.quis3(instance, self.tema, self.level, pilganA))


        pilganB = self.get_field_data(self.tema, self.level, "pilgan2", 1)
        self.button2 = ClickableImage(
            source=pilganB,
            size_hint=(1, 2),
        )
        self.button2.bind(on_press=lambda instance: self.quis3(instance, self.tema, self.level, pilganB))


        pilganC = self.get_field_data(self.tema, self.level, "pilgan2", 2)
        self.button3 = ClickableImage(
            source=pilganC,
            size_hint=(1, 2),
        )
        self.button3.bind(on_press=lambda instance: self.quis3(instance, self.tema, self.level, pilganC))


        pilganD = self.get_field_data(self.tema, self.level, "pilgan2", 3)
        self.button4 = ClickableImage(
            source=pilganD,
            size_hint=(1, 2),
        )
        self.button4.bind(on_press=lambda instance: self.quis3(instance, self.tema, self.level, pilganD))


        speaker = Image(
            source='images/speaker.png',
            size_hint=(0.25, 1)
        )

        label3 = Label(
        )
        
        colored_label = ColoredLabel(self.tema, self.level, size_hint=(1, 0.1))
        
        layout1.add_widget(colored_label)

        layout2.add_widget(Label2)
        layout2.add_widget(speaker)

        layout3.add_widget(Label1)
        layout3.add_widget(layout2)

        layout4.add_widget(self.button1)
        layout4.add_widget(self.button2)
        layout4.add_widget(self.button3)
        layout4.add_widget(self.button4)
        layout4.add_widget(label3)

        layout1.add_widget(layout3)
        layout1.add_widget(layout4)
        self.add_widget(layout1)
        # return layout1

    def quis3(self, instance, temaa, level, pilgan):
        if self.jawaban == pilgan:
            print("benar")
            poin = self.poin + 200
            self.manager.get_screen('quis5').terima_variabel(temaa, level, poin)
            self.manager.current = 'quis5'
        else:
            print("salah")
            poin = self.poin + 50
            self.manager.get_screen('quis5').terima_variabel(temaa, level, poin)
            self.manager.current = 'quis5'

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
