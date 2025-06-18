const apiUrl = '/messages/';

async function fetchMessages() {
    const response = await fetch(apiUrl);
    const messages = await response.json();
    const messageList = document.getElementById('message-list');
    messageList.innerHTML = '';
    messages.forEach(msg => {
        const card = document.createElement('div');
        card.className = 'card message-card';
        card.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">${msg.author}</h5>
                <p class="card-text">${msg.content}</p>
                <p class="card-text"><small class="text-muted">${new Date(msg.created_at).toLocaleString('zh-TW')}</small></p>
                <button class="btn btn-sm btn-warning" onclick="editMessage(${msg.id})">編輯</button>
                <button class="btn btn-sm btn-danger" onclick="deleteMessage(${msg.id})">刪除</button>
            </div>
        `;
        messageList.appendChild(card);
    });
}

async function createMessage(author, content) {
    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ author, content })
    });
    if (response.ok) fetchMessages();
}

async function editMessage(id) {
    const author = prompt('輸入新作者：');
    const content = prompt('輸入新內容：');
    if (author && content) {
        const response = await fetch(`${apiUrl}${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ author, content })
        });
        if (response.ok) fetchMessages();
    }
}

async function deleteMessage(id) {
    if (confirm('確定要刪除這則留言？')) {
        const response = await fetch(`${apiUrl}${id}`, { method: 'DELETE' });
        if (response.ok) fetchMessages();
    }
}

document.getElementById('message-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const author = document.getElementById('author').value;
    const content = document.getElementById('content').value;
    await createMessage(author, content);
    e.target.reset();
});

window.onload = fetchMessages;