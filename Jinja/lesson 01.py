from jinja2 import Template

# example 1

name = "World"

temp = Template("Hello {{ name }}")
msg = temp.render(name=name)
print(msg)

# example 2

name = "World"
age = 30

temp = Template("Hello {{ name.upper() }}, {{ age*3//2 }}")
msg = temp.render(name=name, age=age)
print(msg)


# example 3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

per = Person("Ваня", 20)

temp = Template("Hello {{ p.name }}, {{ p.age }}")
msg = temp.render(p = per)
print(msg)


# example 4

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


per = Person("Илья", 28)

temp = Template("Hello {{ p.getName() }}, {{ p.getAge() }}")
msg = temp.render(p=per)
print(msg)

# example 5

per = {'name': "Слава", 'age': 34}
temp = Template("Hello {{ p.name }}, {{ p.age }}")
msg = temp.render(p=per)
print(msg)
temp = Template("Hello {{ p['name'] }}, {{ p['age'] }}")
msg = temp.render(p=per)
print(msg)