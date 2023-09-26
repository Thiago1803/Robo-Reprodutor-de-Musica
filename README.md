# Trabalho de Inteligência Artificial

O robô foi desenvolvido com a premissa de ajudar os pais no entretenimento de seus filhos. O robô possuí a habilidade de conversar com o usuário e pode aceitar pedidos para reprodução de músicas.

## Arquitetura de Software

<p align="center">
  <img src="https://github.com/Thiago1803/TRABALHOIA/assets/64339671/dd93831c-94e9-4de7-a2b4-3f036c223774" alt="logo" width="180" height="420">
</p>


## Diagrama de classes


![ClassesIA2](https://github.com/Thiago1803/TRABALHOIA/assets/64339671/d8296ab7-a689-4efd-a796-a4e1022c16a8)


### CONTROLLER

**control.py**

Em resumo, a função runRobot() simplesmente importa o módulo sense_music e chama a função speech_to_text() desse módulo. A função speech_to_text() faz exatamente o que o nome diz, o usuário fala algo é ela transcreve as palavras para uma lista.


**think_music.py**

Ela define funções para buscar e reproduzir músicas, reproduzir playlists, controlar o estado da reprodução (pausar, continuar, parar), e lidar com comandos de voz para interagir com o programa.

### MODEL

Essa seção armazena as playlists, os áudio utilizados para a comunicação com o usuário e os comandos do robô.

### VIEW
**act_music.py**
Em resumo, esta classe oferece funções básicas para controlar a reprodução de música, incluindo reproduzir, pausar, parar, continuar, alterar o volume e pular para a próxima música em uma lista de reprodução. Ela utiliza a biblioteca pygame para gerenciar a reprodução de áudio.

**act_talk.py**
A principal finalidade dessa classe é permitir que você envie mensagens de texto para serem reproduzidas como fala em um sistema de saída de áudio, como um assistente de voz. Ela usa o gTTS para a conversão de texto em fala e o pygame para a reprodução do áudio resultante.

**sense_music.py**
Em resumo, essa classe cria uma interface para interagir com um assistente virtual por meio de comandos de voz. Ela permite ao usuário controlar a reprodução de música e executar outras ações com base no reconhecimento de fala. O assistente virtual "Eva" responde aos comandos de voz do usuário e interage com as funções relacionadas à música ou outras ações definidas no arquivo JSON.


### main.py
Em resumo, esse código é parte de um programa que utiliza a biblioteca pygame para reproduzir música e interage com o usuário por meio de comandos de voz. Ele inicializa o Pygame, executa a interação por voz (provavelmente com a função menuSentir), e depois encerra o Pygame quando a interação é concluída. A função falarMensagens é usada para fornecer mensagens de áudio ao usuário. O comportamento exato do programa depende da implementação das funções importadas, que não estão presentes neste código.


## Bibliotecas externas utilizadas

### Pygame

A biblioteca Pygame é uma biblioteca de código aberto para Python que é amplamente utilizada para desenvolver jogos e aplicações multimídia interativas. Ela fornece uma série de recursos e funcionalidades que tornam mais fácil a criação de jogos 2D e aplicações gráficas. No nosso projeto nós utilizamos o recurso de controle de áudio que permitiu a reprodução dos sons e música, além de controlar a reprodução de áudio de maneira simples.

### Google Text-to-Speech

A biblioteca "gTTS" (Google Text-to-Speech) é uma biblioteca Python que permite converter texto em fala usando a tecnologia de síntese de fala do Google. Nós utilizamos o gTTS, para criar os arquivos de áudio a partir de texto, o que é útil em uma variedade de aplicativos, como assistentes virtuais, aplicativos de acessibilidade, geração de áudio para vídeos e consequentemente no nosso projeto.

### Speech Recognition

A biblioteca "speech_recognition" é uma biblioteca Python que fornece uma interface simples para trabalhar com reconhecimento de fala (speech recognition). Ela permite que você integre facilmente recursos de reconhecimento de voz em seus programas Python, tornando possível converter fala em texto. Nós utilizamos para capturar áudio do microfone em tempo real e convertê-lo em texto.

### OS
A biblioteca os é uma biblioteca padrão do Python que fornece uma interface para interagir com o sistema operacional subjacente no qual o Python está sendo executado. Ela permite que você execute várias tarefas relacionadas ao sistema, como navegar pelo sistema de arquivos, manipular caminhos de arquivos, acessar variáveis de ambiente, executar comandos do sistema, criar diretórios e muito mais. É uma biblioteca fundamental para realizar operações de baixo nível relacionadas ao sistema operacional.

