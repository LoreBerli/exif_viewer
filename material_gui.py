from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.image import Image
import State
import im_model
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivy.uix.scatter import Scatter
from kivy.uix.modalview import ModalView
from kivymd.filemanager import MDFileManager
import kivymd.toast
from kivy.properties import StringProperty
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbars import Snackbar
from kivymd.theming import ThemeManager
from kivy.core.window import Window
from kivymd.pickers import MDTimePicker

main_widget_kv = '''
#:import MDToolbar kivymd.toolbar.MDToolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.cards.MDCard
#:import MDSeparator kivymd.cards.MDSeparator
#:import MDDropdownMenu kivymd.menus.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.imagelists.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.pickers.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem
#:import win kivy.core.window

NavigationLayout:
    id: nav_layout
    MDNavigationDrawer:
        id: nav_drawer
        NavigationDrawerToolbar:
            title: "Navigation Drawer"
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "img"
            on_release: app.root.ids.scr_mngr.current = 'img'
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "data"
            on_release: app.root.ids.scr_mngr.current = 'data'

        
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            id: toolbar
            title: 'EXIF Viewer'
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            background_hue: '500'
            left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
            right_action_items: [['dots-vertical', lambda x: app.root.toggle_nav_drawer()]]
        ScreenManager:
            id: scr_mngr
            
            Screen:
                name: 'img'

                        
                MDFloatingActionButton:
                    id:                    float_act_btn
                    icon:                'plus'
                    opposite_colors:    False
                    elevation_normal:    8
                    
                    pos_hint:            {'center_x': 0.9, 'center_y': 0.1}
                    on_press:  app.file_manager_open()
                
                MDFloatingActionButton:
                    id:                    rot_act_btn
                    icon:                'rotate-left'
                    opposite_colors:    False
                    elevation_normal:    8
                    
                    pos_hint:            {'center_x': 0.7, 'center_y': 0.1}
                    on_press:  imagde.rota() 
                            
                FloatLayout:

                    View_pic: 
                        id:imagde         
                        size: self.parent.size
                        source:'photo_2018-10-10_18-05-50.jpg'



                
            Screen:
                name: 'file manager'
            
                MDRaisedButton:
                    size_hint: None, None
                    size: 3 * dp(48), dp(48)
                    text: 'Open files manager'
                    opposite_colors: True
                    pos_hint: {'center_x': .3, 'center_y': .5}
                    on_release: app.file_manager_open()
                    

                    
            Screen:
                name: 'data'           
                BoxLayout:
                    orientation: 'horizontal'
                    padding:10
                    BoxLayout:
                        size_hint: 0.4,0.4

                        pos_hint: {'center_x': 0.3, 'center_y': 0.5}     
                        Image:
                            id:image
                            source:'autoencoder.png'
                    BoxLayout:
                        padding:10
                        orientation: 'vertical'
                        ScrollView:
                            size_hint: 1.0, 0.9
                            do_scroll_x: False
        
                            MDList:
                                id: ml
        
                                OneLineListItem:
                                    text: "diahane"
                                OneLineListItem:
                                    text: "diahane"
                                OneLineListItem:
                                    text: "diahane"
                                        
                                OneLineListItem:
                                    text: "diahane"
                                OneLineListItem:
                                    text: "diahane"
                                OneLineListItem:
                                    text: "diahane"
                                OneLineListItem:
                                    text: "diahane"
                                OneLineListItem:
                                    text: "diahane"
                                OneLineListItem:
                                    text: "diahane"
                        MDFloatingActionButton:
                            size_hint: None, None
                            pos_hint: {'center_x': 0.9, 'center_y': 0.1}     
                            id:                    float_act_btn2
                            icon:                'plus'
                            opposite_colors:    False
                            elevation_normal:    8
                            

                            on_press:  app.file_manager_open()
<View_pic>:
    auto_bring_to_front:False
    do_scale: False
    do_rotation:False
    do_translation:False
    

    size_hint: None, None
    
    Image:
        id: imag
        on_size: self.center = win.Window.center

        source : root.source
        size: root.size[0]/2.0,root.size[0]/2.0
        keep_ratio: True
        allow_stretch: True
        canvas.before:
            PushMatrix
            Rotate:
                angle: root.angle
                axis: 0, 0, 1
                origin: self.center
        canvas.after:
            PopMatrix
        

    
                    
'''

def toast(text):
    # FIXME: crash with Python3.
    try:
        from kivymd.toast import toast
    except TypeError:
        from kivymd.toast.kivytoast import toast
    toast(text)

class KitchenSink(App):
    theme_cls = ThemeManager()
    previous_date = ObjectProperty()
    title = "KivyMD Kitchen Sink"


    menu_items = [
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
        {'viewclass': 'MDMenuItem',
         'text': 'Example item'},
    ]

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        self.theme_cls.accent_palette='Indigo'
        self.manager=None
        self.state = State.State()
        self.im = self.state.current_img
        keyboard = Window.request_keyboard(self._keyboard_released, self.root)
        keyboard.bind(on_key_down=self._keyboard_on_key_down, on_key_up=self._keyboard_released)

        self.bottom_navigation_remove_mobile(main_widget)
        toast("Click on the + botton to open a image")
        return main_widget

    def _keyboard_released(self, window, keycode):
        pass

    def _keyboard_on_key_down(self, window, keycode, text, super):
        if  keycode[1] == 'r':
            self.root.ids['imagde'].rota()
        if  keycode[1] == 'left':
            self.state.roll(1)
            self.change_image(self.state.current_img.path)
        if  keycode[1] == 'right':
            self.state.roll(-1)
            self.change_image(self.state.current_img.path)


    def bottom_navigation_remove_mobile(self, widget):
        # Removes some items from bottom-navigation demo when on mobile
        if DEVICE_TYPE == 'mobile':
            widget.ids.bottom_navigation_demo.remove_widget(widget.ids.bottom_navigation_desktop_2)
        if DEVICE_TYPE == 'mobile' or DEVICE_TYPE == 'tablet':
            widget.ids.bottom_navigation_demo.remove_widget(widget.ids.bottom_navigation_desktop_1)


    def change_image(self,path):
        self.state.change_current(path)
        self.root.ids['image'].source = self.state.current_img.path
        self.root.ids['imagde'].source = self.state.current_img.path
        self.state.must_update = True
        self.fill_exif()
        toast(path)

    def file_manager_open(self):
        import os
        if not self.manager:
            self.manager = ModalView(size_hint=(1, 1), auto_dismiss=False)
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager, select_path=self.select_path,ext=['.jpg','.jpeg'])
            self.manager.add_widget(self.file_manager)
            self.file_manager.show(os.getcwd())  # output manager to the screen
        self.state.cwd=self.file_manager.current_path+"/"
        self.manager_open = True
        self.manager.open()

    def select_path(self, path):
        self.change_image(path)
        self.exit_manager()
        self.root.ids.scr_mngr.current = 'data'




    def fill_exif(self):
        img=self.state.current_img
        dt=img.exif
        self.root.ids['ml'].clear_widgets()
        for v in dt:
            self.root.ids['ml'].add_widget(kivymd.list.ThreeLineRightIconListItem(text=v,secondary_text=str(dt[v])))
    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""

        self.manager.dismiss()
        self.manager_open = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        """Called when buttons are pressed on the mobile device.."""

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def set_error_message(self, *args):
        if len(self.root.ids.text_field_error.text) == 2:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

    def on_pause(self):
        return True

    def on_stop(self):
        pass


class AvatarSampleWidget(ILeftBody, Image):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass

class View_pic(Scatter):
    source = StringProperty(None)
    angle = NumericProperty(0)
    def __init__(self,**kwargs):
        super(View_pic,self).__init__()
        Scatter.auto_bring_to_front=False
    def rota(self):
        self.angle+=30
        print(self.angle)

if __name__ == '__main__':
    KitchenSink().run()
