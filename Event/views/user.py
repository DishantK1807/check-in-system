from Event.views.home import *

@app.route('/view', methods=['GET', 'POST'])
@login_required
def view():
    if request.method == 'GET':
        db = mysql.connection.cursor()
        db.execute("SELECT * FROM events ORDER BY title")

        return render_template('view.html', rows=db.fetchall())