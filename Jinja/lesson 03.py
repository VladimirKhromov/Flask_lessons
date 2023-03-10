from jinja2 import Template

# example 1
# суммирование

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300}
]

tpl = "Суммарная цена авто {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)
print()

# example 2
# рандомайзер

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300}
]

tpl = "Суммарная цена авто {{ cs | random  }}"
tm = Template(tpl)
msg1 = tm.render(cs=cars)
msg2 = tm.render(cs=cars)

print(msg1)
print(msg2)
print()

# example 3
# фильтры

users = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

tpl = '''
{%- for user in users -%}
{% filter upper %}{{user.name}}{% endfilter %}
{% endfor -%}
'''

tm = Template(tpl)
msg = tm.render(users=users)

print(msg)
print()

# example 3
# макроопределения

html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

{{ input('username') }}
{{ input('email') }}
{{ input('password') }}
'''

tm = Template(html)
msg = tm.render(users=users)

print(msg)
print()

# example 4
# вложенные макросы

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in users -%}
    <li>{{u.name}} 
{%- endfor %}
</ul>
{%- endmacro %}

{{list_users(users)}}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)
print()
