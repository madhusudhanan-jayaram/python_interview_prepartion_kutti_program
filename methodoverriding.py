class test:
    def method1(self):
        print("This is method 1")
    
    def multiple_args( self, *args, **kwargs):
        print("This is method 2 with multiple arguments: ", args)
        print("Keyword arguments: ", kwargs)

if __name__ == "__main__":
    t = test()
    t.method1()
    t.multiple_args(1, 2, 3, "hello", [1, 2, 3], key1="value1", key2="value2")