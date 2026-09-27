import datetime
import json
import urllib.error
import urllib.request

# 1. Ваш API-ключ и адрес сервиса Groq
API_KEY = "YOUR_API_KEY_HERE"
url = "https://api.groq.com/openai/v1/chat/completions"

# 2. Пользователь вводит вопрос
user_question = input("Введите ваш вопрос: ")

# Формируем данные для отправки
data = {
    "model": "llama-3.3-70b-versatile",
    "messages": [{"role": "user", "content": user_question}],
}

# Заголовки (с ключом авторизации и User-Agent)
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
}

try:
    # 3. Отправка запроса модели
    json_data = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=json_data, headers=headers)

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))

        # 4. Получаем и выводим ответ
        answer = result["choices"][0]["message"]["content"]
        print("\n--- Ответ Groq ---")
        print(answer)

        # Дополнительно: получаем текущую дату и время
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 5. Сохраняем вопрос, ответ и время в текстовый файл
        with open("history.txt", "a", encoding="utf-8") as file:
            file.write(f"=== Время: {now} ===\n")
            file.write(f"Вопрос: {user_question}\n")
            file.write(f"Ответ:\n{answer}\n")
            file.write("=" * 30 + "\n\n")

        print("\n[Успешно]: Запись сохранена в файл history.txt!")
