#using instance class (constructor) better than class attrib
#lecturer requesting instance
#using self for save function

class Laptop:
    def __init__(self, model, processor, brand, color):
        self.model = model
        self.processor = processor
        self.brand = brand
        self.color = color
        self.status = "off" 

    def nyala(self):
        self.status = "on"
        

#