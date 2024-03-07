from flask import Flask
import random
app = Flask(__name__)


meme_listesi=["mem1",
              "mem2",
              "mem3",
              "mem4"]


@app.route("/")
def mem():
    return f'<h1>{random.choice(meme_listesi)}</h1>'



@app.route("/coin")
def coin():
    para=random.randint(1,2)
    if para==1:
        return f'<h1>Tura</h1>'
    else:
        return f'<h1>Yazı</h1>'


@app.route("/password")
def password():
    karakter="ABCÇDEFGHIİJKLMNOÖPRSTJUÜVYZabcçdefghıijklmnoöprstjuüvyz1234567890=?*_-#/"
    password1=""
    for i in range(12):
        password1+=random.choice(karakter)
    
    return password1




@app.route("/muhammed")
def isim():
    return '<h1>Merhaba benim adım Muhammed</h1>',




app.run(debug=True)










