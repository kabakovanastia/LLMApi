# Пайплайн анализа тональности через LLM API

Скрипт на Python, который автоматически классифицирует тексты отзывов на **Positive / Negative / Neutral** с помощью API LLM и сохраняет результат в JSON.

---

## 📋 Описание задачи

Скрипт выполняет полный ETL-пайплайн:

1. Читает исходные данные из CSV-файла (датасет отзывов).
2. Для каждого отзыва отправляет запрос в LLM через API.
3. Получает от модели структурированный ответ в JSON с одной меткой тональности.
4. Сохраняет итоговый массив в файл `sentiment_analysis_result.json` — вместе с оригинальным текстом и эталонной меткой для сравнения.

**Используемый датасет**: [CRSD (Customer Review Sentiment Dataset)](https://github.com/Infinitode/CRSD)  
**LLM-провайдер**: [Groq](https://groq.com)
**Модель**: `llama-3.3-70b-versatile`

---

## 🚀 Инструкция по запуску

### 1. Клонирование репозитория
```bash
git clone https://github.com/kabakovanastia/LLMApi.git
cd LLMApi
```

### 2. Установка зависимостей
Требуется **Python 3.8+**. Установите библиотеки:
```bash
pip install -r requirements.txt
```

### 3. Получение API-ключа Groq
- Зарегистрируйтесь на [console.groq.com](https://console.groq.com).
- Создайте новый API-ключ.
- Ключ будет выглядеть как `gsk_...`.

### 4. Настройка переменных окружения
Создайте в корне проекта файл `.env` и запишите в него ключ:
```ini
API_KEY=gsk_ваш_ключ
```

### 5. Подготовка данных
Поместите файл `data.csv` из датасета [CRSD](https://github.com/Infinitode/CRSD) в папку со скриптом.  
Для быстрой проверки можно взять первые 50–100 строк.

### 6. Запуск
```bash
python main.py
```
После завершения работы в папке появится файл `sentiment_analysis_result.json` с результатами.

---

## 📥 Пример входных данных (data.csv)

| review | sentiment | model |
|--------|-----------|-------|
| Absolutely fantastic product! Exceeded all my expectations. | positive | GPT-4o-Mini |
| It's okay, nothing extraordinary but does the job. | neutral | GPT-4o-Mini |
| Terrible experience. Would not recommend to anyone. | negative | GPT-4o-Mini |
| The packaging was damaged but the product works fine. | neutral | Llama-3.1-8B |
| I love this so much, best purchase ever! | positive | Llama-3.1-8B |

## 📤 Пример выходных данных (results.json)

```json
[
    {
        "review": "Absolutely fantastic product! Exceeded all my expectations.",
        "true_sentiment": "positive",
        "predicted_sentiment": "Positive"
    },
    {
        "review": "It's okay, nothing extraordinary but does the job.",
        "true_sentiment": "neutral",
        "predicted_sentiment": "Neutral"
    },
    {
        "review": "Terrible experience. Would not recommend to anyone.",
        "true_sentiment": "negative",
        "predicted_sentiment": "Negative"
    }
]
```
