# What I Learned / summary (OOP Basic Concept)

### Object oriented Programming Definition

* Oriented -> interested on something or certain entity
* Object -> object in real life

### OOP continue

* OOP is a design method programming that modelling design with software approach or object, not function and logic
* an object referenced to data field that using attribute and unique method. all in oop was classified.
* OOP is one of popular method in software dev
* OOP suitable for large scale, complex, and updated / actively maintained
* OOP simplify development using concept abstract, inherintance, polymorph, etc

### Important Point

* everything is an object
* developer manipulate object using message passing
* all object is instance from class, class containing attrib and method

### Main Pillar OOP

* Abstraction -> Hiding Implementation, reduce complexity, ease of maintanance
* Encapsulation -> wrapping / binding with class
* Inherintance -> inherit character 
* Polymorphism -> poly means a lot,  morphs means shape.

### Examples

* Abstraction -> MyTest Calculate consist of addition, substraction, multiplication
* Encapsulation -> class including method and attrib
* Inherintance -> person -> worker/customer -> worker can inherit manager or dev
* Polymorphism -> a person can multiwork, can be a worker, father, and husband

### Main Slides - OOP Concept

* Object is a real life entity that own attrib, method, and property
* class is blueprint or template of object
* example of car, class is blueprint and object is the results like audi or mercedes
* class usually named after a object like car, and contain attrib and method.
* Inherintance (Vehicle -> Wheel/Sea -> wheel like car or bicycle -> car like SUV or MPV)

### Relations between class

* Relations between class play important role in definition of how object interact each other
* OOP provide mechanism for relation like association, aggregation, and composition

### summary of trinity relations 

* association is main concept of oop, called *use-a* relation, many shape like 1 to 1, 1 to many, etc
* aggregation is relations use *has-a*, weak relations, object not depend or controlled by container
* composition simply *part of*, strong relation, object depend by container, cannot standalone, clean API

### Examples

* Bank has a 3 Employee, Employee 1, 2, 3. The relations is strong
* College have a teacher and student, but student and teacher dont have the college.
* car have an engine, both need each other

### Coupling 

* separation called coupling
* there are 2 types, loose and tight
* coupling refer to the level of dependency
* tight coupling mean modul strongly connected each other, little change affect others
* opposite of tight, loose mean modul weakly connected each other, little change did small impact to other

### Cohession 

* refers to the level to which elements work together for a common goal
* High cohession mean elements connected each other, focus on 1 purpose
* Low cohession means elements weakly connected each other and serving many goals

* High cohession refers to some 