from jinja2 import Template

# example 1

data = """ {% raw %}
тестовая страка для проверки {{ name }}
{% endraw %}"""


tm = Template(data)
msg = tm.render(name="Vladimir")

print(msg)

# example 2
# экранирование экранных символов

from markupsafe import escape

link = """Определение ссылки в HTML:
<a href="#">Link</a>"""

msg = escape(link)
print(msg)

# example 3
# for - для работы с повторяемыми фрагментами

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}]

# -% или %- убирает перенос строки
link = '''<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
print()

# example 4
# if / elif - для проверки условий

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{%elif c.city == "Москва" -%}
    <option>{{c['city']}}</option>
{%else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''
tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
