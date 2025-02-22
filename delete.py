class Parent:
 
    def show(self):
        print(self.child_attr)  # ❌ This will fail

class Child(Parent):
    def __init__(self):
        self.child_attr = "Hello"  # ✅ This sets child_attr in the instance

c = Child()
c.show()