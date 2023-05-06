from outfit import Outfit
from clothing_item import ClothingItem
#will need weather data 

class Wardrobe():
    def __init__(self, name: str):
        self.name = name
        self.shirts = []
        self.pants = []
        self.jackets = ["void_jacket"]
        self.shoes = []

    def build_wardrobe():
        selecting = True
        #while (selecting):
            #in selection screen there will be a button for togelling selecting to false

            #upload image
            #if shirt select long or short sleeve
            #elif pants select are these shorts?
        
        return
    def make_outfit(self):

        return
        
        #TODO using the clothes from the parent class, pick a shirt, pants, shoes, and jacket(optional)
        #     create using acceptable color combinations which are determined from the current weather.
        #     this needs to be integrated with the OpenWeather API
    def do_laundry(self):
        #TODO set is_clean in every clothing item in the wardrobe to true. (not including shoes)
        
        for clothing_type in ['SHIRT', 'PANTS', 'JACKET']:
            for item in getattr(self, clothing_type):
                if isinstance(item, ClothingItem):
                    item.is_clean = True
    def get_user_preferences(self):
        '''
        for 
        '''
        #return a list of Outfit objects
        return
    def choose_outfit(self):
        #get_user_preferences MUST be called before calling choose_outfit
        return
        #return an Outfit object chosen from the user's preferences


    def __str__(self):
        return f"{self.name} {self.shirts} {self.pants} {self.jackets} {self.shoes}"
