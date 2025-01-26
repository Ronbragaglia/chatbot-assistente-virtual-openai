# -*- coding: utf-8 -*-
"""Chatbot_Inteligente_OpenAI

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AF_xoZ4FVCXrmEj-yIk3l3k5lr_ghtwl
"""

!pip install --upgrade openai

from openai import OpenAI
import time

client = OpenAI(api_key='')

def perguntar_gpt3(prompt, historico):
    """
    Envia uma pergunta para o GPT-3.5 Turbo e retorna a resposta.
    """
    historico.append(f"Usuário: {prompt}")
    contexto = "\n".join(historico[-5:])
    resposta = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=contexto,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    historico.append(f"Chatbot: {resposta.choices[0].text.strip()}")
    time.sleep(1)
    return resposta.choices[0].text.strip()


def chat_gpt3():
    """
    Função principal do chatbot. Interage com o usuário em um loop contínuo.
    """
    historico = []
    print("Olá! Sou um chatbot de atendimento. Como posso ajudar você?")
    while True:

        user_input = input("Você: ")


        if user_input.lower() in ["sair", "tchau", "adeus"]:
            print("Chatbot: Até logo! Espero ter ajudado.")
            break


        if user_input.lower() == "/ajuda":
            print("Chatbot: Digite sua pergunta, ou '/sair' para encerrar.")
            continue


        resposta = perguntar_gpt3(user_input, historico)


        print("Chatbot:", resposta)


if __name__ == "__main__":
    chat_gpt3()