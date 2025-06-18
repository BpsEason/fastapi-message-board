from fastapi.testclient import TestClient
from main import app

# 初始化測試客戶端
client = TestClient(app)

# 測試創建留言
def test_create_message():
    """測試創建一則新留言"""
    response = client.post("/messages/", json={"author": "測試用戶", "content": "你好！"})
    assert response.status_code == 200
    assert response.json()["author"] == "測試用戶"
    assert response.json()["content"] == "你好！"

# 測試獲取所有留言
def test_get_messages():
    """測試獲取所有留言"""
    response = client.get("/messages/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # 確保回傳的是列表

# 測試獲取不存在的留言
def test_get_nonexistent_message():
    """測試獲取不存在的留言應回傳 404"""
    response = client.get("/messages/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "留言不存在"