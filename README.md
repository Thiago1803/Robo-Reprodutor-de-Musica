# Trabalho de Inteligência Artificial

O robô foi desenvolvido com aa premissa de ajudar os pais no entretenimento de seus filhos. O robô possuí a habilidade de conversar com o usuário e pode aceitar pedidos para reprodução de músicas.

A arquitetura se dá da seguinte maneira: 

<p align="center">
  <img src="https://github.com/Thiago1803/TRABALHOIA/assets/64339671/12455c20-a97e-44d2-829e-9972dea6eb67" alt="logo" width="220" height="500">
</p>

### CONTROLLER

**control.py**

Em resumo, o código runRobot() simplesmente importa o módulo sense_music e chama a função speech_to_text() desse módulo. O que exatamente a função speech_to_text() faz depende da implementação dentro do módulo sense_music, que não está presente no código fornecido. Para entender completamente o que esse código faz, você precisaria examinar o conteúdo do módulo sense_music.


**think_music.py**

Ela define funções para buscar e reproduzir músicas, reproduzir playlists, controlar o estado da reprodução (pausar, continuar, parar), e lidar com comandos de voz para interagir com o programa. A variável global pastaPlaylistAtual é usada para rastrear qual playlist está sendo reproduzida no momento.

### MODEL

Essa seção armazena as playlists e os áudio utilizados para a comunicação com o usuário

### VIEW
**act_music.py**
Em resumo, esta classe oferece funções básicas para controlar a reprodução de música, incluindo reproduzir, pausar, parar, continuar, alterar o volume e pular para a próxima música em uma lista de reprodução. Ela utiliza a biblioteca pygame para gerenciar a reprodução de áudio.

**act_talk.py**
A principal finalidade dessa classe é permitir que você envie mensagens de texto para serem reproduzidas como fala em um sistema de saída de áudio, como um assistente de voz. Ela usa o gTTS para a conversão de texto em fala e o pygame para a reprodução do áudio resultante.

**sense_music.py**
Em resumo, essa classe cria uma interface para interagir com um assistente virtual por meio de comandos de voz. Ela permite ao usuário controlar a reprodução de música e executar outras ações com base no reconhecimento de fala. O assistente virtual "Beto" responde aos comandos de voz do usuário e interage com as funções relacionadas à música ou outras ações definidas no arquivo JSON.


### main.py
Em resumo, esse código é parte de um programa que utiliza a biblioteca pygame para reproduzir música e interage com o usuário por meio de comandos de voz. Ele inicializa o Pygame, executa a interação por voz (provavelmente com a função menuSentir), e depois encerra o Pygame quando a interação é concluída. A função falarMensagens é usada para fornecer mensagens de áudio ao usuário. O comportamento exato do programa depende da implementação das funções importadas, que não estão presentes neste código.
