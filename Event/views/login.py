from Event.views.home import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log User In"""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == 'POST':
        if not request.form.get("username") or not request.form.get("password"):
            return render_template('failure.html', msg='Username/Password fields cannot be empty')

        # query database for username
        db = mysql.connection.cursor()
        rows = db.execute("SELECT * FROM users WHERE uname = '{}'".format(request.form.get("username")))
        rv = db.fetchone()

        # verify password
        if rows or rv['pass'] == encode(hashlib.sha1(encode(request.form.get("password", 'utf-8'))).digest(),
                                        'hex_codec').decode('utf-8'):
            session['user_id'] = rv['id']

            return redirect(url_for('index'))

        else:
            return render_template('failure.html', msg="Invalid Username And/Or Password")

    else:
        return render_template('login.html')


