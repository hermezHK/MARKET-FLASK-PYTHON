from flask import Flask, render_template

app=Flask(__name__)




@app.route("/")  #test server 
def index():
    return render_template("index.html")



@app.route("/login")   #login user
def login():
    return render_template("auth/login.html") 



def pagina_no_encontrada(error):  #error 404 
    return render_template("errores/404.html"), 404



def inicializar_app(config):
    app.config.from_object(config)
    app.register_error_handler(404, pagina_no_encontrada)
    return app

