from datetime import datetime

def validarData(dataStr):
    try: 
        data_do_evento = datetime.strptime(dataStr, '%Y-%m-%d').date()
        data_de_hoje = datetime.now().date()
        return data_do_evento >= data_de_hoje
    except ValueError:
        return False

def adicionarEvento(listaEventos, nome, data, local, categoria):
    if not nome.strip() or not data.strip() or not local.strip() or not categoria.strip():
        return "Estranho! Isso deu erro... Tente preencher todos os campos."
    if not validarData(data):
        return "Data inválida! Por favor, insira uma data no formato AAAA-MM-DD ex: 29-10-2025."

    id = max([evento["id"] for evento in listaEventos], default=0) + 1
    
    evento = {
        "id": id,
        "nome": nome.strip(),
        "data": data,
        "local": local.strip(),
        "categoria": categoria.strip(),
        "participado": False
    }
    
    listaEventos.append(evento)
    return f"Parabéns! Você adicionou o evento '{nome}' com sucesso. ID do evento: {evento['id']}."


def listarEventos(listaEventos):
    return listaEventos

