import datetime
from datetime import datetime as dt
from datetime import time as t
from datetime import date as d
import time


def toDelta(data):
    return datetime.timedelta(
        days=data.day,
        hours=data.hour,
        minutes=data.minute,
        seconds=data.second
    )

def toDate(totalSeconds):
    # 604800 segundos em uma semana
    # 86400 segundos em um dia
    # 3600 segundos em uma hora
    # 60 segundos em um minuto
    segundos = totalSeconds % 60                     # verifica se sobrou segundos
    resto = segundos                                 # armazena os segundos que sobraram
    minutos = ((totalSeconds - resto) / 60) % 60     # remove os segundos, e calcula se sobrou minutos
    resto += minutos*60                              # armazena os minutos que sobraram
    horas = ((totalSeconds - resto) / 3600) % 24     # remove os minutos, e calcula se sobrou horas
    resto += horas*3600                              # armazena as horas que sobraram
    dias = ((totalSeconds - resto) / 86400) % 7     # remove as horas, e calcula se sobrou dias
    resto += dias*86400                              # armazena os dias que sobraram
    semanas = ((totalSeconds - resto) / 604800)
    return {
        'semanas' : semanas, 
        'dias' : dias, 
        'horas' : horas, 
        'minutos' : minutos, 
        'segundos' : segundos
    }

rentData = dt(2021,8,21,0,0,0)
returnData = dt(2021,8,30,8,15,12)

rentDataDelta = toDelta(rentData)
returnDataDelta = toDelta(returnData)

#print(f"Rent data: {rentDataDelta.strftime('time %H:%M:%S date %d/%m/%y')}")
#print(f"Return data: {returnDataDelta.strftime('time %H:%M:%S date %d/%m/%y')}")
#print(f"Time delta: {tdelta.strftime('time %H:%M:%S date %d/%m/%y')}")
tdelta = returnDataDelta - rentDataDelta
print(tdelta)
data = toDate(tdelta.total_seconds())
print(data.)