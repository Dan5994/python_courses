from flask import Flask, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(dbname='facebook', host='localhost',  user='postgres', password='260498')



@app.get('/users')
def get_users():
    cursor = conn.cursor()
    sql_create_database = f"select * from users"
    cursor.execute(sql_create_database)
    result_users = cursor.fetchall()
    return result_users


@app.get('/posts')
def get_posts():
    cursor = conn.cursor()
    sql_create_database = "select * from posts"
    cursor.execute(sql_create_database)
    result_posts = cursor.fetchall()
    return result_posts

@app.post('/users')
def create_users():
    cursor = conn.cursor()
    name = request.form.get('name')
    age = request.form.get('age')
    sql_create_database = f"insert into users (name, age) values ('{name}', {age})"
    cursor.execute(sql_create_database)
    conn.commit()
    return 'User created'
#
#
@app.post('/posts')
def create_post():
    cursor = conn.cursor()
    title = request.form.get('title')
    id_user = request.form.get('id_user')
    sql_create_database = f"insert into posts (title, id_user) values ('{title}', {id_user})"
    cursor.execute(sql_create_database)
    conn.commit()
    return 'Post created'

@app.get('/users/<id>')
def get_one_users(id):
    cursor = conn.cursor()
    sql_create_database = f"select * from users where id = {id}"
    cursor.execute(sql_create_database)
    result_users = cursor.fetchone()
    if result_users == None:
        return 'Пользователь не найден'
    else:
        return list(result_users)

@app.get('/posts/<id_posts>')
def get_one_posts(id_posts):
    cursor = conn.cursor()
    sql_create_database = f"select * from posts where id_posts = {id_posts}"
    cursor.execute(sql_create_database)
    result_posts = cursor.fetchone()
    if result_posts == None:
        return 'Пост не найден'
    else:
        return list(result_posts)