from flask import Flask, jsonify

from vendedor import Vendedor

api = Flask(__name__)

if __name__ == "__main__":
    api.run(debug=True)
    
@api.route('/api')
def ola_mundo():
    return jsonify({'msg': 'Olá Mundo!'})

@api.route('/api/calcular_valor_receber/<nome>/<meses_contratado>/<valor_venda>')
def calcular_valor_receber(nome, meses_contratado, valor_venda):
    vendedor = Vendedor(nome, int(meses_contratado), float(valor_venda))
    percent_comissao = vendedor.calcular_comissao()
    salario_base = vendedor.calcular_salario_base()
    valor_receber = vendedor.calcular_valor_receber()
    
    return jsonify({'perc_comissao': percent_comissao, 'salario_base': salario_base, 'valor_receber' : valor_receber})