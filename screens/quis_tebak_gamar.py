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


Window.clearcolor = (255/255, 255/255, 255/255)
Window.size = (360, 640)

class ColoredLabel(BoxLayout):
    def __init__(self, **kwargs):
        super(ColoredLabel, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Add background color
        with self.canvas.before:
            Color(108/255, 56/255, 117/255, 1)  # Set the background color (RGBA)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        label = Label(
            text="Animal Level 1", 
            font_size=20, 
            halign='center',
            size_hint=(1, 1)
        )
        label.color = (1, 1, 1, 1)  # Set text color to white
        self.add_widget(label)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class quis2(Screen):
    def __init__(self, **kwargs):
        super(quis2, self).__init__(**kwargs)
        layout1 = BoxLayout(orientation='vertical')
        layout2 = BoxLayout()
        layout3 = BoxLayout(orientation='vertical')
        layout4 = BoxLayout(orientation='vertical', padding=15, spacing=10)
        layout5 = BoxLayout()

        Label1 =Image(
            source ="images/tebak-gambar/tiger.png",
            size_hint=(1.04, 2),
        )

        Label2 = Label(
            text="Monkey",
            color=(187/255, 183/255, 84/255),
            size_hint=(1, 1),
            font_size=64,
        )

        button1 = ClickableImage(
            source='images/quis-pilgan/gajah.png',
            size_hint=(1, 2),
        )

        button2 = ClickableImage(
            source='images/quis-pilgan/burung.png',
            size_hint=(1, 2),
        )

        button3 = ClickableImage(
            source='images/quis-pilgan/monyet.png',
            size_hint=(1, 2),
        )

        button4 = ClickableImage(
            source='images/quis-pilgan/kambing.png',
            size_hint=(1, 2),
        )

        speaker = Image(
            source='images/speaker.png',
            size_hint=(0.25, 1)
        )

        label3 = Label(
            text='dfgh'
        )
        
        colored_label = ColoredLabel(size_hint=(1, 0.1))  # Membuat label dengan background warna
        
        layout1.add_widget(colored_label)

        layout2.add_widget(Label2)
        layout2.add_widget(speaker)

        layout3.add_widget(Label1)
        # layout3.add_widget(layout2)

        layout4.add_widget(button1)
        layout4.add_widget(button2)
        layout4.add_widget(button3)
        layout4.add_widget(button4)
        layout4.add_widget(label3)

        layout1.add_widget(layout3)
        layout1.add_widget(layout4)
        self.add_widget(layout1)
        # return layout1

class ClickableImage(ButtonBehavior, Image):
    def on_pre(self):
        print(1)
# mainApp().run()
