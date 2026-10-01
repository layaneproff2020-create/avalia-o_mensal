O primeiro arquivo que eu criei foi o produto.py. A ideia era ter uma classe que representasse um produto de verdade, tipo "Arroz 5kg" ou "Feijão 1kg". Então, dentro dela, eu coloquei três informações: a descrição (o nome do produto), o preço unitário (quanto custa cada um) e o estoque (quantos têm disponíveis).

Mas só guardar informação não bastava. Eu precisava que o produto soubesse se controlar sozinho. Então, criei um método chamado decrementar_estoque. Quando alguém tenta comprar, esse método verifica se tem quantidade suficiente. Se tiver, ele subtrai do estoque e devolve "verdadeiro". Se não tiver, ele avisa que faltou e devolve "falso". Assim, o próprio produto impede que o sistema venda algo que não existe.

Arquivo 2: item_venda.py

Depois, criei o arquivo item_venda.py. Aqui eu pensei: "uma venda não é feita só de produtos soltos, ela é feita de itens". Por exemplo, se um cliente compra 2 arrozes, aquilo é um item da venda. Então, a classe ItemVenda recebe um objeto do tipo Produto e uma quantidade.

Para isso, precisei importar a classe Produto lá do arquivo anterior, com um from produto import Produto. Aí, dentro dessa classe, criei um método chamado calcular_subtotal, que simplesmente multiplica o preço do produto pela quantidade. Tipo, se o arroz custa 25 reais e o cliente levou 2, o subtotal é 50 reais. Esse arquivo é curtinho, mas essencial, porque ele faz a ponte entre o produto e a venda.

Arquivo 3: venda.py
O terceiro arquivo foi o venda.py. Esse é o cérebro do sistema. A classe Venda é quem junta tudo. Quando eu crio uma venda, ela já pega automaticamente a data e a hora atual usando o datetime, inicia o valor total como zero e cria uma lista vazia de itens.

Aí vêm os métodos principais. O adicionar_item é o mais importante: ele primeiro tenta decrementar o estoque do produto. Só se o produto tiver estoque, ele cria um novo ItemVenda, coloca na lista e recalcula o total. Se não tiver estoque, ele avisa e não deixa adicionar.

Também criei um método chamado remover_item, porque pensei: "e se o cliente desistir de um item?" Então, esse método procura o produto na lista, remove ele e devolve a quantidade ao estoque do produto. Isso é importante para o estoque nunca ficar errado.

E tem o calcular_total, que percorre todos os itens da lista e soma os subtotais, atualizando o valor total da venda.


Arquivo 4: testar_sisvenda.py
Por fim, criei o arquivo testar_sisvenda.py. Eu não coloquei o nome de main.py porque você já tinha um arquivo com esse nome, então resolvi dar um nome mais específico para não dar conflito.

Esse arquivo é o que a gente chama de "script de teste" ou "ponto de entrada". É aqui que eu simulo o uso real do sistema. Eu criei três produtos com estoques diferentes, criei uma venda, adicionei alguns itens, tentei adicionar um item sem estoque (de propósito, para ver se o sistema bloqueava), removi um item e imprimi o resumo final. Tudo isso para provar que as classes estão conversando direitinho.
