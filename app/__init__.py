from flask import Flask , render_template

app=Flask(__name__)



app =Flask(__name__)
app.debug= True

@app.route('/')
def index():
    return  render_template('index.html')

def pagina_no_encontrada(error):
    return render_template('errores/404.html'),404


def inicializar_app(Config):
    app.config.from_object(Config)
    app.register_error_handler(404, pagina_no_encontrada) #manejador de errores en el caso que se busque una pagina que no existe. en este caso un 404
    return app