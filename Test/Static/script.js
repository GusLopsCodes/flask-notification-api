document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    // Solicita permissão para mostrar notificações
    if (Notification.permission === "default") {
        Notification.requestPermission().then(permission => {
            if (permission === "granted") {
                console.log("Notification permission granted.");
            } else {
                console.log("Notification permission denied.");
            }
        });
    }

    // Subscribe
    document.getElementById('subscribe').addEventListener('click', async () => {
        const userId = document.getElementById('user_id').value;
        const response = await fetch('/subscribe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId })
        });
        const data = await response.json();
        document.getElementById('result').textContent = JSON.stringify(data);
    });

    // Unsubscribe
    document.getElementById('unsubscribe').addEventListener('click', async () => {
        const userId = document.getElementById('user_id').value;
        const response = await fetch('/unsubscribe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId })
        });
        const data = await response.json();
        document.getElementById('result').textContent = JSON.stringify(data);
    });

    // Send Notification
    document.getElementById('send_notification').addEventListener('click', async () => {
        const message = document.getElementById('message').value;
        const response = await fetch('/send_notification', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        document.getElementById('result').textContent = JSON.stringify(data);
    });

    // Handle notifications
    socket.on('notification', (data) => {
        const notifications = document.getElementById('notifications');
        const message = document.createElement('div');
        message.textContent = data.data;
        notifications.appendChild(message);

        // Exibe a notificação pop-up
        if (Notification.permission === "granted") {
            new Notification('New Notification', {
                body: data.data,
                icon: 'https://example.com/icon.png' // Adicione um ícone se desejar
            });
        }
    });

    // Button to test notification pop-up
    document.getElementById('test_notification').addEventListener('click', () => {
        const message = "Test notification from button click!";
        if (Notification.permission === "granted") {
            new Notification('Test Notification', {
                body: message,
                icon: 'https://example.com/icon.png' // Adicione um ícone se desejar
            });
        } else {
            alert('Notification permission not granted.');
        }
    });
});