from config import cliente_chat

cliente, modelo = cliente_chat()

mensagens = [
    {"role": "system", "content": "Responda como se você fosse um pirata."},
    {"role": "user", "content": "quantos dedos tem um elefante?"}
]

# resposta = cliente.chat(model=modelo, messages=mensagens)
# print(resposta.message.content)

# resposta mostrada aos pedaços - efeito "escrevendo"
for parte in cliente.chat(model=modelo, messages=mensagens, stream=True):
    print(parte.message.content, end='', flush=True)
print()