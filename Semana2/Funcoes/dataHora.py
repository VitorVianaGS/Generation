import calendar
import datetime

from babel.dates import format_date

meses = ["janeiro", 
         "fevereiro", 
         "março", 
         "abril", 
         "maio", 
         "junho",
         "julho", 
         "agosto", 
         "setembro", 
         "outubro", 
         "novembro", 
         "dezembro"
         ]


# 12/05/1999
data = datetime.date(1999, 5, 12)
print(data)

# Data atual
hoje = datetime.date.today()
print(hoje)

# Data formatada
hoje = datetime.date.today()
print(hoje.strftime("%d/%m/%Y"))

# Data por extenso
print(f"Guarulhos, {format_date(hoje, format='EEEE', locale='pt_BR')}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

# Ver se o ano é bissexto
print(f"É ano bissexto: {calendar.isleap(2024)}")

# Saber qual é o último dia do mês
print(f"Qual é o último dia do mês? {calendar.monthrange(2026, 2)[1]}")

