from flask import Flask

app=Flask(__name__)



#test server 
@app.route("/")  
def index():
    return 'test server ok'



def inicializar_app(config):
    app.config.from_object(config)
    return app

