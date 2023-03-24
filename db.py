
import sqlite3
from textwrap import indent

def save_user_city(user_id,city):
	con = sqlite3.connect("weatherusers.db")
	cur  = con.cursor()
	conn = sqlite3.connect('cities.db')
	curr  = conn.cursor()
	curr.execute('''select * from cities where Город =  :city''', {'city':city})
	
	city_from_db = curr.fetchone()
	if city_from_db == None:
		return False
	# else:
	# 	cur.execute('insert into weatherusers values (?,?)', (user_id, city_from_db[0]))
	# 	con.commit()
	# 	con.close()
	# 	return True
	# con = sqlite3.connect("weatherusers.db")
	# cur  = con.cursor()
	# conn = sqlite3.connect('cities.db')
	# curr  = conn.cursor()
	cur.execute('''select user_id from weatherusers''')

	user_ids = cur.fetchall()
	if user_id in (x[0] for x in user_ids): 
		cur.execute('''update weatherusers set city_id = :city_id where user_id = :user_id''', {'city_id':city_from_db[0]}, {'user_id':user_id})
	else:
		cur.execute('insert into weatherusers values (?,?)', (user_id, city_from_db[0]))
	con.commit()
	con.close()
	return True
	


def get_user_lon_lat(user_id):
	con = sqlite3.connect("weatherusers.db")
	cur  = con.cursor()
	conn = sqlite3.connect('cities.db')
	curr  = conn.cursor()
	cur.execute('''select * from weatherusers where user_id = :user_id''', {'user_id': user_id})
	city_id = cur.fetchone()[1]
	curr.execute('''select * from cities where city_id = :city_id''', {'city_id':city_id})
	lat_lon= curr.fetchone()
	lat = lat_lon[2]
	lon = lat_lon[3]
	return lat, lon

def get_all_users():
	con = sqlite3.connect('weatherusers.db')
	cur = con.cursor()
	cur.execute('''select user_id from weatherusers''')

	user_ids = cur.fetchall()
	return list(x[0] for x in user_ids)

def get_user_city(user_id):
	con = sqlite3.connect("weatherusers.db")
	cur  = con.cursor()
	conn = sqlite3.connect('cities.db')
	curr  = conn.cursor()
	cur.execute('''select * from weatherusers where user_id = :user_id''', {'user_id': user_id})
	city_id = cur.fetchone()[1]
	curr.execute('''select * from cities where city_id = :city_id''', {'city_id':city_id})
	city = curr.fetchone()[1]
	return city




