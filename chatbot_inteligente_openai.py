!pip install openai python-dotenv > /dev/null


from openai import OpenAI
import os
import time


API_KEY = "SUA_CHAVE_AQUI"  
os.environ["OPENAI_API_KEY"] = API_KEY

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def perguntar_gpt(prompt: str, historico: list) -> str:
    """
    Envia pergunta para o GPT-3.5 Turbo com tratamento de erros
    """
    try:
        contexto = historico[-5:] + [{"role": "user", "content": prompt}]
        
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual profissional de atendimento."},
                *contexto
            ],
            max_tokens=150,
            temperature=0.5,
            timeout=15
        )
        return resposta.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Desculpe, ocorreu um erro: {str(e)}"

def chat_loop():
    """
    Loop principal do chatbot para uso no Colab
    """
    historico = []
    print("\n🔵 Chatbot de Atendimento - Digite '/ajuda' para comandos\n")
    
    try:
        while True:
            user_input = input("Você: ")
            
            if user_input.lower() in ["/sair", "/exit"]:
                print("\n🔴 Chatbot: Atendimento encerrado. Até logo!")
                break
                
            if user_input.lower() == "/ajuda":
                print("\n🟡 Comandos disponíveis:")
                print("/sair - Encerrar atendimento")
                print("/limpar - Reiniciar conversa")
                continue
                
            if user_input.lower() == "/limpar":
                historico.clear()
                print("\n🟢 Chatbot: Conversa reiniciada. Como posso ajudar?")
                continue
            
            resposta = perguntar_gpt(user_input, historico)
            historico.extend([
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": resposta}
            ])
            
            print(f"\n🤖 Chatbot: {resposta}\n")
            time.sleep(0.3)
            
    except KeyboardInterrupt:
        print("\n🔴 Chatbot: Atendimento interrompido pelo usuário.")


if __name__ == "__main__":
    chat_loop()
