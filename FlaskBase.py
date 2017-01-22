from flask import Flask, render_template, request, redirect, url_for, session
from DataManage.DataManage import DataManage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fhksdy687rh23ihrh'

info = {}
formc = {}
login_status = [False]

@app.route('/', methods=['GET', 'POST'])
def login():
    info['message_l'] = '填写并登录'
    info['m_name'] = 'logn'
    if request.method == 'POST':
        formc['name_l'] = request.form.get('inputName')
        formc['psw_l'] = request.form.get('inputPsw')
        if DataManage.DataSelect(formc) != []:
            session['name'] = formc['name_l']
            info['message_l'] = '登录成功！'
            info['m_name'] = 'logy'
            login_status[0] = True
        else:
            info['message_l'] = '登录失败!'
            info['m_name'] = 'logn'
            login_status[0] = False
    return render_template('Login.html', info=info)

@app.route('/Reg/', methods=['GET', 'POST'])
def reg():
    info['message_r'] = '填写并注册'
    if request.method == 'POST':
        formc['name'] = request.form.get('inputName')
        formc['psw'] = request.form.get('inputPsw2')
        formc['email'] = request.form.get('inputEmail')
        formc['tel'] = request.form.get('inputTel')
        if DataManage.DataInsert(formc):
            info['message_r'] = '注册成功！'
        else:
            info['message_r'] = '注册失败！'
    return render_template('Reg.html', info=info)

@app.route('/Success/')
def LoginSuccess():
    if login_status[0] == False:
        return redirect(url_for('login'))
    info['user_agent'] = request.headers.get('User-Agent')
    # info['ip'] = request.remote_addr
    info['ip'] = request.headers['X-Forwarded-For']
    return render_template('Success.html', info=info, username=session.get('name'))

if __name__ == '__main__':
    app.run(debug=True)