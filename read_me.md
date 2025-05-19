### Teste Técnico: Programa Trainee triggo.ai

### Objetivo:
Este notebook contém a análise do dataset público de e-commerce brasileiro da Olist, com o objetivo de extrair insights valiosos para auxiliar nas decisões estratégicas do negócio, conforme solicitado no teste técnico.

### - Preparação dos Dados:

## Célula 1: Importação e Exploração Inicial
Importação das bibliotecas e carregamento dos DataFrames dos arquivos CSV para o dicionário `dfs`, seguido de uma primeira exploração básica de cada DataFrame (primeiras linhas, `info()`, `describe()`, identificação de nulos, duplicados e colunas).

## Célula 2: Conversão de Tipos de Dados
Conversão dos tipos de dados de várias colunas nos DataFrames carregados para tipos mais apropriados (`category`, `datetime`, `int`, `float`).

## Célula 3: Conexão SQLite, Carregamento e Tratamento de Nulos
Conexão com o banco de dados SQLite (`olist.db`), carregamento de todos os DataFrames do dicionário `dfs` para tabelas correspondentes no SQLite e tratamento dos valores nulos.
**Observações:**
* Optei por `-1` em valores nulos na tabela `olist_products_dataset`, pois a inserção de texto alteraria o tipo da coluna.
* Ao analisar a tabela `olist_orders_dataset`, observei valores nulos em algumas colunas relacionadas ao progresso do pedido: `order_approved_at`, `order_delivered_carrier_date` e `order_delivered_customer_date`.
* Decidi **manter** esses valores nulos, pois sua ausência geralmente contém informações significativas sobre o status do pedido:
    * `order_approved_at`: Nulo pode indicar que o pedido não foi aprovado (cancelamento ou problema no pagamento).
    * `order_delivered_carrier_date`: Nulo sugere que o pedido ainda não foi entregue à transportadora (status: `created`, `invoiced`, `processing`).
    * `order_delivered_customer_date`: Nulo indica que o pedido ainda não foi entregue ao cliente (status: em trânsito, `shipped`).
* Manter os nulos preserva a integridade dos dados e permite análises futuras considerando o status do pedido. Análises que dependam dessas colunas devem filtrar os dados pelo `order_status` para garantir precisão.

### - Análise Exploratória de Dados:

### Célula 4: Volume de Pedidos por Mês e Sazonalidade
**Pergunta:** Qual o volume de pedidos por mês? Existe sazonalidade nas vendas?
**Resposta:** O mês com o maior volume de pedidos registrado foi novembro de 2017. Em relação à sazonalidade, há uma possível alta no período da Black Friday, mas é difícil confirmar com os dados disponíveis.

### Célula 5: Distribuição do Tempo de Entrega
**Pergunta:** Qual a distribuição do tempo de entrega dos pedidos?
**Resposta:** A distribuição do tempo de entrega dos pedidos concentra-se em prazos mais curtos, com a maioria sendo entregue em até 15 dias. O tempo médio de entrega é de aproximadamente 12 dias, e a mediana é de 10 dias, indicando que metade dos pedidos é entregue em 10 dias ou menos.

### Célula 6: Relação entre Frete e Distância
**Pergunta:** Qual a relação entre o valor do frete e a distância de entrega?
**Resposta:** A relação entre o valor do frete e a distância de entrega é positiva, mas moderada, com um coeficiente de correlação de aproximadamente 0.38. Isso sugere que, em geral, quanto maior a distância, maior tende a ser o frete.

### Célula 7: Categorias Mais Vendidas por Faturamento
**Pergunta:** Quais são as categorias de produtos mais vendidas em termos de faturamento?
**Resposta:** A categoria de "cama, mesa e banho" lidera em faturamento, seguida de perto por "beleza e saúde" e "informática e acessórios".

### Célula 8: Estados com Maior Valor Médio de Pedido
**Pergunta:** Quais estados brasileiros possuem o maior valor médio de pedido?
**Resposta:** Com base nos resultados, os estados brasileiros com o maior valor médio de pedido são: Paraíba, Acre, Rondônia, Amapá e Alagoas.

### - Solução de Problemas de Negócio:

## Célula 9: Análise de Retenção:
**Pergunta:** Calcule a taxa de clientes recorrentes. Considere um cliente recorrente aquele que fez mais de um pedido no período analisado. Quais insights podemos extrair destes dados?
**Resposta:** O crescimento das vendas se baseia exclusivamente na aquisição de novos compradores, pois não foi identificado recompras de produtos pelos mesmos clientes no período analisado. É importante implementar uma estratégia de fidelização de clientes e investigar o motivo da ausência de recompra.

## Célula 10: Predição de Atraso:
**Pergunta:** Crie um modelo simples para prever se um pedido será entregue com atraso. Defina o que seria um pedido atrasado (baseado nas colunas disponíveis). Use os campos relevantes para criar features para seu modelo. Divida o dataset em treino e teste. Implemente um modelo de classificação simples (pode usar Regressão Logística, Random Forest ou outro de sua escolha). Avalie a performance do modelo e explique os resultados.
**Resposta:** Um pedido é considerado atrasado quando sua data de entrega (`order_delivered_customer_date`) ocorre após a data estimada para entrega (`order_estimated_delivery_date`). Baseado em um limiar de 7 dias no tempo estimado de entrega, o modelo apresentou uma alta acurácia de 91%. No entanto, essa alta acurácia é enganosa devido ao desbalanceamento das classes (muito mais entregas no prazo do que atrasos). A precisão para a classe 'atraso' foi de apenas 31%, e o recall de apenas 5%, indicando que o modelo é ineficaz em identificar atrasos.

## Célula 11: Segmentação de Clientes:
**Pergunta:** Utilize técnicas de clustering para segmentar os clientes em grupos. Analise o comportamento de cada grupo e sugira estratégias de marketing específicas para cada um.
**Resposta:** Dada a constatação de que todos os clientes realizaram apenas um pedido no período analisado, a segmentação foi realizada com base em duas características da compra única de cada cliente: o valor total gasto e o número de categorias de produtos adquiridas.

Após calcular essas features e normalizá-las, a visualização dos dados em um gráfico de dispersão (valor gasto normalizado vs. número de categorias normalizado) sugere a presença de distintos grupos de clientes:

* **Grupo 1: Alto Gasto, Poucas Categorias:** Clientes que realizaram uma compra de valor elevado, concentrando-se em um número limitado de categorias de produtos.
  **Comportamento:** Compradores com necessidades específicas ou interesse em nichos de produtos, dispostos a investir um valor maior em suas áreas de interesse.
  **Estratégia de Marketing:** Foco em ofertas direcionadas dentro das categorias compradas, possíveis programas de fidelidade para essas categorias específicas, e comunicação personalizada sobre novidades e produtos relacionados aos seus interesses.

* **Grupo 2: Baixo Gasto, Poucas Categorias:** Clientes que realizaram uma compra de valor baixo, também com foco em poucas categorias.
  **Comportamento:** Compradores mais sensíveis a preço ou com necessidades pontuais e limitadas.
  **Estratégia de Marketing:** Campanhas de remarketing com produtos relacionados à sua compra inicial, ofertas para aumentar o valor do carrinho (como combos ou frete grátis acima de um certo valor), e sugestões de produtos de outras categorias que possam ser de interesse.

* **Grupo 3: Gasto Variável, Mais Categorias:** Clientes que realizaram uma compra com um valor que pode variar, mas exploraram uma gama maior de categorias de produtos.
  **Comportamento:** Compradores mais exploradores ou com necessidades diversificadas em sua única compra.
  **Estratégia de Marketing:** Newsletter com novidades em diversas categorias, promoções amplas em diferentes tipos de produtos para incentivar novas descobertas, e possíveis recompensas por explorar novas categorias em futuras compras.

**Conclusão:**

Embora a ausência de dados de recompra limite a análise do comportamento do cliente ao longo do tempo, esta segmentação inicial oferece insights valiosos sobre os diferentes perfis de compradores únicos. As estratégias de marketing sugeridas visam atender às características distintas de cada grupo, buscando otimizar o engajamento e incentivar futuras compras, caso esses clientes retornem à plataforma. 

## Célula 12: Análise de Satisfação do Cliente:

**Pergunta:** Explore a relação entre a nota de avaliação dos clientes e diferentes aspectos como categoria do produto, tempo de entrega, valor do pedido, etc. Identifique fatores que mais impactam na satisfação do cliente.
**Resposta:** A análise da satisfação do cliente (via `review_score`) em relação a diferentes fatores revela que **o tempo de entrega, especialmente o atraso, é um dos principais determinantes da insatisfação**. Pedidos atrasados recebem notas significativamente mais baixas. O tempo de entrega real também apresenta uma leve correlação negativa com a avaliação.

Além disso, a **categoria do produto influencia a satisfação**, com algumas categorias consistentemente recebendo notas mais altas ou mais baixas, sugerindo que a qualidade ou expectativas ligadas ao tipo de produto são relevantes.

Por outro lado, o **valor do pedido não demonstrou uma correlação linear significativa com a nota de avaliação**, indicando que o preço em si não é um fator primário na satisfação geral.

**Em resumo, para aumentar a satisfação, a prioridade deve ser a redução de atrasos na entrega e a investigação das categorias de produtos com avaliações mais baixas.**

## Célula 13: Dashboard interativo:
Após diversas tentativas de implementação do mapa de calor para visualizar a concentração de vendas por estado do Brasil utilizando as funcionalidades nativas da biblioteca Plotly Express, Encontrei certa dificuldade na renderização precisa e colorida das subdivisões estaduais dentro do escopo geográfico da América do Sul. Diante dessa limitação técnica e visando a entrega de um dashboard funcional e informativo, optei por substituir temporariamente a visualização do mapa de calor por um gráfico de barras horizontal. Esta alternativa permite apresentar de forma clara e comparativa o volume total de vendas por estado, garantindo a compreensão da distribuição geográfica das vendas, embora sem a representação espacial direta sobre um mapa. A decisão visa priorizar a clareza e a funcionalidade do dashboard dentro das restrições identificadas durante o processo de desenvolvimento.