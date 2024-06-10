---
title: "Testes dos Requisitos Não-Funcionais"
position: 2
---

&emsp;Este presente documento tem como objetivo detalhar os procedimenos e metodologias utilizados para a realização de testes de requisitps não funcionais da solução desenvolvida pelo grupo Cannabot. Os testes de requisitosnão funcionasi sçao essenciais para assegurar que o sistema atenta às expectativas de desempenhos, usabilidade e segurança, além de outros critérios de qualidade.

&emsp;Os requisitos analisados foram:

- *RNF2 - Latência na Transmissão de Dados:*
A transmissão dos dados e imagens capturadas pela câmera integrada ao roboô deve occorrer com mínima latência, garantinfo uma visualização em tempo real e uma resposta ágil dos operados.

    *Métrica:* A latência média de transmissão de dados não deve exceder 300ms, assegurando uma comunicação eficiente e rápida das informações.

    *Resultado dos Testes:* Durante os testes de uso, foram conduziadas avaliações com quatro usuários distintos, permitindo avaliar a latência durante a transmissão de dados e como isso afeta a solução.

    &emsp;Os resultados dos testes indicaram que apenas um dos quatro usuários não teve problemas significativos com latência, mantendo-se entre 400 e 500ms, enquantos os demais usuários enfrentaram problemas significativos com latência ainda maiores, comprometendo a eficiência da comunciação e a capacidade de respsota em tempo real, fazendo com que a teleoperação fosse prejudicada, ou até mesmo, incapaz de ser executada devido ao delay de transmissão.

    &emsp;Sendo assim, recomenda-se que seja feito uma revisão na configuração de rede para identificar psosíveis gargalos ou problemas de infraestrutura que possam estar contribuindo para a alta latência. Também, recomenda-se avaliar o desemprenho do software de transmissão de dados e imagens para identificar possíveis melhorias e otimizações. Além disso, realizar testes adicionais e com um grupo maior de usuário e em diferentes condições de rede, pode fornecer uma visão mais abrangente dos problemas de latência.
