from flask import Flask, request, jsonify
from models import tarefas

app = Flask(__name__)

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova_tarefa = request.json
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def editar_tarefa(id):
    if id < 0 or id >= len(tarefas):
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    tarefas[id].update(request.json)
    return jsonify(tarefas[id])

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    if id < 0 or id >= len(tarefas):
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    tarefa_removida = tarefas.pop(id)
    return jsonify(tarefa_removida)

if __name__ == "__main__":
    app.run(debug=True)