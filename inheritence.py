class parent:
    def __init__(self):
        print("This is the parent class")

class child(parent):
    def __init__(self):
        super().__init__()
        print("This is the child class")    

if __name__ == "__main__":
    c = child()
    