# 🧠 Diminas Bot — персональный Telegram-ассистент и развлекатель

**Diminas Bot** — это многофункциональный Telegram-бот, разработанный как персональный помощник и развлекательный инструмент. Основан на Python с использованием библиотеки `pyTelegramBotAPI`. Бот умеет показывать мемы, рассказывать анекдоты, информировать о погоде, общаться, пересылать "цитаты Джейсона Стетхема" (юмористические), а также интегрироваться с другими платформами, такими как ВКонтакте.

Проект распространяется под лицензией **GNU Affero General Public License v3.0** — свободен для использования, модификации и распространения при соблюдении условий лицензии.

---

## ⚙️ Возможности бота

- 👋 `/start` — приветственное сообщение и меню
- 🌤 `/weather` — прогноз погоды по городу
- 🕐 `/time` — текущее московское время
- 😂 `/joke` — случайный анекдот (без повторений)
- 📸 `/meme` — случайный мем из папки `meme/`
- ☑ `/photo` — приём пользовательских мемов на модерацию
- 🧠 `/jasons_wisdom` — шуточные цитаты Джейсона Стетхема (из-под его постов в одной соцсети)
- 📝 `/zakaz` — оформление заявки на создание персонального Telegram-бота
- 🔤 `/en_to_ru` — автоматическая перекладка с английской раскладки на русскую
- 🔐 `/key` — генерация ключа для связи с VK-ботом
- 🤖 Ответы на произвольные фразы: «привет», «мем», «анекдот», «спасибо», «как дела», «загрузить» и др.

---

## 📁 Структура проекта

```angular2html
.
├── .gitignore
├── LICENSE
├── README.md
├── main.py # Основной скрипт запуска Telegram-бота
├── VkBot.py # Подключение и работа с VK API
├── Textes.py # Хранилище анекдотов, цитат и других текстов
├── Zakazi.txt # История заказов от пользователей
├── .env # Переменные окружения (секреты)
├── meme/ # Папка с мемами для команды /meme
├── not moderated/ # Загруженные пользователями мемы
└── picture.jpg # Изображение-пример
```

> ⚠️ Картинки в папках `meme/` и `not moderated/` приведены в качестве примеров, чтобы показать структуру. В продакшене рекомендуется заменить их на актуальные изображения или автоматизировать сбор мемов.

---

## 🚀 Установка и запуск

1. **Клонируйте репозиторий**:
```bash
git clone https://github.com/your-username/Diminas-Bot.git
 ```
   
2. **Создайте виртуальное окружение и установите зависимости:**
```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
```
```bash
pip install -r requirements.txt
```

3. **Создайте файл .env и добавьте в него свои ключи**:

```ini
TELEGRAM_TOKEN=ваш_телеграм_токен
WEATHER_TOKEN=ваш_токен_от_openweather
```

4. **Запустите бота**:

```bash
python main.py
```

Используется библиотека **pyTelegramBotAPI**, убедитесь, что у вас установлена последняя версия библиотеки и Python 3.8+

---

## 🔮 Планы по развитию
- Ежедневная рассылка случайных цитат Джейсона Стетхема по подписке
- Личный дневник через бота
- Админ-панель для управления загрузками и заказами
- Расширение набора цитат и анекдотов

---

## 📜 Лицензия

Проект распространяется по лицензии  [GNU AFFERO GENERAL PUBLIC LICENSE Version 3](LICENSE).

**Это значит, что вы можете свободно использовать, изменять и распространять проект, при условии раскрытия исходного кода и соблюдения условий лицензии при размещении сервиса в сети.**

---

Разработано с ❤️ на Python, чтобы сделать вашу (в основном мою) жизнь веселее.