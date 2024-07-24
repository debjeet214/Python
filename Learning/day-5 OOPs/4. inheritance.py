# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

```
Types of inheritance:
Single inheritance
Multiple inheritance
Multilevel inheritance
Hierarchical Inheritance
Hybrid Inheritance
```

class Parent:
    def func1(self):
        print("This function is in parent class.")
 
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
 
object = Child()
object.func1()
object.func2()
