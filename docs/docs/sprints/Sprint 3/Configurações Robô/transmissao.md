---
title: "Transmissão de imagens"
sidebar_position: 1
description: Nessa seção, iremos abordar a transmissão de imagens do robô Turtlebot 3, que é um dos principais componentes do projeto.
---

# Transmissão de imagens

## Introdução

&emsp;Dentre as funcionalidades implementadas no robô na sprint 3, uma delas é a implementação de uma câmera para a realização da transmissão de vídeo em tempo real. A câmera embutida no robô captura imagens que são transmitidas para um computador. Isso permite ao operador visualizar em tempo real o que o robô está vendo, o que proporciona dados valiosos para a Atvos sobre a limpeza dos tubos do reboiler.

### Câmera do robô

<div align="center"> 

![](../../../../..\docs\static\img\sprint3\robocamera.png)

Fonte: Elaborado pelo grupo Cannabot
</div>

&emsp;A câmera utilizada é a mesma presente no robô Dobot Magician Lite. Ela é conectada ao Raspberry Pi 4 presente no turtlebot, e assim é configurada para realizar a transmissão das imagens. Ela está posicionada na parte da frente do robô, onde foi fixada com um suporte feito numa impressora 3D, para garantir a qualidade das gravações.
    
### Transmissão do vídeo

<div align="center"> 

![](../../../../..\docs\static\img\sprint3\robovideo.png)

Fonte: Elaborado pelo grupo Cannabot
</div>

&emsp;Nesta imagem, é possível ver a transmissão do vídeo em que a câmera embutida no robô transmite em tempo real. A partir do momento que o código é inicializado, a câmera começa e funcionar e enviar as imagens para o computador. Essa transmissão de imagens é feita a partir do websockets, uma tecnologia de comunicação bidirecional que permite a transmissão de dados entre um navegador web e um servidor de maneira eficiente e em tempo real.

### Latência

<div align="center"> 

![](../../../../..\docs\static\img\sprint3\latencia.png)

Fonte: Elaborado pelo grupo Cannabot
</div>

&emsp;A partir desta outra imagem, é possível ver novamente a tela em que as imagens estão sendo transmitidas. Abaixo do quadro com o vídeo da transmissão, há uma estimativa da latência do processo de aquisição, processamento e envio da imagem. 

&emsp;Na imagem acima, a latência se encontra na casa dos 20 mil milissegundos. Essa é uma estimativa ruim, mas vale ressaltar que no momento desta captura de tela a internet da faculdade estava relativamente fraca. Durante a maioria dos testes o robô apresentou uma latência de aproximadamente 500 milissegundos. 

&emsp;Dessa forma, a equipe conseguiu implementar a transmissão de imagens em tempo real no robô, para fazer o monitoramento e controle dos processos de limpeza dos tubos do reboiler.
Esta funcionalidade não só melhora a capacidade de supervisão do operador, mas também proporciona à Atvos dados visuais que podem ser analisados para otimizar ainda mais os processos de limpeza dos reboilers.