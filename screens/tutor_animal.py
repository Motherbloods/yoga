from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.video import Video

Window.clearcolor = (255/255, 255/255, 255/255)
Window.size = (360, 640)

class tutor_animal(Screen):
    def __init__(self, **kwargs):
        super(tutor_animal, self).__init__(**kwargs)

    def terima_variabel(self, bolen):
        self.bolen = bolen

        layout1 = BoxLayout(orientation='vertical')
        layout2 = BoxLayout(orientation='vertical', size_hint_y=4, padding=10, spacing=10)
        layout2.bind(minimum_height=layout2.setter('height'))
        layout3 = BoxLayout(spacing=10)
        layout4 = BoxLayout(spacing=10)
        layout5 = BoxLayout(spacing=10)
        layout6 = BoxLayout(spacing=10)
        layout7 = BoxLayout(spacing=10)
        layout8 = BoxLayout(spacing=10)
        layout9 = BoxLayout(spacing=10)
        layout10 = BoxLayout(spacing=10)
        layout11 = BoxLayout(spacing=10)
        layout12 = BoxLayout(spacing=10)
        layout13 = BoxLayout(spacing=10)
        layout14 = BoxLayout(spacing=10)
        layout15 = BoxLayout(spacing=10)
        scroll_view = ScrollView()

        self.background_video = Video(
            source="video/background.mp4",  # Path ke video latar belakang
            state='play',  # Memulai video secara otomatis
            options={'eos': 'loop'},  # Mengatur agar video diputar terus-menerus (loop)
            allow_stretch=True,
            keep_ratio=False
        )

        self.soundButton = SoundLoader.load('sound/button.wav')

        self.back = ClickableImage(
            source ="images/back.png",
            size_hint=(0.1, 0.1,)
        )
        self.back.bind(on_press=self.kembali)

        title = Image(
            source='images/title tutor animal.png',
            size_hint=(0.6, 0.15)
        )
        title.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.images1 = ClickableImage(source='images/tutorial-animal/cat.png')
        self.images1.bind(on_press=lambda instance: self.anim(elemen=self.images1))
        self.images1.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/cat.MP3'))

        self.images2 = ClickableImage(source='images/tutorial-animal/dog.png')
        self.images2.bind(on_press=lambda instance: self.anim(elemen=self.images2))
        self.images2.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/dog.MP3'))

        self.images3 = ClickableImage(source='images/tutorial-animal/chameleon.png')
        self.images3.bind(on_press=lambda instance: self.anim(elemen=self.images3))
        self.images3.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/chameleon.MP3'))

        self.images4 = ClickableImage(source='images/tutorial-animal/crocodile.png')
        self.images4.bind(on_press=lambda instance: self.anim(elemen=self.images4))
        self.images4.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/crocodile.MP3'))

        self.images5 = ClickableImage(source='images/tutorial-animal/duck.png')
        self.images5.bind(on_press=lambda instance: self.anim(elemen=self.images5))
        self.images5.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/duck.MP3'))

        self.images6 = ClickableImage(source='images/tutorial-animal/pigeon.png')
        self.images6.bind(on_press=lambda instance: self.anim(elemen=self.images6))
        self.images6.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/pigeon.MP3'))

        self.images7 = ClickableImage(source='images/tutorial-animal/butterfly.png')
        self.images7.bind(on_press=lambda instance: self.anim(elemen=self.images7))
        self.images7.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/butterfly.MP3'))

        self.images8 = ClickableImage(source='images/tutorial-animal/mouse.png')
        self.images8.bind(on_press=lambda instance: self.anim(elemen=self.images8))
        self.images8.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/mouse.MP3'))

        self.images9 = ClickableImage(source='images/tutorial-animal/rhinoceros.png')
        self.images9.bind(on_press=lambda instance: self.anim(elemen=self.images9))
        self.images9.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/rhinoceros.MP3'))

        self.images10 = ClickableImage(source='images/tutorial-animal/hedgehog.png')
        self.images10.bind(on_press=lambda instance: self.anim(elemen=self.images10))
        self.images10.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/hedgehog.MP3'))

        self.images11 = ClickableImage(source='images/tutorial-animal/monkey.png')
        self.images11.bind(on_press=lambda instance: self.anim(elemen=self.images11))
        self.images11.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/monkey.MP3'))

        self.images12 = ClickableImage(source='images/tutorial-animal/panda.png')
        self.images12.bind(on_press=lambda instance: self.anim(elemen=self.images12))
        self.images12.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/panda.MP3'))

        self.images13 = ClickableImage(source='images/tutorial-animal/bear.png')
        self.images13.bind(on_press=lambda instance: self.anim(elemen=self.images13))
        self.images13.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/bear.MP3'))

        self.images14 = ClickableImage(source='images/tutorial-animal/pig.png')
        self.images14.bind(on_press=lambda instance: self.anim(elemen=self.images14))
        self.images14.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/pig.MP3'))

        self.images15 = ClickableImage(source='images/tutorial-animal/sheep.png')
        self.images15.bind(on_press=lambda instance: self.anim(elemen=self.images15))
        self.images15.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/sheep.MP3'))

        self.images16 = ClickableImage(source='images/tutorial-animal/horse.png')
        self.images16.bind(on_press=lambda instance: self.anim(elemen=self.images16))
        self.images16.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/horse.MP3'))

        self.images17 = ClickableImage(source='images/tutorial-animal/deer.png')
        self.images17.bind(on_press=lambda instance: self.anim(elemen=self.images17))
        self.images17.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/deer.MP3'))

        self.images18 = ClickableImage(source='images/tutorial-animal/camel.png')
        self.images18.bind(on_press=lambda instance: self.anim(elemen=self.images18))
        self.images18.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/camel.MP3'))

        self.images19 = ClickableImage(source='images/tutorial-animal/dinosaurs.png')
        self.images19.bind(on_press=lambda instance: self.anim(elemen=self.images19))
        self.images19.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/dinosaurs.MP3'))

        self.images20 = ClickableImage(source='images/tutorial-animal/hawk.png')
        self.images20.bind(on_press=lambda instance: self.anim(elemen=self.images20))
        self.images20.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/hawk.MP3'))

        self.images21 = ClickableImage(source='images/tutorial-animal/cow.png')
        self.images21.bind(on_press=lambda instance: self.anim(elemen=self.images21))
        self.images21.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/cow.MP3'))

        self.images22 = ClickableImage(source='images/tutorial-animal/rabbit.png')
        self.images22.bind(on_press=lambda instance: self.anim(elemen=self.images22))
        self.images22.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/rabbit.MP3'))

        self.images23 = ClickableImage(source='images/tutorial-animal/elephan.png')
        self.images23.bind(on_press=lambda instance: self.anim(elemen=self.images23))
        self.images23.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/elephan.MP3'))

        self.images24 = ClickableImage(source='images/tutorial-animal/tiger.png')
        self.images24.bind(on_press=lambda instance: self.anim(elemen=self.images24))
        self.images24.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/tiger.MP3'))

        self.images25 = ClickableImage(source='images/tutorial-animal/loin.png')
        self.images25.bind(on_press=lambda instance: self.anim(elemen=self.images25))
        self.images25.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/lion.MP3'))

        self.images26 = ClickableImage(source='images/tutorial-animal/giraffale.png')
        self.images26.bind(on_press=lambda instance: self.anim(elemen=self.images26))
        self.images26.bind(on_press=lambda instance: self.play_sound('sound/tutorial-animal/giraffe.MP3'))

        layout3.add_widget(self.images1)
        layout3.add_widget(self.images2)
        layout4.add_widget(self.images3)
        layout4.add_widget(self.images4)
        layout5.add_widget(self.images5)
        layout5.add_widget(self.images6)
        layout6.add_widget(self.images7)
        layout6.add_widget(self.images8)
        layout7.add_widget(self.images9)
        layout7.add_widget(self.images10)
        layout8.add_widget(self.images11)
        layout8.add_widget(self.images12)
        layout9.add_widget(self.images13)
        layout9.add_widget(self.images14)
        layout10.add_widget(self.images15)
        layout10.add_widget(self.images16)
        layout11.add_widget(self.images17)
        layout11.add_widget(self.images18)
        layout12.add_widget(self.images19)
        layout12.add_widget(self.images20)
        layout13.add_widget(self.images21)
        layout13.add_widget(self.images22)
        layout14.add_widget(self.images23)
        layout14.add_widget(self.images24)
        layout15.add_widget(self.images25)
        layout15.add_widget(self.images26)


        layout2.add_widget(layout3)
        layout2.add_widget(layout4)
        layout2.add_widget(layout5)
        layout2.add_widget(layout6)
        layout2.add_widget(layout7)
        layout2.add_widget(layout8)
        layout2.add_widget(layout9)
        layout2.add_widget(layout10)
        layout2.add_widget(layout11)
        layout2.add_widget(layout12)
        layout2.add_widget(layout13)
        layout2.add_widget(layout14)
        layout2.add_widget(layout15)
 
        scroll_view.add_widget(layout2)
        layout1.add_widget(self.back)
        layout1.add_widget(title)
        layout1.add_widget(scroll_view)

        self.add_widget(self.background_video)
        self.add_widget(layout1)

    def anim(self, elemen):
        Clock.schedule_once(lambda dt: self.anim1(elemen), 0)
        Clock.schedule_once(lambda dt: self.anim2(elemen), 1)

    def anim1(self, elemen):
        anim_out = Animation(size_hint=(1, 1.2), duration=0.1)
        anim_out.start(elemen)

    def anim2(self, elemen):
        anim_in = Animation(size_hint=(1, 1), duration=0.1)
        anim_in.start(elemen)

    def play_sound(self, url):
        voice= SoundLoader.load(url)
        voice.volume = 3
        voice.play()

    def on_enter(self, *args):
        self.background_video.state = 'play'
        self.manager.get_screen('splash').backsound
        self.manager.get_screen('splash').backsound.volume = 0.3

    def on_leave(self, *args):
        print("stop")
        # self.soundButton.stop()
        self.background_video.state = 'stop'

    def kembali(self, instance):
        self.soundButton.play()
        print("teessss")
        self.manager.get_screen('pilih_tema').terima_variabel("tutor", self.bolen)
        self.manager.current = 'pilih_tema'
    
class ClickableImage(ButtonBehavior, Image):
    def on_pre(self):
       print(1)

