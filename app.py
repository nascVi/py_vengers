from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/index/')
@app.route('/')
def rat_d_biblio():
    return "TEST FLASK"


# query strings
@app.route('/test')
def query_strings(voiture='BMW'):
    query_val = request.args.get('voiture', voiture)
    return '<h1> ma voiture est une : {} </h1>'.format(query_val)


# remove query strings
@app.route('/user/')
@app.route('/user/<name>')
def no_query_strings(name='Linda'):
    return '<h1> Bienvenue {} !</h1>'.format(name)


# Using Template
@app.route('/films')
def films():
    films_dict = {
        'Black Panther': 2.5,
        'Avengers: End Game': 2.5,
        'Avengers: Infinity War': 3.2,
        'Doctor Strange': 2.14,
        'Captain Marvel': 1.48,
        'Guardians of the Galaxy': 2.52,
        'Guardians of the Galaxy 2': 3.5,
        'Captain America, Civil War': 1.5
    }
    return render_template('table_movies.html', films=films_dict, name='Marvel fans')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

