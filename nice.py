from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """Hi! This is the home page. 
              <br> 
              <a href='/hello'>Go to the Hello page.</a> """




@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    html_tokens = ["<option value='{0}'>{0}</option>".format(c) for c in AWESOMENESS]

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <label>
          Select a nice word:
          <select name="compliment">
            %s
          </select>
          </label>
          <input type="submit">
        </form>
        <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label>
          <label>
          Select a mean word:
          <select name="insult">
            <option value="smelly">smelly</option>
            <option value="cinohtyP">cinohtyP</option>
            <option value="ugly">ugly</option>
            <option value="rude">rude</option>
          </select>
          </label>
          <input type="submit">
        </form>

      </body>
    </html>
    """ % '\n'.join(html_tokens)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    print compliment
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    insult = request.args.get("insult")
    
    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, insult)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change sthe code.
    app.run(debug=True)
