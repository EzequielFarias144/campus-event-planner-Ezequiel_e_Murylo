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
        return "Data inválida! Por favor, insira uma data no formato AAAA-MM-DD ex: 2025-12-15."

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
    print(f"Parabéns! Você adicionou o evento {nome} com sucesso. ID do evento: {evento['id']}.")


def listarEventos(listaEventos):
    if len(listaEventos) == 0:
        return "❌ Nenhum evento encontrado... Que tal cadastrar um?"
    
    resultado = "EVENTOS\n"
    resultado += "=" * 40 + "\n"
    
    for i, evento in enumerate(listaEventos, start=1):
        resultado += f"\n🎯 Evento #{i}:\n"
        resultado += f"   ID: {evento.get('id', 'N/A')}\n"
        resultado += f"   Nome: {evento['nome']}\n"
        resultado += f"   Data: {evento['data']}\n"
        resultado += f"   Local: {evento['local']}\n"
        resultado += f"   Categoria: {evento['categoria']}\n"
        
        participou = evento['participado']
        status = "Sim" if participou else "Não"
        resultado += f"   Participou: {status}\n"
        
        if i < len(listaEventos):
            resultado += "─" * 25 + "\n"

    resultado += f"\n📊 Total: {len(listaEventos)} evento(s)"
    print(resultado)


def procurarEventoPorNome(listaEventos, nome):
    if not nome or nome.isspace():
        print("Por favor, insira um nome válido para a busca.")
        
    nome_pronto_para_busca = nome.strip().lower()
    resultados_da_busca = []

    for evento in listaEventos:
        nome_do_evento = evento.get('nome', '').lower()

        if nome_pronto_para_busca in nome_do_evento:
            resultados_da_busca.append(evento)

    if resultados_da_busca:
        print("Encontrei seu evento! Aqui estão os detalhes:")
        for evento in resultados_da_busca:
            print(f"\nID: {evento['id']}, \nNome: {evento['nome']}, \nData: {evento['data']}, \nLocal: {evento['local']}, \nCategoria: {evento['categoria']}, \nParticipou: {[evento['participado']]} ")
    else:
        print("Nenhum evento encontrado com esse nome, por favor tente outro.")
