from jinja2 import Environment, FileSystemLoader, FunctionLoader

# example 1

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain='http://proproprogs.ru', title="Про Jinja")

print(msg)
