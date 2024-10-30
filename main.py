from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from screens.homeBox import homeBox
from screens.pilih_levelBox import pilih_levelBox
from screens.pilih_temaBox import pilih_tema
from screens.quisBox1 import quis1
from screens.quisBox2 import quis2
from screens.quisBox3 import quis3
from screens.quisBox4 import quis4
from screens.quisBox5 import quis5
from screens.true_falseBox import true_false
from screens.splash import splash
from screens.selebration import selebration
from screens.tutor_number import tutor_number
from screens.tutor_fruits import tutor_fruits
from screens.tutor_animal import tutor_animal

class MainApp(App):
    def build(self):
       
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(splash(name='splash'))
        sm.add_widget(homeBox(name='homeBox'))
        sm.add_widget(pilih_tema(name='pilih_tema'))
        sm.add_widget(pilih_levelBox(name='pilih_levelBox'))
        sm.add_widget(quis1(name='quis1'))
        sm.add_widget(quis2(name='quis2'))
        sm.add_widget(quis3(name='quis3'))
        sm.add_widget(quis4(name='quis4'))
        sm.add_widget(quis5(name='quis5'))
        sm.add_widget(selebration(name='selebration'))
        sm.add_widget(tutor_number(name='tutor_number'))
        sm.add_widget(tutor_fruits(name='tutor_fruits'))
        sm.add_widget(tutor_animal(name='tutor_animal'))
        sm.add_widget(true_false(name='true_valse'))
        return sm

if __name__ == '__main__':
    MainApp().run()
