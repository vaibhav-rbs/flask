from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Vaibhav' } # fake user
    posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'Anshu' }, 
            'body': 'Vaibhav is the best in the world.!' 
        },
        { 
            'author': { 'nickname': 'Courtney' },
            'body': 'I love you!' 
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)
