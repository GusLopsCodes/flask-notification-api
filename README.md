# API de Notificações

## Descrição

<p align="center">
  <img src="https://images.pexels.com/photos/27451157/pexels-photo-27451157.png?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" width="475" />
</p>

A **API de Notificações** é um serviço de notificações em tempo real desenvolvido com Python, Flask e WebSocket. Este serviço permite que usuários se inscrevam, desinscrevam e recebam notificações em tempo real. O projeto também inclui uma interface HTML básica para testar e demonstrar a funcionalidade da API. Criado para aprimorar meu portfólio em Python, o projeto utiliza habilidades adquiridas durante meus estudos em Ciência da Computação.

## Funcionalidades

- **Gerenciamento de Inscrições:** Inscreva-se e desinscreva-se para receber notificações.
- **Notificações em Tempo Real:** Envio de notificações para todos os usuários inscritos usando WebSocket.
- **Interface HTML:** Interface web simples para testar a funcionalidade da API.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação para construir a API.
- **Flask:** Framework web para Python, utilizado para criar os endpoints da API e gerenciar requisições HTTP.
- **Flask-SocketIO:** Suporte a WebSocket para comunicação em tempo real.
- **HTML:** Interface web básica para interação com a API.

## Instalação

1. **Clone o Repositório:**
   ```sh
   git clone https://github.com/USERNAME/notification-api.git
   cd notification-api

**Configure um Ambiente Virtual (Opcional, mas Recomendado):**
python -m venv venv
source venv/bin/activate  # No Windows use venv\Scripts\activate

**Instale as Dependências:** pip install -r requirements.txt

## Uso
**Execute o Servidor Flask:**
python app.py

Acesse a Interface HTML:
Abra um navegador web e vá para **http://127.0.0.1:5000/** para testar a API e ver as notificações em tempo real.

## Endpoints da API
### POST /subscribe

**Descrição:** Adiciona um usuário à lista de notificações.

**Parâmetros:** user_id (string) - ID do usuário a ser inscrito.

**Resposta**

*json:*
{ "status": "Unsubscribed", "user_id": "user_id" }

### POST /send_notification

**Descrição:** Envia uma mensagem de notificação para todos os usuários inscritos.

**Parâmetros:** message (string) - A mensagem de notificação a ser enviada.

**Resposta:**

*json:*
{ "status": "Notification sent", "message": "message" }

## Planos Futuros
Este projeto foi criado para expandir meu portfólio em Python e demonstrar habilidades práticas adquiridas em meus estudos em Ciência da Computação. No futuro, pretendo desenvolver um sistema mais complexo, incluindo a criação de um site de e-commerce onde esta API de notificações será integrada. O objetivo é construir uma plataforma robusta com capacidades de notificação em tempo real e expandir suas funcionalidades.

## Contribuição
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, por favor, faça um fork do repositório, crie um branch com suas alterações e envie um pull request.
