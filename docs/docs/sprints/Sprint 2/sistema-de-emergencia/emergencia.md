---
title: Desenvolvimento do sistema de emergência do Robô
sidebar_position: 1
description : Desenvolvimentos do robô referente a segunda sprint.
---


## Introdução 

&emsp;Ao desenvolver projetos que envolvem a execução de robôs teleoperados, é de extrema importância pensar em maneiras para interromper a operação do robô em qualquer momento e de forma fácil e prática, com a finalidade de evitar possíveis eventualidades e riscos que podem trazer problemas ao projeto, para que os testes do protótipo sejam feitos com segurança no ambiente, e também para facilitar a interrupção da operação caso o robô não esteja realizando os comandos em conformidade com o que era esperado. 

## Sistema de Emergência

&emsp;A partir disso, um mecanismo de emergência foi criado neste projeto, em que permite o operador enviar um comando de parada imediata ao robô através da CLI para o TurtleBot, em caso de qualquer eventualidade ou risco observado.

Na figura abaixo, é possível ver o código que faz com que o robô pare completamente.

<p align="center"><b> Figura Código da parada de Emergência </b></p>
<div align="center">
  ![](../../../../static/img/sprint2/stop-code.png)
  <p><b>Fonte:</b> Elaborado por Cannabot</p>
</div>

&emsp;Para interromper a operação do robô quando estiver executando os comandos designados para o mesmo, é preciso apenas escolher a opção *stop* na CLI. Com isso, a execução do script é interrompida imediatamente e o robô para de realizar suas ações. Ao designar a função de interromper a operação com o uso de apenas uma tecla, o mecanismo de emergência pode ser ativado com facilidade e rapidez, o que promove a eficácia desse mecanismo.

Na figura abaixo, é possível ver qual a resposta que a CLI retorna após clicar no botão que aciona a parada de emergência.

<p align="center"><b> Figura Parada de Emergência </b></p>
<div align="center">
  ![](../../../../static/img/sprint2/cli-stop.png)
  <p><b>Fonte:</b> Elaborado por Cannabot</p>
</div>

## Conclusão

&emsp;Dessa forma, é possível dizer que a implementação de um sistema de emergência ao robô teleoperado é crucial para garantir a segurança durante os testes e as operações do protótipo. Ao permitir que o operador interrompa imediatamente as operações do robô através de um comando simple, a tecla ESQ do computador, potenciais riscos e eventualidades podem ser mitigados de forma eficaz. Essa abordagem não apenas proporciona uma camada adicional de segurança para o ambiente de trabalho, mas também oferece uma maneira prática de garantir que o robô opere conforme o esperado, contribuindo assim para o sucesso do projeto como um todo.