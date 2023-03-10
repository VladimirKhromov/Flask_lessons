from jinja2 import Environment, FileSystemLoader, FunctionLoader

# example 1
# FileSystemLoader

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons)

print(msg)
print()


# example 2
# FunctionLoader

def loadTpl(path):
    if path == "index":
        return '''Имя {{user.name}}, возраст {{user.old}}'''
    else:
        return '''Данные: {{user}}'''


file_loader = FunctionLoader(loadTpl) # передаем ссылку на функцию, не вызываем ее!
env = Environment(loader=file_loader)

tm = env.get_template('index')
msg = tm.render(user=persons[0])

print(msg)
print()