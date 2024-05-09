---
title: CLI
sidebar_position: 1
---

# CLI: Command-Line Interface
### O que é 'CLI' afinal?

&emsp;CLI ou command-line interface é uma área de interação simplificada. Usalamente ela é integrada a aplicação no ínicio do projeto para conseguir interagir com a solução e realizar testes de movimentação simplificadas. Isso revela sua importância em ser desenvolvida para escalar o projeto ao decorrer de seu desenvolvimento e integração com uma aplicação frontend no futuro.

&emsp;A construção da CLI do grupo Cannabot foi projetada para que seja o mais simples e intuitivo possivel para o usuario que irá testar a aplicação nesse ponto do projeto, pensamos tambem que como a CLI é um passo anterior para a aplicação frontend não seria de grande valia aplicar um esforço muito grande em sua construção. Veja abaixo a primeira versão da command-line interface do grupo cannabot e como foi seu processo de construçaão a partir do seu própio código:

### Interface

&emsp;Ao rodar nosso pacote ROS, será exibido no terminal nossa interface gráfica capaz de interagir com a solução. Podemos observar as seguintes opções:

<p align="center">Figura Command-Line Interface 1:</p>
<div align="center">
  ![CLI](../../../../static/img/sprint2/cli-principal.png)
  <p><b>Fonte:</b> Elaborado por Cannabot</p>
</div>

&emsp;Ao selecionar a opção 'right' será exibido uma segunda pergunta para inserir o prompt, que seria de quantos graus para direita você deseja virar o robô:
<p align="center">Figura Command-Line Interface 2:</p>
<div align="center">
  ![CLI](../../../../static/img/sprint2/cli-right.png)
  <p><b>Fonte:</b> Elaborado por Cannabot</p>
</div>

&emsp;Ao selecionar a opção 'left' também será exibido uma segunda pergunta para inserir o prompt, que seria de quantos graus para direita você deseja virar o robô:
<p align="center">Figura Command-Line Interface 3:</p>
<div align="center">
  ![CLI](../../../../static/img/sprint2/cli-left.png)
  <p><b>Fonte:</b> Elaborado por Cannabot</p>
</div>

&em
### Código

<p align="center">Figura Command-Line Interface code 4:</p>
<div align="center">
  ![CLI](../../../../static/img/sprint2/if-main.png)
  <p><b>Fonte:</b> Elaborado por Cannabot</p>
</div>

<p align="center">Figura Command-Line Interface code 5:</p>
<div align="center">
  ![CLI](../../../../static/img/sprint2/def-main.png)
  <p><b>Fonte:</b> Elaborado por Cannabot</p>
</div>

<p align="center">Figura Command-Line Interface code 6:</p>
<div align="center">
  ![CLI](../../../../static/img/sprint2/def-menu.png)
  <p><b>Fonte:</b> Elaborado por Cannabot</p>
</div>

### Conclusão



