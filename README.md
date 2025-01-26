Chatbot de Atendimento com GPT-3.5 Turbo
Este projeto é um chatbot de atendimento desenvolvido em Python, utilizando a API da OpenAI (GPT-3.5 Turbo). Ele foi criado para automatizar respostas a perguntas frequentes, fornecer suporte ao cliente e melhorar a eficiência do atendimento em empresas.

O chatbot é capaz de:

Responder a perguntas de forma contextual, mantendo um histórico das últimas interações.

Ser integrado a diversos canais de comunicação, como WhatsApp, Telegram ou sites.

Ser facilmente personalizado para atender às necessidades específicas da sua empresa.

Funcionalidades
Respostas Contextuais:

O chatbot usa o histórico das últimas interações para gerar respostas mais precisas e relevantes.

Comandos Especiais:

Inclui comandos como /ajuda para orientar os usuários sobre como interagir com o bot.

Integração com APIs:

Pode ser integrado a APIs de serviços como WhatsApp, Telegram ou sistemas internos da empresa.

Personalização:

Fácil adaptação para incluir perguntas e respostas específicas da empresa.

Controle de Cota:

Inclui um intervalo de 1 segundo entre as requisições para evitar exceder os limites de cota da API da OpenAI.

Tecnologias Usadas
Python: Linguagem de programação principal.

OpenAI API: Utilizada para acessar o modelo GPT-3.5 Turbo e gerar respostas inteligentes.

Git/GitHub: Para versionamento e compartilhamento do código.

Google Colab: Ambiente de desenvolvimento e teste (opcional).

Flask (opcional): Para criar uma interface web ou API RESTful.

Twilio (opcional): Para integração com WhatsApp ou SMS.

Telegram API (opcional): Para integração com o Telegram.

Como Funciona
Interação com o Usuário:

O usuário faz uma pergunta ou comando.

O chatbot processa a pergunta usando o modelo GPT-3.5 Turbo e gera uma resposta.

Histórico de Conversas:

O chatbot mantém um histórico das últimas 5 interações para gerar respostas contextuais.

Comandos Especiais:

Comandos como /ajuda e /sair permitem que o usuário obtenha ajuda ou encerre a conversa.

Integração com Canais de Comunicação:

O chatbot pode ser integrado a WhatsApp, Telegram, sites ou outros sistemas via APIs.

Como Usar
Pré-requisitos
Python 3.7 ou superior.

Uma chave de API da OpenAI.

Integração com Outros Sistemas
WhatsApp: Use a API do Twilio para enviar e receber mensagens.

Telegram: Use a API do Telegram para criar um bot.

Site: Use Flask ou Django para criar uma interface web.

Exemplo de Uso:
![image](https://github.com/user-attachments/assets/51b8e063-14fd-48ce-92a9-f0626aceeb70)



