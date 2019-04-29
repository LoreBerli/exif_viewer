from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.core.window import Window
# Define new widgets via *inheritance*.
from kivy.clock import Clock
from PIL import Image
from PIL import ExifTags
from time import sleep
import actions
import os
import im_model
import State

class exif_vis(App):

    def my_callback(self,dt):
        #self.state.roll()
        if self.state.must_update:
            self.state.must_update=False
            self.base.ids['labels'].rows = len(self.state.current_img.exif)
            self.base.ids['image'].source = self.state.current_img.path
            self.base.ids['prev'].source = self.state.other_img.path
            self.base.ids['labels'].clear_widgets()
            dt=self.state.current_img.exif
            for k in dt:
                if(k in self.state.get_diff()):
                    col=[1,0,0,1]
                else:
                    col=[1,1,1,1]
                lab=str(k)+" :"+str(dt[k])
                lab=lab.replace("\n"," ")
                print(lab)
                self.base.ids['labels'].add_widget(Label(text=lab,halign='left',font_size=9,line_height=0.9,color=col))




    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        self.state=State.State()

        base=Builder.load_file('layout.kv')
        base.ids['labels'].rows=len(self.state.current_img.exif)
        base.ids['image'].source=self.state.current_img.path
        dt=self.state.current_img.exif
        for k in dt:

            base.ids['labels'].add_widget(Label(text=str(k)+" :"+str(dt[k]),halign='left',font_size=9,text_size=(300,None),line_height=0.9))
        self.base=base
        self.button_builder()
        event = Clock.schedule_interval(self.my_callback, 0.1)
        return base

    def button_builder(self):
        for b in range(2):
            self.base.ids['buts'].add_widget(ButtonModel(self.state,actions.forward))
        for b in range(2):
            self.base.ids['buts'].add_widget(ButtonModel(self.state,actions.back))



class ButtonModel(Button):
    def __init__(self,state,clb,**kwargs):
        super(Button,self).__init__(**kwargs)
        self.ste=state
        self.clb=clb
    def on_press(self):
        self.clb(self.ste)



# Instantiate useful stuff.
app = exif_vis()
app.run()