def analise_vendas(vendas):
    #calcule o total de vendas
    total_vendas = sum(vendas)
    #calcule a media mensal de vendas
    media_vendas = total_vendas / len(vendas)
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    #solicite a entrada do usuario em uma unica linha 
    entrada = input("")
    #converta a entrada em uma lista de inteiros
    vendas = list(map(int,entrada.split(",")))
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))