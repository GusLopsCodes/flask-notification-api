from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
import logging
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app, cors_allowed_origins="*")

# Configuração de logs
logging.basicConfig(level=logging.INFO)

# Armazenar inscritos e autenticação básica
subscribers = {}
users = {
    'admin': generate_password_hash('admin_password')  # Exemplo de usuário para autenticação
}

def authenticate(username, password):
    if username in users:
        return check_password_hash(users[username], password)
    return False

@app.route('/')
def index():
    return app.send_static_file('index.html')  # Serve o arquivo HTML da pasta static

@socketio.on('connect')
def handle_connect():
    logging.info('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    logging.info('Client disconnected')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    user_id = data.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    if user_id not in subscribers:
        subscribers[user_id] = None
        logging.info(f'User {user_id} subscribed')
    
    return jsonify({'status': 'Subscribed', 'user_id': user_id}), 200

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.json
    user_id = data.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    if user_id in subscribers:
        del subscribers[user_id]
        logging.info(f'User {user_id} unsubscribed')
    
    return jsonify({'status': 'Unsubscribed', 'user_id': user_id}), 200

@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({'error': 'Message is required'}), 400
    
    if not subscribers:
        return jsonify({'status': 'No subscribers'}), 200
    
    for user_id in subscribers:
        try:
            socketio.emit('notification', {'data': message}, room=user_id)
        except Exception as e:
            logging.error(f"Failed to send notification to {user_id}: {e}")
    
    logging.info(f"Notification sent to all subscribers: {message}")
    return jsonify({'status': 'Notification sent', 'message': message}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not authenticate(username, password):
        return jsonify({'error': 'Invalid credentials'}), 401
    
    return jsonify({'status': 'Logged in'}), 200

if __name__ == '__main__':
    socketio.run(app, debug=True)
