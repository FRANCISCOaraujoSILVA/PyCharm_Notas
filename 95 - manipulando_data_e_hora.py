"""
MANIPULANDO DATA E HORA

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime.
"""
import datetime
# print(dir(datetime))


print(datetime.MAXYEAR)  # qual o ano máximo que o datetime suporta
print(datetime.MINYEAR)  # qual o ano mínimo que o datetime suporta
print(datetime.datetime.now())  # móduloDatetime.classeDatetime.metodoNow
print('----')


# datetime.datetime(year, month, day, minute, second, microsecond)
print(repr(datetime.datetime.now()))  # pegando a representação


# replace() para ajuste na data e hora
inicio = datetime.datetime.now()
print(inicio)

# alterar o horário para 16 horas, 0 minutos, 0 segundos, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)


