# -*- coding: utf8 -*-

import requests
import sqlite3
import json
import datetime
from datetime import datetime
import urllib.request
import re

def _post(str, payload):
	responce=requests.post(str, params=payload)
	return responce

def is_id_exists(id) -> bool:
	return bool(c.execute(f'SELECT * FROM "Base" WHERE id="'+id+'";').fetchall())

def is_findDB_exists(table,str, id) -> bool: #где ищем, что ищем и чему должно быть равно
	return bool(c.execute(f'SELECT * FROM "'+table+'" WHERE '+str+'="'+id+'";').fetchall())

def addtoDB(db,ids):
	try:
	
		c.execute('''create table if not exists "Base" (
		"id"	INTEGER,
		"name"	TEXT,
		"app_id"	INTEGER,
		"url"	TEXT
		)''')
		pass
	except Exception as e:
		print("except at create TABLE")

	try:
		for i in range(0, db["response"]["count"]):
			if not is_id_exists(str(db["response"]["items"][i]['id'])):
				c.execute("""insert into 'Base' values (?,?,?,?)""",(
				str(db["response"]["items"][i]['id']),
				str(db["response"]["items"][i]['name']),
				str(ids),
				str(db["response"]["items"][i]['images'][0]['url'])
				))
			#else:
			#	print("add id: "+str(db["response"]["items"][i]['id'])+" at app_id= "+ids+" skipped")
	except Exception as e:
		print("except a add to db, maybe token not valid, please try to change him or delete datebase file: "+str(e))

#временная база 
massapps={}
#id приложений
try:
	with open('appids.txt', 'r') as f:
		g=f.read().splitlines()
		#print(g)
		app_ids = g
except Exception as e:
	print(e)
	app_ids=['7362610']
	
for i in app_ids:
	massapps[i]={'access_token':''}


def post(ids):
	print("ids to get list= "+ids)
	payload={
	'api_id':ids,
	'access_token':massapps[ids]['access_token'],
	'request_id':'7',
	'method':'status.getImageList',
	'format':'json',
	'v':'5.103',
	}
	url="https://api.vk.com/method/"+payload['method']
	r=_post(url,payload)
	return json.loads(r.text)

def get(ids):
	payload={
	'api_id':ids,
	'access_token':massapps[ids]['access_token'],
	'request_id':'7',
	'method':'status.getImage',
	'format':'json',
	'v':'5.103',
	}
	url="https://api.vk.com/method/"+payload['method']
	r=_post(url,payload)
	return r.text

def set(status_id):
	

	c.execute("""SELECT * from 'Base'""")
	records = c.fetchall()
	api_id=str(c.execute(f'SELECT * FROM "Base" WHERE id="'+str(status_id)+'";').fetchall()[0][2])
	name=str(c.execute(f'SELECT * FROM "Base" WHERE id="'+str(status_id)+'";').fetchall()[0][1])
	#print("api_id: "+api_id+" name: "+name)
	payload={
	'api_id':str(api_id),
	'access_token':massapps[str(api_id)]['access_token'],
	'status_id':str(status_id),
	'request_id':'7',
	'method':'status.setImage',
	'format':'json',
	'v':'5.103'
	}
	url="https://api.vk.com/method/"+payload['method']
	r=_post(url,payload)
	#требуется для вывода информации
	#db=json.loads(get(api_id))

	print("response: "+str(r.status_code)+" set id: "+str(status_id)+" Name of emoji: "+name)#+str(db['response']['status']['name']))

	return json.loads(r.text)
	
def checkValidurl(url) -> bool:
	try:
		responce=requests.post(url)
		responce=json.loads(responce.text)
	
		if(responce['error_description']=='application is disabled'):
			return False
	except Exception as e:
		return True
	return True


#подключение БД
conn=sqlite3.connect('vk_status.getImageList.db')
c=conn.cursor()



#Запрос на сервер для получения ip
try:
	res = urllib.request.urlopen('http://2ip.ru/').read()
	ip=re.search(b'\d+\.\d+\.\d+\.\d+', res).	group().decode("utf-8") 
except Exception as e:
	print("запрос на 2ip.ru провален. текст: ",e)
	ip='192.168.99.1'

#инициализация
choise=''
update_tokens=''
print_url=''
info=False

#меню
settings=input("открыть отладочное меню?(y/n)")
if settings=='y':
	print('1. вы хотите обновить токены?')
	print('2. вы хотите сбросить список таблицы?')
	print('3. вы хотите сбросить персональные данные?(все сохраненные токены)')
	print("4. Выводить ссылку эмодзи статуса")
	print("5. вывести служебную информацию?(не рекоментуется к включению)")
	print('0. выход')
	choise=input()
if choise=='1':
	update_tokens='1'
elif choise=='2':
	try:
		c.execute('''DROP TABLE IF EXISTS 'Base';''')
	except Exception as e:
		print("table reset failed",e)
elif choise=='3':
	try:
		c.execute('''DROP TABLE IF EXISTS 'personal';''')
	except Exception as e:
		print("personal info reset failed",e)
elif choise=='4':
	print_url='1'
elif choise=='5':
	info=True
	print_url='1'
try:
	
	c.execute('''create table if not exists "personal" (
	"app_id"	INTEGER,
	"token"	TEXT,
	"date"	TEXT,
	"ip"	TEXT
	)''')
	pass
except Exception as e:
	print("except at create Personal table")

time=datetime.now()

for i in range(0, len(app_ids)):
		try:
			basetime=c.execute(f'SELECT * FROM "personal" WHERE app_id="'+str(app_ids[i])+'" AND ip="'+ip+'";').fetchall()[0][2]
			basetimedatetime=datetime.strptime(basetime, "%d-%m-%Y %H:%M")

		except Exception as e:
			print("time don't installed for appid=",app_ids[i],"error text: ",e)
			basetimedatetime=datetime.strptime("1-11-2077 1:27", "%d-%m-%Y %H:%M")
		try:
			baseip=str(c.execute(f'SELECT * FROM "personal" WHERE app_id="'+str(app_ids[i])+'" AND ip="'+ip+'";').fetchall()[0][3])
		except Exception as e:
			baseip="0.0.0.0"
			print('Не получилось получить ip от приложения с appids=', app_ids[i],'сообщение ошибки: ',e)
		try:
			time_delta=time-basetimedatetime
		except Exception as e:
			print('opps, delta dont')
			time_delta=time
		try:
			for j in range (0,5):
				if (time_delta.total_seconds() // 3600)>=24:
					try:
						c.execute('''DELETE FROM 'personal' WHERE app_id = ? AND ip=?''', (app_ids[i],ip))
					except Exception as e:
						print(app_ids[i],"time expired and falled him delete. e:",e)
					time_delta= time
		except Exception as e:
			print(e)
		
		if info:
			print(baseip," ", ip)
			print("update tokens var: ",update_tokens)
			print("in personal table finded appids=",app_ids[i]," result:",is_findDB_exists('personal', 'app_id',app_ids[i]))
			print("delta time >24?:",(time_delta.total_seconds() // 3600)>=24)

		if ((not is_findDB_exists('personal', 'app_id',app_ids[i])) or (time_delta.total_seconds() // 3600)>=24 or update_tokens=='1' or not (ip==baseip)):
			if checkValidurl('https://oauth.vk.com/authorize?client_id='+str(app_ids[i])+'&scope=1024&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1'):
				print('\n \n У вас истек или не обнаружен токен приложения: '+str(app_ids[i])+' требуется его получение, сейчас будет написана сыллка, вы должны раздрешить приложению доступ,потом когда будет написано, что нельзя никому её отправлять, скопируйте её сюда(это абсолютно безопасно, можете проверить исходник, этот файл). К сожалению токен живет 24 часа, по этому его переодически придется обновлять:( \n ')
				print('https://oauth.vk.com/authorize?client_id='+str(app_ids[i])+'&scope=1024&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1 \n')
				re=input('Вставте полученную ссылку: ')
				if re=='' or re=='-1':
					print("\n пропускаю токен \n")
				else:	
					token=re[re.find('access_token=')+13 : re.find('&')]
					if not len(token)==85: 
						print("Вы точно уверены, что ссылка содержит токен? Мы не смогли его вытащить")
						token=input('Пожалуста, извлеките токен лично(скопируйте то, что между access_token= и &expires_in), вставте его сюда: ')
						c.execute('''DELETE FROM 'personal' WHERE app_id = ? AND ip=?''', (app_ids[i],ip))
					c.execute("""insert into 'personal' values (?,?,?,?)""",(
					str(app_ids[i]),
					token,
					str(time.strftime("%d-%m-%Y %H:%M")),
					ip
					))

					conn.commit()
			else:
				print("\n appid",app_ids[i],'is not valid \n')


for i in range(0, len(app_ids)):
	try:
	   massapps[str(app_ids[i])]['access_token']=str(c.execute(f'SELECT * FROM "personal" WHERE app_id="'+str(app_ids[i])+'" AND ip="'+ip+'";').fetchall()[0][1])
	except Exception as e:
	   print('access token не получен из базы, от приложения',app_ids[i],'\n')
	



if input("Мне проверить новые эмодзи?(если запуск впервые, то соглашайтесь) (y/n) ")=="y":
	print("проверка на наличие новых эмодзи")
	try:
		c.execute('''DROP TABLE IF EXISTS 'Base';''')
	except Exception as e:
		print("table reset failed",e)
	for i in range(0, len(app_ids)):
		db=post(app_ids[i])
		addtoDB(db,app_ids[i])
	conn.commit()
	print("Проверка завершена, база обновлена")
#db=post(app_ids[0])
#print(db)
print('Список: ')
try:
	c.execute("""SELECT * from 'base'""")
	records = c.fetchall()
	print("Всего строк:  ", len(records))
	print("Вывод каждой строки \n")
	for row in records:
		print("ID:", row[0], " Имя:", row[1])
		if print_url=='1':
			print('url: ',row[3],"\n")
	print("\n\n В списке присудствует пустые имена, это значит, что в запросе имя тоже было пустое, потестируйте, как будет выглядеть(в базе данных есть ссылки на картинки эмодзи, база на sqlite3)")
	if not (print_url == '1'):
		print("Вывод ссылок на эмодзи можно включить в отладочном меню\n\n")
	else:
		print("\n")

	
except Exception as e:
	print("ошибка вывода списка, скорее всего он не создан. текст ошибки:",e)


try:
	set(input("какой Id хотите поставить? (Выберите из списка): "))
	pass
except Exception as e:
	print("По какой то причине мы не смогли установить id, если это был ваш первый запуск, то попробуйте снова запустить, вот текст ошибки: "+str(e))

conn.commit()

c.close()

input('Нажмите любую клавишу, чтобы закрыть программу...')
#print(str(json.loads(db)["response"]["items"][0]['id']))
