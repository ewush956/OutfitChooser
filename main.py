#from typing import Any
#import datetime

from outfit import Outfit
from clothing_item import ClothingItem
from wardrobe import Wardrobe

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder

class MainScreen(BoxLayout):
    pass
'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        settings_button = Button(text="Settings")
        laundry_button = Button(text="Laundry day")
        edit_wardrobe_button = Button(text="Edit wardrobe")
        choose_new_outfit_button = Button(text="Choose new outfit")

        self.add_widget(settings_button)
        self.add_widget(laundry_button)
        self.add_widget(edit_wardrobe_button)
        self.add_widget(choose_new_outfit_button)
'''


class MainWidget(Widget):
    pass

class clothingApp(App):
    pass
    
if __name__ == "__main__":
    clothingApp().run()
'''
class childApp(GridLayout):

    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Wardrobe"))
        self.wardrobe_name = TextInput(multiline=False)
        self.add_widget(self.wardrobe_name)

        self.press = Button(text="Submit")
        self.press.bind(on_press=self.click_wardrobe)
        self.add_widget(self.press)

        # Seperate column for an outfit object
        self.add_widget(Label(text="Outfit"))
        self.outfit_name = TextInput(multiline=False)
        self.add_widget(self.outfit_name)
        self.outfit_button = Button(text="Edit")
        self.outfit_button.bind(on_press=self.edit_outfit)
        self.add_widget(self.outfit_button)

        # Display weather information and date/time
        self.add_widget(Label(text="Weather"))
        self.weather_info = Label(text="Updating...")
        self.add_widget(self.weather_info)
        self.add_widget(Label(text="Date/Time"))
        self.date_time_label = Label(text=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.add_widget(self.date_time_label)

        # 'Laundry day' button
        self.laundry_button = Button(text="Laundry day")
        self.laundry_button.bind(on_press=self.do_laundry)
        self.add_widget(self.laundry_button)

    def edit_outfit(self, instance):
        # TODO: Implement edit outfit functionality
        pass

    def do_laundry(self, instance):
        # TODO: Implement laundry day functionality
        pass

    def click_wardrobe(self, instance):
        print("Name of wardrobe is: " + self.wardrobe_name.text)

class parentApp(App):
    def build(self):
        return childApp()
    

if __name__ == "__main__":
    parentApp().run()  
'''


