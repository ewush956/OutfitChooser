from clothing_item import ClothingItem

class Outfit:
    def __init__(self, shirt: ClothingItem, pants: ClothingItem, jacket: ClothingItem, shoes: ClothingItem):
        
        self.shirt = shirt
        self.pants = pants
        self.jacket = jacket
        self.shoes = shoes
    
    def wear(self):
        self.shirts.is_clean = False
        self.pants.is_clean = False

    
    
    