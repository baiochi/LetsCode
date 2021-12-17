
# Projeto Final  

## Descrição  

Para esse projeto nós criaremos uma rede social baseada no Instagram onde teremos um grafo direcionado, já que posso seguir alguém que não me segue. Além disso, teremos conexões que serão melhores amigos e outras que serão conexão comuns. Logo, teremos um grafo direcionado e ponderado.  
O objetivo será criar algumas funções relacionadas ao grafo e a rede social:  
- Exibir número de seguidores
- Exibir quantidades de pessoas que o usuário segue
- Ordenar a lista de Stories, ou seja, melhores amigos primeiro e depois conexões comuns ordenadas por ordem alfabética -> [melhores amigos em ordem alfabetica , amigos em ordem alfabetica]
- Encontrar top k influencers, ou seja, k pessoas que mais tem seguidores da rede
- Encontrar o caminho entre uma pessoa e outra na rede

## Dados

Para montar o grafo, irei disponibilizar dois arquivos csv contendo:  
1) Usuário da rede: Nome e username  
2) Conexões: Pessoas que cada usuário segue e uma flag indicando se é melhor 
amigo ou não (2 = Melhor amigo, 1 = não melhor amigo)  

Usuarios.csv  
    Nome, Username
Conexoes.csv  
    Username, Pessoa que ele segue, Flag Melhor Amigo

NÃO É PERMITIDA A UTILIZAÇÃO DE BIBLIOTECAS QUE NÃO VIMOS EM AULA.

Data de entrega: 29/09/2021  
  
<b>Critérios de avaliação:</b>  
- Funcionamento (Se funciona ou não)
- Qualidade do código (o código está limpo? Usou bons nomes de variáveis? Fez bom uso de abstrações? Etc)
- Bom uso das estruturas e algoritmos que vimos
- Explicação sobre o que fizeram
  
Cada grupo terá de 3-5min para mostrar funcionando e explicar, de forma sucinta, o que fizeram

Testes usando o usário Helena (helena42)

quantidade_seguidores('helena42') --> Seguidores da Helena: 18
quantidade_seguindo('helena42') --> Pessoas que a Helena segue: 16
stories('helena42') --> Ordem dos stories da Helena: ['ana_julia22', 'pietro33', 'alice43', 'ana_clara30', 'calebe49', 'caua11', 'davi48', 'gustavo16', 'heloisa37', 'lavinia36','mariana5', 'matheus6', 'melissa42', 'nicolas4', 'rafael38', 'sophia31']
top_influencers(5) --> Top influences: {'maria_alice19': 24, 'henrique12': 22, 'miguel1': 22, 'isis3': 22, 'alice43': 22}
encontra_caminho('helena42', 'isadora45') --> Caminho de Helena até Isadora: helena42 -> ana_clara30 -> isadora45
