import datetime
from babel.dates import format_date

hoje = datetime.date.today()

dia_semana = format_date(hoje, format="EEEE", locale="pt_BR")

print(f"Guarulhos, {dia_semana}, {hoje.day} de {format_date(hoje, format='MMMM', locale='pt_BR')} de {hoje.year}")