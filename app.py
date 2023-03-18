from asyncio.windows_events import NULL
from flask import Flask, render_template, url_for, request, flash, redirect
import sqlite3
import random
from users import Users

app = Flask(__name__)
app.config['SECRET_KEY'] = "atron"

def get_db_connection():
    connection = sqlite3.connect('users.db')
    connection.row_factory = sqlite3.Row
    return connection

def get_user_first_name(user_first_name):
    connection = get_db_connection()
    curso = connection.cursor()
    user_first = curso.execute('SELECT first_name FROM users WHERE id = ?', (user_first_name).fetchmany(10))
    connection.commit()
    connection.close()
    return user_first

def get_user_last_name(user_last_name):
    connection = get_db_connection()
    curso = connection.cursor()
    user_last = curso.execute('SELECT last_name FROM users WHERE id = ?', (user_last_name).fetchmany(10))
    connection.commit()
    connection.close()
    return user_last

def get_user_points(user_points):
    connection = get_db_connection()
    curso = connection.cursor()
    user_p = curso.execute('SELECT points FROM users WHERE id = ?', (user_points).fetchmany(10))
    connection.commit()
    connection.close()
    return user_p

def get_user_id(id_user):
    connection = get_db_connection()
    curso = connection.cursor()
    users_id= curso.execute('SELECT * FROM users WHERE id = ?', (id_user).fetchmany(10))
    connection.commit()
    connection.close()
    return users_id

#Allow users to create the users by their first and last names
#These users will have a random set of numbers for their points and their id will be uniquely given
@app.route('/create/', methods = ('GET', 'POST'))
def create_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        if not first_name and last_name:
            flash('Please enter your first name!')
        elif not last_name and  first_name:
            flash('Please enter your last name!')
        elif not first_name and not last_name:
            flash('Please enter both your first and last name!')
            
        else:
           connection = get_db_connection()
           points = random.randint(0,100)
           u_id = random.randint(0,1000)
           connection.execute('INSERT INTO users (user_id,first_name, last_name, points) VALUES (?,?,?,?)', (u_id,first_name, last_name,points))
           u_id_string = str(u_id)
           flash('Here is your id, keep it safe! ' + u_id_string)
           connection.commit()
           connection.close()
    return render_template('create.html')


#Allow users to search for users by first name, last name, id, or points
@app.route('/search/', methods = ('GET','POST'))
def search_user():
   if request.method == 'POST':
       first_name = request.form['first_name']
       last_name = request.form['last_name']
       points = request.form['points']
       user_id = request.form['user_id']

       if first_name is not NULL:
           get_data = get_user_first_name(first_name)
           flash(get_data)
       elif last_name is not NULL:
           get_data = get_user_last_name(last_name)
           flash(get_data)
       elif points is not NULL:
           get_data = get_user_points(points)
           flash(get_data)
       elif user_id is not NULL:
           get_data = get_user_id(user_id)
           flash(get_data)
       else:
           flash('Please enter a first name, last name, the number of points, or user id')
   return render_template('search.html')

@app.route('/delete/', methods = ('GET', 'POST'))
def delete_user():
     if request.method == 'POST':
         user_ids = request.form['user_id']
         
         if not user_ids:
             flash('Please enter an ID number')
         elif isinstance(user_ids,str):
            flash('Not a valid ID number')
         else:
           user_id_data = get_user_id(user_ids)
           connection = get_db_connection()
           connection.execute('DELETE FROM users WHERE id = ?', (user_ids))
           flash('"User ID {}" was successfully deleted' .format(user_id_data['user_id']))
           connection.commit()
           connection.close()
     return render_template('delete.html')



if __name__ == "__main__":
    app.run(debug=True)


