---
title: Arquitetura
sidebar_position: 2
description : Arquitetura referente a segunda sprint.
---


## Introdução 

Antes de iniciar a explicação da arquitetura é recomendado ao leitor que leia a secção *Segunda sprint*. Neste texto existem explicações em mais detalhes sobre os motivos das alterações que foram realizadas no projeto. 

## Mudança de escopo 

Após conversas com funcionários da Atvos, foi explicado que o processo de manutenção é realizado semanalmente e há necessidade de que seja algo bem rápido. 

Assim, ao invés de ser um robô que realiza o mapeamento dos tubos e em seguida insere uma câmera endoscópica em cada tubo para verificar se ainda existem vestígios de sujeira, o grupo optou por um caminho mais simples e que gera valor em outras frentes para a empresa.

O novo robô tem como objetivo ficar circulando por dentro do reboiler em funcionamento e medir informações internas como temperatura, concentração de açúcares e qualquer outro tipo de medição que auxilie a manutenção dos reboilers.

Em suma, o objetivo do robô é ficar andando pelo reboiler em funcionamento, gerar um fluxo de dados dessa medição e permitir que exista uma interface para que o usuário consiga interagir com o robô e visualizar os dados.

## Vantagens do novo projeto 

A mudança de escopo muda o objetivo que o robô tem. Ao invés de uma solução que garante a qualidade da limpeza.  Foi feito a mudança para um robô que gera dados e ajuda na tomada de decisões de manutenção. São dois os principais ganhos que essa nova arquitetura atinge. 

***Geração de dados*** Com o aumento exponencial da capacidade computacional dos computadores e um ambiente de negócios cada vez mais competitivo, um projeto que gera um fluxo de dados tem grande valor para a companhia. Primeiramente, é possível criar um dashboard que permite visualizar em tempo real os dados de dentro do reboiler e ajudar na tomada de decisão. Além disso, um fluxo de dados permite a criação de um futuro data warehouse e a implementação de modelos de IA proprietários que ajudam na tomada de decisão baseada em dados. 

***Aumento de produtividade*** Com um robô que é capaz de coletar informações intermitentes sobre o ambiente industrial em que está inserido, é possível criar um dashboard que permite visualizar em tempo real os dados de dentro do reboiler e ajudar na tomada de decisão se o reboiler já chegou a um ponto em que é necessário interromper a operação. Assim, o reboiler só é desligado no momento correto e garante o máximo de produtividade sem desligamentos desnecessários.
