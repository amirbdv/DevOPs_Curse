from flask import Flask
import requests
app = Flask(__name__)

@app.route('/h')
def hello():
    return '    Hello, Class!'

@app.route('/')
def root():
    try:
        new_joke_response = requests.get('https://api.chucknorris.io/jokes/random')
        new_joke = new_joke_response.json()
        new_joke = new_joke['value']
        return new_joke
    except Exception as e:
        return f"An error occurred: {e}"

def main() -> None:
    app.run(port=8001, debug=True)

if __name__ == '__main__':
    main()