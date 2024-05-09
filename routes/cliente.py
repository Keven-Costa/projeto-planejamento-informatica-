from flask import Blueprint, request, redirect, url_for, render_template
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""Listar Clientes"""
@cliente_route.route("/")
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)

'''Página Cadastrar'''
@cliente_route.route("/cadastrar")
def pagina_cadastrar():
    return render_template('form.html')

'''Usuario cadatrado'''
@cliente_route.route("/sucesso")
def pagina_sucesso():
    return render_template('sucesso.html')


@cliente_route.route("/", methods=["POST"])
def inserir_cliente():
    data = request.form
    
    # Cria um novo cliente e insere na lista
    novo_cliente = {
        "id": len(CLIENTES) + 1,
        "nome": data.get("nome", ""),  # Nome do cliente
        "idade": data.get("idade", ""),  # Idade do cliente
        "sexo": data.get("sexo", ""),  # Sexo do cliente
        "altura": data.get("altura", ""),  # Altura do cliente
        "peso": data.get("peso", ""),  # Peso do cliente
        "pressao_arterial": data.get("pressao_arterial", ""),  # Pressão arterial do cliente
        "alergias": data.get("alergias", ""),  # Alergias do cliente
        "medicamentos_em_uso": data.get("medicamentos_em_uso", ""),  # Medicamentos em uso
        "fuma": data.get("fuma", ""),  # O cliente fuma?
        "bebe": data.get("bebe", ""),  # O cliente bebe?
        "parentes_com_doencas": data.get("parentes_com_doencas", ""),  # Parentes com doenças
    }

    CLIENTES.append(novo_cliente)

    # Redirecionar para a página de sucesso
    return redirect(url_for("cliente.pagina_sucesso"))
