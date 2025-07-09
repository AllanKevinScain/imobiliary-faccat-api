from django import template
import re

register = template.Library()


@register.filter
def format_cpf(value):
    cpf = re.sub(r'\D', '', value)
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return value


@register.filter
def format_telefone(value):
    telefone = re.sub(r'\D', '', value)
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    elif len(telefone) == 10:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    return value
