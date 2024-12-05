from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dados armazenados em memória
consultas = [
    {"id": 1, "paciente": "João Silva", "medico": "Dra. Maria", "data": "2024-12-10", "horario": "10:00", "descricao": "Consulta de rotina"},
    {"id": 2, "paciente": "Ana Costa", "medico": "Dr. Carlos", "data": "2024-12-12", "horario": "14:30", "descricao": "Exames de acompanhamento"},
]

# Rota GET: Listar todas as consultas
@app.get("/consultas")
def listar_consultas():
    return consultas

# Rota GET: Buscar consulta por ID
@app.get("/consultas/{consulta_id}")
def buscar_consulta(consulta_id: int):
    consulta = next((c for c in consultas if c["id"] == consulta_id), None)
    if consulta is None:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    return consulta

# Rota POST: Adicionar nova consulta
@app.post("/consultas")
def adicionar_consulta(consulta: dict):
    nova_id = max(c["id"] for c in consultas) + 1 if consultas else 1
    consulta["id"] = nova_id
    consultas.append(consulta)
    return consulta

# Rota PUT: Atualizar consulta existente
@app.put("/consultas/{consulta_id}")
def atualizar_consulta(consulta_id: int, dados_atualizados: dict):
    consulta = next((c for c in consultas if c["id"] == consulta_id), None)
    if consulta is None:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    consulta.update(dados_atualizados)
    return consulta

# Rota DELETE: Remover consulta por ID
@app.delete("/consultas/{consulta_id}")
def remover_consulta(consulta_id: int):
    global consultas
    consultas = [c for c in consultas if c["id"] != consulta_id]
    return {"message": f"Consulta {consulta_id} removida com sucesso"}
