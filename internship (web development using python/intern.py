import mysql.connector
from flask import Flask, render_template, request, redirect, flash, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Function to get database connection and cursor
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Divya@2004",
        database="dbs"
    )

# Route for login page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        mydb = get_db_connection()
        mycursor = mydb.cursor()
        
        sql = "SELECT * FROM dtable WHERE username = %s AND passwrd = %s"
        values = (username, password)
        
        mycursor.execute(sql, values)
        result = mycursor.fetchone()
        
        mycursor.close()
        mydb.close()
        
        if result:
            session['username'] = username
            return redirect(url_for('b'))
        else:
            flash("Invalid username or password. Please try again.")
            return redirect(url_for('index'))
    
    return render_template('loginto.html')


# Main page route
@app.route('/b', methods=['GET', 'POST'])
def b():
    return render_template('blue.html')

# Sample page route
@app.route('/s', methods=['GET', 'POST'])
def s():
    return render_template('sample.html')

# Signup route
@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        mydb = get_db_connection()
        mycursor = mydb.cursor()
        
        sql = "INSERT INTO dtable (username, passwrd) VALUES (%s, %s)"
        values = (username, password)
        
        mycursor.execute(sql, values)
        mydb.commit()
        
        mycursor.close()
        mydb.close()
        
        return redirect('/')
    
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
