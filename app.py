from flask import Flask, render_template, request, flash
import sqlite3

app = Flask(__name__)

@app.route("/")
@app.route('/home') 
def index(): 
    return render_template('index.html') 
  
  
connect = sqlite3.connect('staffBranch.db') 
connect.execute('CREATE TABLE IF NOT EXISTS Staff (staffId TEXT, name TEXT, position TEXT, salary REAL, branchNo TEXT)')
connect.execute('CREATE TABLE IF NOT EXISTS Branch (branchNo TEXT, branchAddress TEXT)') 
  
@app.route('/addnew', methods=['GET', 'POST']) 
def addnew(): 
    if request.method == 'POST': 
        staffId = request.form['staffId']
        name = request.form['name'] 
        position = request.form['position'] 
        salary = request.form['salary'] 
        branchNo = request.form['branchNo'] 
        with sqlite3.connect("staffBranch.db") as users: 
            cursor = users.cursor() 
            cursor.execute("INSERT INTO Staff VALUES (?,?,?,?,?)", 
                           (staffId, name, position, salary, branchNo)) 
            users.commit() 
        return render_template("index.html") 
    else:
        connect = sqlite3.connect('staffBranch.db') 
        cursor = connect.cursor() 
        cursor.execute('SELECT * FROM Branch') 
        data = cursor.fetchall()
        # data = ['a', 'b', 'c']
        return render_template('addnew.html', data=data) 
  
  
@app.route('/allstaff') 
def allstaff(): 
    connect = sqlite3.connect('staffBranch.db') 
    cursor = connect.cursor() 
    cursor.execute('SELECT staffId, name, position, salary, branchNo FROM Staff') 
    data = cursor.fetchall() 
    return render_template("allstaff.html", data=data) 


@app.route('/deletestaff', methods=['GET', 'POST']) 
def deletestaff():
    error = None;
    if request.method == 'POST': 
        sId = request.form['staffId']
        connect = sqlite3.connect('staffBranch.db') 
        cursor = connect.cursor()
        cursor.execute("SELECT staffId from Staff WHERE staffId = ?", (sId,))
        data = cursor.fetchall()
        if data == []:
            error = 'Error, staff not found'
            return render_template('deletestaff.html', error=error)
        else:
            query = """DELETE FROM Staff WHERE staffId = ?"""
            cursor.execute(query, (sId,))
            connect.commit()
            return render_template('deletestaff.html', error="Delete successful") 
    else:
        return render_template('deletestaff.html', error=error) 

@app.route('/allbranch') 
def allbranch(): 
    connect = sqlite3.connect('staffBranch.db') 
    cursor = connect.cursor() 
    cursor.execute('SELECT branchNo, branchAddress FROM Branch') 
    data = cursor.fetchall() 
    return render_template("allbranch.html", data=data) 

@app.route('/addbranch', methods=['GET', 'POST']) 
def addbranch(): 
    if request.method == 'POST': 
        branchNo = request.form['branchNo'] 
        branchAddress = request.form['branchAddress'] 
  
        with sqlite3.connect("staffBranch.db") as users: 
            cursor = users.cursor() 
            cursor.execute("INSERT INTO Branch (branchNo, branchAddress) VALUES (?,?)", 
                           (branchNo, branchAddress)) 
            users.commit() 
        return render_template("index.html") 
    else: 
        return render_template('addbranch.html') 
    
@app.route('/editstaff', methods=['GET', 'POST']) 
def editstaff():
    error = None
    connect = sqlite3.connect('staffBranch.db') 
    cursor = connect.cursor() 
    cursor.execute('SELECT * FROM Branch') 
    data = cursor.fetchall()
    cursor.execute('SELECT staffId, name FROM Staff')
    staff = cursor.fetchall()
    if request.method == 'POST': 
        sId = request.form['staffId']
        name = request.form['name'] 
        position = request.form['position'] 
        salary = request.form['salary'] 
        branchNo = request.form['branchNo']
        with sqlite3.connect("staffBranch.db") as users: 
            cursor = users.cursor() 
            cursor.execute("UPDATE Staff SET name=?, position=?, salary=?, branchNo=? WHERE staffId = ?", 
                           (name, position, salary, branchNo, sId)) 
            users.commit()
            cursor.execute('SELECT staffId, name FROM Staff')
            staff = cursor.fetchall()
        return render_template('editstaff.html', error="Update successful", data=data, staff=staff) 
    
        connect = sqlite3.connect('staffBranch.db') 
        cursor = connect.cursor()
       # query = """UPDATE Staff SET name=?, position=?, salary=?, branchNo=? WHERE staffId = ?"""
       # cursor.execute(query, (name, position, salary, branchNo, sId))
       # connect.commit()
       # cursor.execute('SELECT staffId, name FROM Staff')
       # staff = cursor.fetchall()
        return render_template('editstaff.html', error="Update successful", data=data, staff=staff) 
    else:
        return render_template('editstaff.html', error=error, data=data, staff=staff)

@app.route('/editbranch', methods=['GET', 'POST']) 
def editbranch():
    error = None
    if request.method == 'POST':  
        branchNo = request.form['branchNo'] 
        branchAddress = request.form['branchAddress'] 
        connect = sqlite3.connect('staffBranch.db') 
        cursor = connect.cursor()
        cursor.execute("SELECT * from Branch WHERE branchNo = ?", (branchNo,))
        data = cursor.fetchall()
        if data == []:
            error = 'Error, branch not found'
            return render_template('editstaff.html', error=error)
        else:
            query = """UPDATE Branch SET branchAddress=? WHERE branchNo = ?"""
            cursor.execute(query, (branchAddress, branchNo,))
            connect.commit()
            return render_template('editbranch.html', error="Update successful") 
    else:
        return render_template('editbranch.html', error=error) 

@app.route('/deletebranch', methods=['GET', 'POST']) 
def deletebranch():
    error = None;
    if request.method == 'POST': 
        bId = request.form['branchNo']
        connect = sqlite3.connect('staffBranch.db') 
        cursor = connect.cursor()
        cursor.execute("SELECT branchNo from Branch WHERE branchNo = ?", (bId,))
        data = cursor.fetchall()
        if data == []:
            error = 'Error, branch not found'
            return render_template('deletebranch.html', error=error)
        else:
            cursor.execute("UPDATE Staff SET branchNo='' WHERE branchNo=?", (bId,))
            connect.commit()
            query = """DELETE FROM Branch WHERE branchNo = ?"""
            cursor.execute(query, (bId,))
            connect.commit()

            return render_template('deletebranch.html', error="Delete successful") 
    else:
        return render_template('deletebranch.html', error=error) 
    
if __name__ == '__main__': 
    app.run(debug=False) 