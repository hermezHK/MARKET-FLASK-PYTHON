from flask import Flask, render_template

app=Flask(__name__)



#test server 
@app.route("/")  
def index():
    return render_template("index.html")

def pagina_no_encontrada(error):
    return render_template("errores/404.html"), 404



def inicializar_app(config):
    app.config.from_object(config)
    app.register_error_handler(404, pagina_no_encontrada)
    return app

