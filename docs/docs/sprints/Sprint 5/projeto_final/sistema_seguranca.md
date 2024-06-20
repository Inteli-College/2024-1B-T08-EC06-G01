---
title: "Sistema de segurança"
position: 3
---

Este documento descreve o Sistema de Segurança desenvolvido para o projeto Cannabot, com o objetivo primordial de assegurar operações seguras do robô, bem como a proteção dos operadores envolvidos. As principais medidas implementadas incluem um botão de parada de emergência e um sistema de detecção de obstáculos com parada automática do robô, visando proporcionar maior controle operacional e prevenir acidentes durante a execução do projeto. A seguir, apresentaremos uma análise detalhada do funcionamento de cada uma dessas medidas de segurança.

## Botão de parada de emergência

Durante a Sprint 2, a equipe Cannabot apresentou a primeira versão da funcionalidade de parada de emergência do robô, inicialmente implementada através da interface de linha de comando (CLI). Na Sprint 3, com a introdução da interface de usuário, foram realizadas alterações significativas na forma de ativação dessa função.

[Tela da central de controle]()

No projeto final, a ativação da parada de emergência é realizada através da interface, como a imagem acima ilustra. Ao clicar no botão "Modo de Emergência" na tela "Central de Controle" do frontend, o usuário aciona o serviço de emergência. Este serviço, ao ser requisitado, executa a função de parada do robô, fechando a conexão. Dessa forma, mesmo que haja tentativas de movimentar o robô através dos comandos do frontend, ele permanecerá imóvel. A única forma de restabelecer o funcionamento normal é reiniciando o robô manualmente.

Para visualizar com maior precisão o código relacionado ao processo acesse a documentação refere a [Sprint 3]()




## Detecção de obstáculo e parada imediata

Uma abordagem crucial para garantir a segurança do sistema foi implementada através da detecção de obstáculos à frente ou atrás do robô. Essa funcionalidade desempenha um papel fundamental na prevenção de colisões e na garantia da integridade do equipamento e do ambiente ao seu redor.

A detecção de obstáculos permite que o robô reaja de forma proativa, impedindo qualquer movimento em direção a esses obstáculos, mesmo que o usuário tente comandar essa ação. Essa capacidade é especialmente vital em ambientes dinâmicos e imprevisíveis.

Para incorporar essa funcionalidade, o primeiro passo foi utilizar o Lidar. O LIDAR (Light Detection and Ranging) é um sensor que mede distâncias e detecta objetos ao redor do robô. Esse sensor emite um feixe de laser que varre o ambiente, calculando o tempo que leva para o feixe refletir de volta ao sensor após atingir um objeto. No modelo do Turtlebot3, o robô utilizado nesta prova de conceito, o Lidar já está integrado.

Com base nos dados fornecidos pelo Lidar, foi possível implementar uma lógica que impede a colisão do robô a partir dos dados recebidos.
Nessa lógica, é criada uma lista contendo todos os registros do lidar em uma varredura de 360 graus. Como essa lista é dinâmica, foi criada uma outra variável chamada "que armazena o tamanho dessa lista. A partir dessa informação, é possível implementar a lógica para determinar se há obstáculos à frente ou atrás do robô.

A lógica empregada consiste em dividir a lista em quatro partes para definir os quadrantes que compõem a circunferência do lidar. A partir disso, são criadas as variáveis A e B, que representam, respectivamente, as delimitações do primeiro e do último quadrante, partindo do ângulo 0. Para detectar se um obstáculo está atrás do robô, basta verificar se seu índice na lista é maior que A e menor que B, ou seja, se ele está no segundo ou terceiro quadrante. Caso contrário, o obstáculo está à frente do robô.

É importante ressaltar que consideramos uma distância de 0.2 metros como critério para determinar a presença ou não de um obstáculo.

No código a seguir, as condições para a movimentação do robô são definidas. No caso "forward" (avançar), o robô só pode se locomover se o sensor lidar indicar que há um obstáculo atrás ou se não houver obstáculo. Essa mesma lógica é aplicada quando o movimento é para trás.

Essa abordagem dinâmica permite que o robô ajuste seu comportamento de acordo com a presença de obstáculos, garantindo uma navegação segura e eficiente em ambientes desafiadores. O monitoramento constante do Lidar e a adaptação contínua do comportamento do robô contribuem significativamente para a segurança e a confiabilidade do sistema como um todo.