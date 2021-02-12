import datetime as dt
from datetime import datetime
import subprocess

# Equivalência de datas
# 0 -> Segunda
# 1 -> Terça
#... -> ...
# 5 -> Sexta

zoomIdsByWeekdayAndHour = {
	'0A':'',
	'0B':'',
	'1A':'',
	'1B':'',
	'2A':'',
	'2B':'',
	'3AP':'',
	'3AI':'',
	'3BP':'98665096620',
	'3BI':'',
	'4A':'',
	'4B':''
}

today = dt.datetime.now()
todayWeekday = dt.datetime.today().weekday()
weekofYear = dt.datetime.now().isocalendar()[1]
todayDay = today.day
hourNow = today.hour
minuteNow = today.minute


if hourNow>=22:
	print('Não há mais aulas para hoje :D')
	input('Pressione qualquer tecla para continuar')
	exit()

if hourNow <20 or (hourNow == 20 and minuteNow <25):
	aux = 'A'
else:
	aux = 'B'

if todayWeekday == 3 :
	if(weekofYear % 2 == 0):
		aux+='P'
	else:
		aux+='I'

try:
	classId = zoomIdsByWeekdayAndHour[f'{todayWeekday}{aux}']
	print('Abrindo aula...')
	subprocess.call(['%AppData%\\Zoom\\bin\\Zoom.exe', f"--url=zoommtg://zoom.us/join?action=join^&confno={classId}"], shell=True)

except:
	print('Não há aula cadastrada para o dia de hoje!')
	input('Pressione qualquer tecla para continuar')
