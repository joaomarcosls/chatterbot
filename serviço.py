from sqlalchemy import true
from robo import *
from flask import Flask

robo = configurar_robo()

servico = Flask(__name__)

VERSAO = "1.0"

@servico.route("/info")
def get_info_robo():
 return VERSAO

 if __name__ == "__main__"
 servico.run(
    host= "0.0.0.0"
    debug= true
 )
