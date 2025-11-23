# Python Classes - Simple & Clear Explanation

## 🧱 What is a Class?
A **class** is a blueprint for creating objects.

**Class = Blueprint**
**Object = Actual product created using the blueprint**

---

## 🧪 Why Do We Need Classes?
- Organize data and functions together
- Reuse code easily
- Model real-world things like Car, Student, BankAccount

---

## 🧩 Basic Structure
```python
class ClassName:
    # attributes
    # methods
```

---

## 🧨 Constructor (`__init__`)
Runs automatically when you create an object.
```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
```

---

## 🏗️ Creating Objects
```python
s1 = Student("Amey", 24, 95)
s2 = Student("Riya", 22, 88)
```

---

## 🔧 Adding Methods
```python
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def greet(self):
        return f"Hello, I am {self.name}"
```

---

## 📦 Full Example
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def full_name(self):
        return f"{self.brand} {self.model} ({self.year})"
```

---

## 🎯 Key Terms
- **Class**: Template
- **Object**: Instance created from class
- **Attributes**: Variables inside object
- **Methods**: Functions inside class
- **self**: Represents the object itself
- **Constructor**: `__init__`

---

## 🧠 Memory Trick
**Class = Recipe**  
**Object = Cake**  
**Ingredients = Attributes**  
**Steps = Methods**

---

## 🏛️ Inheritance
Inheritance allows one class (child) to use the properties and methods of another class (parent).

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"
```

---

## 🎭 Polymorphism
Same method name, different behaviors.

```python
class Cat:
    def speak(self): return "Meow"

class Dog:
    def speak(self): return "Bark"

for pet in [Cat(), Dog()]:
    print(pet.speak())
```

---

## 🔐 Encapsulation
Protecting data using private variables.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance
```

---

## 🆚 Class vs Instance Variables
- **Class variable** → shared by all objects
- **Instance variable** → unique for each object

```python
class Car:
    wheels = 4  # class variable
    def __init__(self, brand):
        self.brand = brand  # instance variable
```

---

## ✨ Magic Methods
Special methods that start and end with `__`.

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages
```

---

