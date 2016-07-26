from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Tom'}
    posts = [
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Florida!' 
        },
        { 
            'author': {'nickname': 'Dalton'}, 
            'body': 'I like turtles!' 
        },
        { 
            'author': {'nickname': 'Tom'}, 
            'body': 'I think I like Python and Flask!' 
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)