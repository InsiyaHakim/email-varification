from flask import Flask,redirect,request,render_template,session
from mysqlconnection import MySQLConnector
import datetime
t = (2009, 2, 17, 3, 1,'PM')
#t = time.mktime(t)
format = '%Y-%m-%d %H:%M %p'

app=Flask(__name__)
mysql=MySQLConnector(app,'user_emails')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index',methods=['POST'])
def display_records():
    query="SELECT * FROM emails where emails= :selected_email"
    data={
        'selected_email': request.form['email']
    }
    db=mysql.query_db(query,data)
    if len(db)==0:
        return render_template('index.html',message="Email is not Valid")
    else:
        return redirect('/success')
        #return render_template('index.html',user_record=db)
@app.route('/success')
def success():
    query="SELECT * FROM emails"
    db=mysql.query_db(query)
    #for entity in db:
        #entity_date=entity['created_at']
        #my_date = datetime.datetime.strftime("%m/%d/%y %-H:%M %p", entity_date)
        #print my_date
    return render_template('success.html',users_record=db)

@app.route('/<u_id>/delete')
def delete(u_id):
    query="DELETE FROM emails where id = :selected_id"
    data={
        'selected_id': u_id
    }
    mysql.query_db(query,data)
    return redirect('/success')
app.run(debug=True)