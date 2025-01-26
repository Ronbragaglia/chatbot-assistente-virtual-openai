!pip install cryptography --quiet  

from getpass import getpass
import os
import time
from openai import OpenAI
from cryptography.fernet import Fernet  


API_KEY = getpass("Cole sua API Key da OpenAI (não será exibida): ")
os.environ["OPENAI_API_KEY"] = API_KEY


KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)
encrypted_key = cipher_suite.encrypt(API_KEY.encode())

client = OpenAI(api_key=cipher_suite.decrypt(encrypted_key).decode())


def sanitizar_input(texto: str) -> str:
    """Remove caracteres perigosos e limita tamanho"""
    return texto[:500].replace("\n", " ").strip()  

def gerar_resposta(prompt: str, historico: list) -> str:
    """Processa a pergunta com 4 camadas de segurança"""
    try:
        prompt_limpo = sanitizar_input(prompt)
        
        resposta = client.chat.completions.create(
            model="gpt-4-turbo",  
            messages=[
                {"role": "system", "content": "Você é um assistente corporativo profissional. Responda de forma concisa e técnica."},
                *historico[-3:],  
                {"role": "user", "content": prompt_limpo}
            ],
            max_tokens=200,
            temperature=0.4,
            timeout=10
        )
        return resposta.choices[0].message.content.strip()
    
    except Exception as e:
        return f"🚨 Erro: {str(e)}. Notifique o administrador."


def chat_loop_seguro():
    historico = []
    log = []
    
    print("\n" + "="*50)
    print(" CHATBOT CORPORATIVO - v3.0 ".center(50, "⚡"))
    print("="*50 + "\n")
    
    try:
        while True:
            user_input = input("Você: ").strip()
            
            
            if user_input.startswith("/"):
                if user_input.lower() == "/sair":
                    break
                elif user_input.lower() == "/ajuda":
                    print("\n📝 Comandos:\n/sair - Encerrar\n/limpar - Reiniciar\n/log - Ver registro")
                elif user_input.lower() == "/limpar":
                    historico.clear()
                    print("\n🔄 Conversa reiniciada.")
                elif user_input == "/log" and len(log) > 0:
                    print("\n".join(log[-3:]))
                continue
            
            resposta = gerar_resposta(user_input, historico)
            
           
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            historico.append({"role": "user", "content": user_input})
            historico.append({"role": "assistant", "content": resposta})
            log.append(f"[{timestamp}] User: {user_input[:50]}... | Bot: {resposta[:50]}...")
            
            print(f"\n🤖: {resposta}\n")

    finally:
        
        os.environ.pop("OPENAI_API_KEY", None)
        print("\n🔒 Sessão encerrada com purge de credenciais.")


if __name__ == "__main__":
    chat_loop_seguro()
