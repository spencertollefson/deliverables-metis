from flask import Flask, request, render_template, jsonify

point_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5,
                'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q':10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4,
                'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

app = Flask('scrabble')

def score_letters(letters):
    letters = letters.upper()
    letter_scores = [point_values.get(letter,0) for letter in letters]
    return sum(letter_scores)


@app.route('/')
def index():
    return 'Welcome to Scrabble Land!!!'


@app.route('/hand/<letters>')
def sum_of_points(letters):
    if not letters.isalpha():
        return render_template('error.html', letters=letters)
    letters = letters.upper()
    return render_template('scrabble.html', score=score_letters(letters), letters=letters)


@app.route('/api/hand', methods=['POST'])
def api_score():
    # if not request.json or ('letters' not in request.json):
    #     abort(400)
    score = score_letters(request.json['letters'])
    response = {
        'score': score
    }
    return jsonify(response), 201


## Put your work here. You are also free to use static/css and templates/ if you would like


## This just gets flask running
if __name__=='__main__':
    app.run(port=5000, debug=True)


"""
sam = {
'type': 'POST',
'contentType': 'application/json',
'url': '/api/hand',
'dataType': 'json',
'async': true,
'data': JSON.stringify({'letters': 'coffee'}),
'success': (result) => {console.log(result) },
'error': (result) => {console.log('Something went horribly wrong')}
}
"""