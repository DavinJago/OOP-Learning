## Polymorphism, Abstract class, interface 
### Last slides, next ride to the mastering the python

### Super() Python
* Super is a function
* super simply allow us to acsess parent's method (function)
* called in child class, we can call
1. Super Constructor
2. Super Variable
3. Super Method

[Examples -> Code I](https://github.com/DavinJago/OOP-Learning/blob/60c09d61cd3ac0c936d21e7c5f36873ee84bf1ed/e%20polymorphism/polymorph.py#L1-L12)

### Continue from Super
* when super and child had the same method, same variable, some scenario we want to use this 2
* with this scenario/example, we can call super variable

[Examples -> Code II](https://github.com/DavinJago/OOP-Learning/blob/dc196457db096bfbbe0c1cb48a57ca5eeee3d5d2/e%20polymorphism/polymorph.py#L16-L26)

### Polymorphism
* Poly -> A lot, Morph -> shapes
* "one shape in many forms"
* Example 1 like Businessman, he can be dad, postman, negotiate, delivery man, etc.
* Example 2 Animal can speak(); but different sound, cat -> meow, dog -> woof, cow -> moo.

### Overiding
* Features that allow modify parent's method from child-class
> example: animal can speak, but cat had spesific meow sound.
* when a method from subclass had the same name, attrib, and subtype. method in subclass actually are overriding that method in super class.
> Example
    Animal -> data1, move(), eat()
    Dog -> data2, move(), bark()
    *atp move in many animal are different in dog's way

[Examples -> Code IV](https://github.com/DavinJago/OOP-Learning/blob/2c6ce57311b9af6223b3a3ff5f691b63a8c8f759/e%20polymorphism/polymorph.py#L45-L58)

### Overloading
* Allow 1 method had the same name, but with different signature. 
* signature can be different depend on parameter amount
> Example (From Google)
    int plus(a + b)
    int plus(a + b + c)

### Overloading #Python
* we can use same operator or method for different purpose
* there are 3 types of overload

### Overloading Operator
* we use same operator for diff purpose
* '+' can be use at arithmatic and string merge
* '*' multiply can be use for number multiplication and repetition string, list, etc
> Example
    print(10+20)
    print("Python" + "Programming")
    print([1,2,3]+[4,5,6])

### Method Overloading
* if 2 method had the same name but argument different type 
> In python, overloading is not possible, if we try declare method with same name but different argument, python will choose the last method

[Examples -> Code III](https://github.com/DavinJago/OOP-Learning/blob/2c6ce57311b9af6223b3a3ff5f691b63a8c8f759/e%20polymorphism/polymorph.py#L30-L41)

### Constructor Overloading
* Overloading are not possible in python too
* if we declare some construct, only the last construct will executed

### Abstract Class
* Containing one or more abstract method
* just defined but not implemented

### Method on Python
1. Implemented Method
    * A method that have a name and contents, this method called implemented method
    * this method called concrete method or non-abstract
2. Un-Implemented Method
    * Only has name but not content, this called un-implemented
    * called non-concrete or abstract

* defaultly, python does'nt provide abstract class
* python equipped with modul that define abstract class (ABC) this modul called ABC.

[Examples -> Code V]()
