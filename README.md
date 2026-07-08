🎲 Desafio do Número Oculto (Number Guessing Game)

Uma experiência clássica de lógica e dedução, desenvolvida inteiramente em Python.

O Desafio do Número Oculto é um jogo interativo via terminal onde o computador escolhe aleatoriamente um número secreto dentro de um intervalo específico, e sua missão é adivinhá-lo usando o menor número de tentativas possível. A cada palpite, o sistema fornece dicas valiosas para guiar sua próxima jogada.

É um projeto excelente para demonstrar o uso de estruturas de controle, loops e manipulação de bibliotecas nativas em Python.
⚙️ Como Funciona

A mecânica do jogo é simples, direta e viciante:

    Geração do Número: O jogo utiliza a biblioteca random do Python para sortear um número secreto (por exemplo, entre 1 e 100).

    Entrada do Jogador: O usuário digita o seu palpite no terminal.

    Feedback Imediato: O programa analisa o palpite e retorna uma das seguintes respostas:

        📈 "Muito alto! Tente um número menor."

        📉 "Muito baixo! Tente um número maior."

        🎉 "Parabéns! Você acertou o número em [X] tentativas!"

    Fim de Jogo: O ciclo se repete até que o jogador acerte o número ou o limite de tentativas (dependendo da dificuldade) seja atingido.

✨ Principais Funcionalidades

    Dificuldade Ajustável: Diferentes níveis (Fácil, Médio, Difícil) que alteram o intervalo de números e a quantidade máxima de tentativas permitidas.

    Sistema de Pontuação (Opcional): Um contador que rastreia quantas tentativas foram necessárias, incentivando o jogador a quebrar seu próprio recorde.

    Interface Limpa no Terminal: Mensagens formatadas e amigáveis para garantir uma boa experiência de usuário no console.

🛠️ Tecnologias e Conceitos Utilizados

Este projeto foi construído utilizando conceitos fundamentais da linguagem Python:

    Módulos nativos: import random

    Laços de repetição: while loops para manter o jogo rodando até a condição de vitória ou derrota.

    Estruturas condicionais: if, elif e else para avaliar o palpite em relação ao número secreto.
