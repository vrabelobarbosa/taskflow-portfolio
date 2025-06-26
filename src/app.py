from flask import Flask, request, jsonify
from models import tarefas

app = Flask(__name__)

# Rota para listar todas as tarefas
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    # Retorna a lista completa de tarefas no formato JSON
    return jsonify(tarefas)

# Rota para criar uma nova tarefa
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    # Recebe os dados da nova tarefa do corpo da requisição (JSON)
    nova_tarefa = request.json
    # Adiciona a nova tarefa à lista de tarefas
    tarefas.append(nova_tarefa)
    # Retorna a tarefa criada com status HTTP 201 (Created)
    return jsonify(nova_tarefa), 201

# Rota para editar uma tarefa existente pelo índice (id)
@app.route("/tarefas/<int:id>", methods=["PUT"])
def editar_tarefa(id):
    # Verifica se o id é válido dentro do intervalo da lista de tarefas
    if id < 0 or id >= len(tarefas):
        # Retorna erro 404 caso a tarefa não exista
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    # Atualiza a tarefa com os dados recebidos no corpo da requisição
    tarefas[id].update(request.json)
    # Retorna a tarefa atualizada
    return jsonify(tarefas[id])

# Rota para deletar uma tarefa pelo índice (id)
@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    # Verifica se o id é válido dentro do intervalo da lista de tarefas
    if id < 0 or id >= len(tarefas):
        # Retorna erro 404 caso a tarefa não exista
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    # Remove a tarefa da lista e guarda para retornar
    tarefa_removida = tarefas.pop(id)
    # Retorna a tarefa removida
    return jsonify(tarefa_removida)

if __name__ == "__main__":
    # Inicia o servidor Flask em modo debug para facilitar o desenvolvimento
    app.run(debug=True)