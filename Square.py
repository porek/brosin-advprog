class Square(Rectangle):
    def __init__(self,x,y):
        self.x = x
        self.y = x

    def __str__(self):
        return "Area: %2.f Length: %2.f"
