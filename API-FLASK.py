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



def _cpf(cpf: str) -> bool:

    if cpf is confirme_condition and cpf is not None:
        return True
    else: return False

def _cnpj(cnpj: str) -> bool:

    if cnpj is confirme_condition and cnpj is not None:
        return True
    else: return False








app = Flask(__name__)

@app.route("/api/v1/transacao", methods=['POST'])
def payment_transacao():

    argumentos_ = request.json()
    cliente_cnpj = argumentos_.get("estabelecimento")
    cliente_cpf = argumentos_.get("cliente")
    if _cpf(cliente_cpf) and _cnpj(cliente_cnpj):
        del argumentos_["estabelecimento"]
        database_["recebimentos"].append(argumentos_)
        database_["total_recebido"] += argumentos_["valor"]
        response = {'aceito': 'true'}
        return jsonify(response), 200
    else:
        response = {'aceito': 'false'}
        return jsonify(response), 200


@app.route("/api/v1/transacoes/estabelecimento?cnpj=<cnpj>", methods=['GET'])
def todastransacoes(cnpj: str):

    todos_cnpj = database_
    return todos_cnpj



if __name__ == "__main__":
    app.run()
