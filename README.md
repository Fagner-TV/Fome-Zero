# Fome-Zero-
# 1.	Problema de negócio
Você acaba de ser contratado como Cientista de Dados da empresa Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados! A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.
O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:

# Geral 
1. Quantos restaurantes únicos estão registrados? 
2. Quantos países únicos estão registrados? 
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas? 
5. Qual o total de tipos de culinária registrados? 

# País 
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados? 
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados? 
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas? 
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega? 
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas? 8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada? 
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada? 
11. Qual a média de preço de um prato para dois por país?
# Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados? 
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4? 
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5? 
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois? 
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas? 
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas? 
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online? 

# Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações? 
2. Qual o nome do restaurante com a maior nota média? 
3. Qual o nome do restaurante que possui o maior valor de um prato para duas pessoas? 
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação? 
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas? 
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
# Tipos de Culinária 
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação? 
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação? 
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação? 
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação? 
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação? 
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação? 
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação? 
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação? 
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação? 
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas? 
12. Qual o tipo de culinária que possui a maior nota média? 
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

# O objetivo desse projeto é que fosse gerado um dashboard que permitisse visualizar as principais informações para o CEO, para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.

# 2.	Premissas assumidas para análises:
A.	Markeplace de restaurantes foi o modelo de negócio.
B.	As 3 visões escolhidas foram: Visão pedidos, Visão Culinárias e Visão Cidades. 

# 3.Estratégia da solução:
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:
A.	Visão Países 
B.	Visão Culinárias 
C.	Visão Cidades

# Cada visão é representada pelo seguinte conjunto de métricas.
# 1.	Visão Países
A.	Quantidade de restaurantes registrado por países.
B.	Quantidade de cidades registradas por país.
C.	Média de avaliações feitas por país.
D.	Média de preço de um prato para duas pessoas por país.

# 2. Visão Culinária
A. Melhores restaurantes por tipo de culinárias.
B. Top 10 restaurantes com melhor avaliação
c. Top 10 melhores culinárias, filtrando por país e culinária
d. Top 10 piores culinárias, filtrando por país e culinária

# 3. Visão Cidades
A. Top 10 de cidades com restaurantes
B. Top 7 de restaurantes com a média acima de 4.0
C. Top de restaurantes com a média abaixo de 2.5
D. Top 10 cidades mais restaurantes com culinárias distintas 

# 4. Top 3 insights de dados
A. Os países que possuem a maior quantidade de restaurantes, possuem também a maioria de restaurantes por cidade e melhor avaliado. 
B. E os top 10 de restaurantes possuem um média de valor baixo de parto para duas pessoas. 
C. Podemos verificar que possuem uma variedade de 165 culinárias cadastradas na base de dados.

# 5. Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet. O painel pode ser acessado através desse link: https://fome-zero-dash.streamlit.app/

# 6. Conclusão
O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO. 
Da visão da Empresa, podemos concluir que o número de restaurantes cadastrados na base de dados é bem grande, temos uma grande variedade de culinárias e podemos avaliar onde estão os melhores restaurantes avaliados e como os piores, por região, cidade e país.   

# 7. Próximo passos 
A. Reduzir o número de métricas. 
B. Criar novos filtros. 
C. Adicionar novas visões de negócio.


