from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_bootstrap import Bootstrap

import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///researchportal.db?check_same_thread=False', echo=True)
app = Flask(__name__)
Bootstrap(app)

#Route definitions
@app.route('/')
def home():
    Session = sessionmaker(bind=engine)
    s = Session()
    last_posting = s.query(Posting).first()
    return render_template('index.html', last_posting=last_posting)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/search')
@app.route('/search/<term>')
@app.route('/search', methods=['POST'])
def search(term=None, exact=None):
    if(request.form):
        bar_term = str(request.form['term'])
        term = bar_term

    Session = sessionmaker(bind=engine)
    s = Session()


    if(term):
        results = s.query(Lab).filter(or_(Lab.PI.like('%'+term+'%'),
                                            Lab.desc.like('%'+term+'%'),
                                            Lab.category.like('%'+term+'%')))
    elif(exact):
        results = s.query(Lab).filter(Lab.category.equals('%'+term+'%'))
    else:
        results = s.query(Lab).all()

    return render_template('search.html', results=results, query=term)

@app.route('/postings')
def show_postings():
    Session = sessionmaker(bind=engine)
    s = Session()
    result = s.query(Posting).all()
    return render_template('postings.html', postings=result)

@app.route('/lab/<id>')
def show_lab(id=1):
    Session = sessionmaker(bind=engine)
    s = Session()
    results = [s.query(Lab).filter(Lab.id==id).first(),
            s.query(Comment).filter(Comment.lab_id==id)]
    announcements = s.query(Posting).filter(Posting.lab_id==id).all()
    return render_template('lab.html', data=results, announcements=announcements)

@app.route('/login')
def do_login():
    return render_template('login.html')

@app.route('/login_verify', methods=['POST'])
def do_login_verify():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]) )
    result = query.first()
    if result:
        if result.validate_password(POST_PASSWORD):
            session['logged_in'] = True
            session['username'] = POST_USERNAME
            return home()
    else:
        flash('wrong password!')
        return do_login()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
