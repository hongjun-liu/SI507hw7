from flask import Flask, render_template
import secret as s
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):

    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def  topstories(nm):
    base_url = "https://api.nytimes.com/svc/topstories/v2/technology.json?"
    params = {"api-key" : s.api_key}
    results = requests.get(base_url, params).json()
    content = list()
    name=nm
    for i in results["results"]:
        content.append(i["title"])

    html = f'''
         <!DOCTYPE html>
            <html>
              <head>
                 <meta charset="UTF-8">
                   <title>Hello</title>
              </head>
              <body>
                <h1>
                    Hello, {name}!
                </h1>
                <p>Today's technology headlines are...</p>
                <p>  &#8197 &#8197 &#8197 1. { content[0]} <br>
                  &#8197 &#8197 &#8197 2. { content[1]}  <br>
                  &#8197 &#8197 &#8197 3. { content[2]}  <br>
                  &#8197 &#8197 &#8197 4. { content[3]}  <br>
                  &#8197 &#8197 &#8197 5. { content[4]}</p>
            </body>
            </html>
        '''
    return html

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)