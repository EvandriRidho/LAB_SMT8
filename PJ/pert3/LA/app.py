from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)

url_map = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(5))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form.get('url')
        if original_url:
            short_code = generate_short_code()
            url_map[short_code] = original_url
            
    return render_template('index.html', urls=url_map)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    original_url = url_map.get(short_code)
    if original_url:
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'https://' + original_url
        return redirect(original_url)
    return "URL tidak ditemukan", 404

if __name__ == '__main__':
    app.run(debug=True)