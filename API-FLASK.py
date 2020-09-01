from flask import Flask, jsonify, request
import json


database_ = {
    "estabelecimento": {
        "nome": "Nosso Restaurante de Todo Dia LTDA",
        "cnpj": "45.283.163/0001-67",
        "dono": "Fabio I.",
        "telefone": "11909000300",
    },
    "recebimentos": [
    ],
    "total_recebido":""
}



def validate_cpf(cpf: str) -> bool:

    if cpf is confirme_condition and cpf is not None:
        return True
    else: return False

def validate_cnpj(cnpj: str) -> bool:

    if cnpj is confirme_condition and cnpj is not None:
        return True
    else: return False








app = Flask(__name__)

@app.route("/api/v1/transacao", methods=['POST'])
def post_transacao():

    argumentos_ = request.json()
    cliente_cpf = argumentos_.get("cliente")
    cliente_cnpj = argumentos_.get("estabelecimento")
    if validate_cpf(cliente_cpf) and validate_cnpj(cliente_cnpj):
        del argumentos_["estabelecimento"]
        database_["recebimentos"].append(argumentos_)
        database_["total_recebido"] += argumentos_["valor"]
        response = {'aceito': 'true'}
        return jsonify(response), 200
    else:
        response = {'aceito': 'false'}
        return jsonify(response), 200


@app.route("/api/v1/transacoes/estabelecimento?cnpj=<cnpj>", methods=['GET'])
def get_all_transactions(cnpj: str):

    todos_cnpj = database_
    return todos_cnpj



if __name__ == "__main__":
    app.run()
