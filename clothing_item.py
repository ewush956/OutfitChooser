class ClothingItem:
    def __init__(self, item_id: str, category: str, is_clean: bool):
        self.item_id = item_id
        self.category = category
        #4 types will by SHIRT(0), PANTS(1), JACKET(2), SHOES(3)
        self.is_clean = is_clean

    def clean(self):
        self.is_clean = True
    def __str__(self) -> str:
        return f'{self.item_id} {self.category} {self.is_clean}'
    
    

        
    

    

    
