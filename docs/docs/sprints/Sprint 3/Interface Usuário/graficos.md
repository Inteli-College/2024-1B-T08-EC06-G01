---
title: "Sugestão de gráficos"
sidebar_position: 1
---

# Gráficos 

&emsp;O projeto desenvolvido pelo grupo cannabot conta com um robô turtlebot3 que tem a possibilidade de ser acoplado a um micro-controlador raspeberry pi pico. Essa conexão com o Raspeberry permite a conexão de um sensor de temperatura e gerar um fluxo de dados que podem ser visualizados. 

&emsp;O grupo pensou em alguns possíveis gráficos que podem ser desenvolvidos e que trariam grande vantagem na parte da inteligência do negócio. Permitindo enxergar padrões e tendências no funcionamento do reboiler. 

### Mapa de calor (Heatmap) 

Este é o principal gráfico a ser utilizado em toda solução. Ele permite visualizar por cima do reboiler como anda a temperatura em cada ponto específico. Esse gráfico tem como objetivo ser gerado em tempo real, conforme o robô vai coletando os dados o gráfico vai sendo atualizado e o operador do robô entende como anda a situação do reboiler. 

Na figura abaixo é possível ver o heatmap e como foi pensado a sua implementação.

<div align="center"> 

![](../../../../..\docs\static\img\sprint3\heatmap.png)

Fonte: Elaborado pelo grupo Cannabot
</div>


### Histórico de temperaturas diária 

Outro gráfico que pode ser gerado é um análise diária dos setores do reboilers. Assim, é possível dividir o reboiler que é um círculo em oito quadrantes e cada um desses quadrantes corresponde a uma barra no gráfico e lá é feito a média da temperatura. 
Assim, o operador do sistema consegue ter uma noção se a temperatura dentro do reboiler é homôgenea ou há variação em algum setor específico. Com base nessas informações é possível tomar uma decisão mais assertiva se é hora ou não de limpar o reboiler. 

Na figura abaixo é possível ver o esquema de como é feita a divisão do reboiler em quadrantes e o gráfico com a média de temperatura para cada região.

<div align="center"> 

![Divisão do Reboiler](../../../../..\docs\static\img\sprint3\circle.png)
Fonte: Elaborado pelo grupo Cannabot
</div>

<div align="center"> 

![Média da temperatura por setor](../../../../..\docs\static\img\sprint3\grafico1.png)
Fonte: Elaborado pelo grupo Cannabot
</div>

### 