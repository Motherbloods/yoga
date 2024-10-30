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

class true_false(Screen):
    def __init__(self, **kwargs):
        super(true_false, self).__init__(**kwargs)
        layout1 = BoxLayout(orientation='vertical')
        layout2 = BoxLayout()
        layout3 = BoxLayout()
        layout4 = BoxLayout(orientation='vertical')
        layout5 = BoxLayout(orientation='vertical')
        layout6 = BoxLayout()

        Label1 = Label(
            text="apakah benar bahwa",
            color=(0, 0, 0),
            size_hint=(1,0.3),
            font_size=24,
        )

        Label2 = Label(
            text="Chicken",
            color=(187/255, 183/255, 84/255),
            size_hint=(1, 1),
            font_size=70,
        )

        Label3 = Label(
            text="artinya adalah",
            color=(0, 0, 0),
            size_hint=(1,0.3),
            font_size=24,
        )

        Label4 = Label(
            text="Ayam",
            color=(187/255, 183/255, 84/255),
            size_hint=(1,1),
            font_size=70,
        )

        button1=ClickableImage(
            source='images/benar.png',
            size_hint=(1, 1),
        )

        button2=ClickableImage(
            source='images/salah.png',
            size_hint=(1, 1),
        )

        speaker1 = Image(
            source='images/speaker.png',
            size_hint=(0.25, 1)
        )

        speaker2 = Image(
            source='images/speaker.png',
            size_hint=(0.25, 1)
        )

        label=Label(
            size_hint=(0.3, 0.3)
        )


        colored_label = ColoredLabel(size_hint=(1, 0.1))  # Membuat label dengan background warna
        
        layout1.add_widget(colored_label)

        layout2.add_widget(Label2)
        layout2.add_widget(speaker1)

        layout3.add_widget(Label4)
        layout3.add_widget(speaker2)

        layout4.add_widget(Label1)
        layout4.add_widget(layout2)

        layout5.add_widget(Label3)
        layout5.add_widget(layout3)

        layout6.add_widget(button1)
        layout6.add_widget(button2)

        layout1.add_widget(layout4)
        layout1.add_widget(layout5)
        layout1.add_widget(layout6)
        layout1.add_widget(label)

        self.add_widget(layout1)
        # return layout1

class ClickableImage(ButtonBehavior, Image):
    def on_pre(self):
        print(1)
    
# mainApp().run()
