import requests
import sqlite3
import json
import datetime

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
		print("except a add to db: "+str(e))

#временная база 
massapps={
'7362610':{
'status_id':'8',
'access_token':""
},
'7670023':{
'status_id':'161',
'access_token':""
},
'7622189':{
'status_id':'121',
'access_token':""
},
'7664915':{
'status_id':'149',
'access_token':""
},
'7641157':{
'status_id':'106',
'access_token':""
}
} 
#id приложений
app_ids=['7362610','7670023','7622189','7664915','7641157']
def post(ids):
	print("ids to get list= "+ids)
	payload={
	'api_id':ids,
	'access_token':massapps[ids]['access_token'],
	'status_id':massapps[ids]['status_id'],
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

#пример вызова
#db=post(app_ids[0])


#test db json
#db="""{"response":{"count":8,"items":[{"id":114,"name":"","images":[{"height":80,"url":"https:\/\/sun9-18.userapi.com\/7Gtu0nby4TjBv-X0sX8dTzWNeO44PWnRqe9IFQ\/8a3zbKzyU3k.png","width":80},{"height":60,"url":"https:\/\/sun1.ufanet.userapi.com\/snf9roGASjuN7-KrFd_nOku2t3uRC5eKYSzzzg\/VSlZSF8XyFo.png","width":60},{"height":40,"url":"https:\/\/sun9-73.userapi.com\/c6RzhcyD10S6Mk2s6Er6bd8O3p6EVxLM0-jLiQ\/CX_ZRGlczm8.png","width":40},{"height":30,"url":"https:\/\/sun9-6.userapi.com\/wY4OvVm9HGPMa3nTFuNpa94CF6StViwprs9FpA\/axmBl7tZmWs.png","width":30},{"height":20,"url":"https:\/\/sun9-6.userapi.com\/AUDFh5oZwYL89Dyoa-cRvB1GPc0cDWxGl7De2g\/C22lwN_h8BM.png","width":20}]},{"id":115,"name":"","images":[{"height":80,"url":"https:\/\/sun2.ufanet.userapi.com\/-z7Trcb0dgFl6L93J64EbWtKqt6kxY0_fIsSJQ\/nUZmj9iuNNU.png","width":80},{"height":60,"url":"https:\/\/sun9-71.userapi.com\/rTpQxk4iKUbkn9e9akUzt_7It1EX0a9axweG6A\/xwjKBLjnr74.png","width":60},{"height":40,"url":"https:\/\/sun1.ufanet.userapi.com\/kAW4zyvhG7AUPkv9_lp669Hc8OsJv_Mu2wWZ4g\/1AeJjMmxOys.png","width":40},{"height":30,"url":"https:\/\/sun9-55.userapi.com\/gJ0nCtwXoRVr9ttMlDhLoK8BYMJSFRFlFd5oTQ\/nWCP3SbSZf4.png","width":30},{"height":20,"url":"https:\/\/sun2.ufanet.userapi.com\/skAmlDoAV3ztd9VjpvhdBIrlJSe4Lbc_rMTh0A\/B5eXBtiwh2g.png","width":20}]},{"id":116,"name":"","images":[{"height":80,"url":"https:\/\/sun1.ufanet.userapi.com\/DBnyifGraFx93seIMVMUJ-1g6uS5GQhfI3cYxg\/icdP0ZrJtKs.png","width":80},{"height":60,"url":"https:\/\/sun9-47.userapi.com\/tYgu-lkol4AEw8COc4blXqkyzhb8WDLNtXJM5g\/5Q4FIfN6QBg.png","width":60},{"height":40,"url":"https:\/\/sun1.ufanet.userapi.com\/4c9RNx8UepXJFQC0_EQmjQh2dwKQJUFOa8hpBg\/GBxxwrm7QpI.png","width":40},{"height":30,"url":"https:\/\/sun9-65.userapi.com\/iZL-7_CAeLOgAw5BOhuhEoOAH1dQ4iHiI-VpFQ\/x4E7oBsxnRY.png","width":30},{"height":20,"url":"https:\/\/sun3.ufanet.userapi.com\/g5ItozkaSH0r8mlkWNeDtPf_SnK12dBw6cSfSw\/niWOudaRfCw.png","width":20}]},{"id":117,"name":"","images":[{"height":80,"url":"https:\/\/sun9-43.userapi.com\/t9BJTDISO9JU5hQ5W11LoTLVmv_3sz2xgdYvqA\/XcqgDWNoXWU.png","width":80},{"height":60,"url":"https:\/\/sun3.ufanet.userapi.com\/8O0YKiexXQQzzk3Ra5Baf02jbznOmnEh-5n4cw\/ILIEGDUJloY.png","width":60},{"height":40,"url":"https:\/\/sun9-53.userapi.com\/r5Gsusb6naxwoId5DEXUQz9HwmdQiL58bg0rUA\/jSZcik_7-h0.png","width":40},{"height":30,"url":"https:\/\/sun9-62.userapi.com\/C0nDvNtooXSncX8M7XxJQiQuzHlwVuBme-MC-Q\/DG9MShqz1Eo.png","width":30},{"height":20,"url":"https:\/\/sun9-68.userapi.com\/bDju0HiuzeIjNqY5AvhoE6FKsIDVDw4hDqPcmg\/wbiRV5VihJU.png","width":20}]},{"id":118,"name":"","images":[{"height":80,"url":"https:\/\/sun9-20.userapi.com\/dt8aDv2dGIIBWep2u8I5TCajM-sgifLYIszZtg\/GKZo8i0SwZ4.png","width":80},{"height":60,"url":"https:\/\/sun9-74.userapi.com\/OEkGwYb1i7Vkoq1gq9u-FcQKftyGkje3N-P1nQ\/kvJx0uYIpLc.png","width":60},{"height":40,"url":"https:\/\/sun9-67.userapi.com\/WMlh8Pwn9Y9yGH19uOEOrau80mupor4owsQbkw\/lcIdAZ2oKho.png","width":40},{"height":30,"url":"https:\/\/sun9-40.userapi.com\/N1jd_39HCKPmW7jru7JmtvKbZdqINtCf2icIlQ\/cCy0ezw22DU.png","width":30},{"height":20,"url":"https:\/\/sun9-36.userapi.com\/1lKP5F4qa3OSlwqkqIx5meLVxV5T5sqcPeyWkw\/WsloUuc2hlY.png","width":20}]},{"id":119,"name":"","images":[{"height":80,"url":"https:\/\/sun1.ufanet.userapi.com\/iV2meCWQyYPM3eERpD4AWhDzCY8zTb-fTc_1ng\/3Ugi6Ok4pME.png","width":80},{"height":60,"url":"https:\/\/sun9-32.userapi.com\/gVGf0VVow5Ck8tZI9YiH2dAcpRLznMm-7vf1mg\/Sk2qJqlO7zw.png","width":60},{"height":40,"url":"https:\/\/sun2.ufanet.userapi.com\/0OCxFz_bB7Dg9RoI4g_rYc20YEjgZBWS6bwtBA\/c2LoWHADq5U.png","width":40},{"height":30,"url":"https:\/\/sun9-2.userapi.com\/KU4Vww5HWRbeswSK72m-yHNDqTZtKYfj1wrbYg\/ytFuYr4Blpg.png","width":30},{"height":20,"url":"https:\/\/sun9-37.userapi.com\/SqSttn8n72Ut7BbMJEctYrCfhTbkI1HtrPVNDQ\/NXGxvKw_qZY.png","width":20}]},{"id":120,"name":"","images":[{"height":80,"url":"https:\/\/sun1.ufanet.userapi.com\/HAJsq-jDejSjQir2fmdWrJiumvEfSZK0VkR-nw\/oPNHVF5I33w.png","width":80},{"height":60,"url":"https:\/\/sun9-75.userapi.com\/NCEmIOenLUkkaeIY16OymJ9HNp9vMTda5eDZ9g\/DDr6jtLV-9Y.png","width":60},{"height":40,"url":"https:\/\/sun3.ufanet.userapi.com\/uBUl7Hd9r9pe0tEQLQTgYFmhY1Rvzt-_4SAbsg\/dwIsgf-yPH8.png","width":40},{"height":30,"url":"https:\/\/sun9-65.userapi.com\/nhlFeKsQpltPlLAR17z2uHqtwKPt68BVLUQ63w\/tSKbuFSbwdU.png","width":30},{"height":20,"url":"https:\/\/sun9-7.userapi.com\/MmY3zfAJUN7tMIVFH7mptwlKL4AtW3cqx2kqyw\/mQTJElNje9U.png","width":20}]},{"id":121,"name":"","images":[{"height":80,"url":"https:\/\/sun9-33.userapi.com\/RoGd25GyMrn6AywUM00Wpe6W0fjJ3KZugzta_A\/K0rUhFjlEmA.png","width":80},{"height":60,"url":"https:\/\/sun9-73.userapi.com\/5F1PRYI2w1nRJvNnynsVol4lmAtWyUgQfbR9UA\/vAyMr919ZUA.png","width":60},{"height":40,"url":"https:\/\/sun9-8.userapi.com\/WOrVXaW0TNDqG8oZ5l4z5xpRMrVGJ42yNx_b6g\/pEoveAh5qlc.png","width":40},{"height":30,"url":"https:\/\/sun9-10.userapi.com\/Nit9e2YBZxwkHh6Mwu5KkaCzVQD0EuWhv4CtkA\/rEj9yp864dk.png","width":30},{"height":20,"url":"https:\/\/sun9-60.userapi.com\/qFbDhvy6xWwkvCfIAc6wEkt_UP0Yw-wGxhhrhg\/h8rAYaJuhJI.png","width":20}]}]}}"""


#try:
#	for i in range(0, db["response"]["count"]):
#		print("Id: "+str(db["response"]["items"][i]['id']))
#		print("name: "+str(db["response"]["items"][i]['name']))
#		print("Url: "+str(db["response"]["items"][i]['images'][0]['url']))
#except Exception as e:
#	print("except a json format: "+e)

conn=sqlite3.connect('vk_status.getImageList.db')
c=conn.cursor()

try:
	
	c.execute('''create table if not exists "personal" (
	"app_id"	INTEGER,
	"token"	TEXT,
	"date"	TEXT
	)''')
	pass
except Exception as e:
	print("except at create Personal table")

time=datetime.date.today()

for i in range(0, len(app_ids)):
	try:
		basetime=c.execute(f'SELECT * FROM "personal" WHERE app_id="'+str(app_ids[i])+'";').fetchall()[0][2]
		time_d=basetime[basetime.rfind('-')+1:]
		time_m=basetime[basetime.find('-')+1:basetime.rfind('-')]
	except Exception as e:
		time_d=-1
		time_m=-1

	if ((not is_findDB_exists('personal', 'app_id',app_ids[i])) or not (str(time.day)==time_d and time_m==str(time.month))):
		print('\n \n У вас истек или не обнаружен токен приложения: '+str(app_ids[i])+' требуется его получение, сейчас будет написана сыллка, вы должны раздрешить приложению доступ,потом когда будет написано, что нельзя никому её отправлять, скопируйте её сюда(это абсолютно безопасно, можете проверить исходник, этот файл). К сожалению токен живет 24 часа, по этому его переодически придется обновлять:( \n ')
		print('https://oauth.vk.com/authorize?client_id='+str(app_ids[i])+'&scope=1024&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1 \n')
		re=input('Вставте полученную ссылку: ')
		token=re[re.find('access_token=')+13 : re.find('&')]
		if not len(token)==85: 
			print("Вы точно уверены, что ссылка содержит токен? Мы не смогли его вытащить")
			token=input('Пожалуста, извлеките токен лично(скопируйте то, что между access_token= и &expires_in), вставте его сюда: ')
		c.execute('''DELETE FROM 'personal' WHERE app_id = ?''', (app_ids[i],))
		c.execute("""insert into 'personal' values (?,?,?)""",(
		str(app_ids[i]),
		token,
		str(time)
		))

conn.commit()

for i in range(0, len(app_ids)):
	massapps[str(app_ids[i])]['access_token']=str(c.execute(f'SELECT * FROM "personal" WHERE app_id="'+str(app_ids[i])+'";').fetchall()[0][1])



if input("Мне проверить новые эмодзи?(если запуск впервые, то соглашайтесь) (y/n)")=="y":
	print("проверка на наличие новых эмодзи")
	for i in range(0, len(app_ids)):
		db=post(app_ids[i])
		addtoDB(db,app_ids[i])
	conn.commit()
	print("Проверка завершена, база обновлена")
#db=post(app_ids[0])
#print(db)
print('Список: ')

c.execute("""SELECT * from 'base'""")
records = c.fetchall()
print("Всего строк:  ", len(records))
print("Вывод каждой строки \n")
for row in records:
	print("ID:", row[0], " Имя:", row[1])

print("\n\n В списке присудствует пустые имена, это значит, что в запросе имя тоже было пустое, потестируйте, как будет выглядеть(в базе данных есть ссылки на картинки эмодзи, база на sqlite3) \n\n")



try:
	set(input("какой Id хотите поставить? (Выберите из списка): "))
	pass
except Exception as e:
	print("По какой то причине мы не смогли установить id, если это был ваш первый запуск, то попробуйте снова запустить, вот лог ошибки: "+str(e))

conn.commit()

c.close()


#print(str(json.loads(db)["response"]["items"][0]['id']))

