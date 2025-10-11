# campus-event-planner-Ezequiel_e_Murylo
Atividade avaliativa 1 do curso de backend com Python.

É um sistema simples em Python para gerenciar eventos, permitindo adicionar, listar, buscar e remover eventos de forma prática.  


# Como funciona o projeto

Este projeto funciona via código, sem interface gráfica. Ele utiliza uma lista de dicionários para armazenar os eventos, e cada evento possui os seguintes campos:

- `id`: número único gerado automaticamente
- `nome`: nome do evento
- `data`: data no formato `AAAA-MM-DD`
- `local`: onde o evento acontecerá o dia todo
- `categoria`: tipo do evento (ex: música, esporte, palestra)
- `participado`: status de participação (True ou False)

# Funcionalidades

- Validar data
- Adicionar eventos com **nome, data, local, categoria e participado**  
- Validar se a data do evento é válida e futura
- Listar todos os eventos cadastrados  
- Procurar eventos pelo nome  
- Deletar eventos pelo **ID**  
  
---

# Tecnologias Utilizadas

- **Python 3.12**
- Módulos nativos:
  - `datetime`
  - `time`

---

# Autor

**Ezequiel Elisel**


# Exemplo de Uso
ListaEvento = []

## Validando data

print(validarData('2025-12-05'))

## Adicionando um evento
adicionarEvento(ListaEventos, "Hackathon", "2025-12-15", "Brasília", "Tecnologia", True)

## Listando eventos
listarEventos(ListaEvento)

## Procurando por nome
procurarEventoPorNome(ListaEventos, "hackathon")

## Deletando evento
deletarEvento(eventos, 1)
