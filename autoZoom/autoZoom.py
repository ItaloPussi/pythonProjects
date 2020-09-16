import datetime as dt
from datetime import datetime
import subprocess

# Equivalência de datas
# 0 -> Segunda
# 1 -> Terça
#... -> ...
# 5 -> Sexta

zoomIdsByWeekdayAndHour = {
	'0A':'96882707383',
	'0B':'99065746906',
	'1AT':'96483600439',
	'1BT':'94534367630',
	'1AP':'93887197663',
	'1BP':'93002058443',
	'2A':'99831250028',
	'2B':'96214476566',
	'3A':'98507116066',
	'3B':'92229832578',
	'4A':'94148244295',
	'4B':'97169171013'
}

today = dt.datetime.now()
todayWeekday = dt.datetime.today().weekday()
weekofYear = dt.datetime.now().isocalendar()[1]
todayDay = today.day
hourNow = today.hour
minuteNow = today.minute


if hourNow>11 or (hourNow == 11 and minuteNow >15):
	print('Não há mais aulas para hoje :D')
	input('Pressione qualquer tecla para continuar')
	exit()

if hourNow <9 or (hourNow == 9 and minuteNow <35):
	aux = 'A'
else:
	aux = 'B'

if todayWeekday == 1 :
	if(weekofYear % 2 == 0):
		aux+='T'
	else:
		aux+='P'

try:
	classId = zoomIdsByWeekdayAndHour[f'{todayWeekday}{aux}']
	print('Abrindo aula...')
	subprocess.call(['%AppData%\\Zoom\\bin\\Zoom.exe', f"--url=zoommtg://zoom.us/join?action=join^&confno={classId}"], shell=True)
	exit()

except:
	print('Não há aula cadastrada para o dia de hoje!')
	input('Pressione qualquer tecla para continuar')
