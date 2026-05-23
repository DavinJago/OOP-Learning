## Summary Inheritance Slides
### Lecturer skipped the 4th slides, Implementation on class of program

### Inheritance Concept
* we can use the class that we make earlier, and inherit all skills from past class. 
* different form from memory and reuse 
* you write once, use it many times
* child class had the past class (parent)

### Advantage 
* Represent rl relation
* Reusable code
* transitive, it means if B inherit from A, all the subclass from B automatically inherit from A    
* Inheritance offers simple structure and ez to understand
* Low cost development and maintanance

### Inheritance Types
Syntax :
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}

> Code -> Inheritance.py

### Super Function
* super() is a default function return object from parents class
* making possibly to acsess method and attribute from child class

> Code -> Inheritance.py Code II

### Single Inherit
* enabling child class inherit property from single parent.
* possibly reuse of code and adding new features.

> Code -> Code III

### Multiple Inherit
* when a class can inherit more than 1 
* all the features inherit into child class

> Code -> Code IV

### Multilevel Inherit
* all features from child and parents inherit to the new grandchild class
* similar to relations child to grandparents.

### illustation :
A -> B -> C 
A Base class, B Intermediatory

> Code -> Code V    