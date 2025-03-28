# 🗣 TG Voice to Text (RU) — n8n workflow с распознаванием речи через VOSK

Этот проект представляет собой n8n-воркфлоу, который позволяет распознавать голосовые сообщения на русском языке, отправленные пользователем в Telegram-бота.  
В основе используется **офлайн-движок VOSK**, не требующий облачных сервисов.  
На выходе вы получаете текстовое сообщение, которое можно отправить обратно в бот или передать следующему этапу обработки (например, AI-агенту).

---

## ⚙️ Переменные и настройки из `wf_tgvoicetotxt_prefs.json`

Перед запуском необходимо настроить следующий конфигурационный файл:

```json
{
  "telegram_valid_id": [111111111, 222222222],
  "tg_bot_token": "<токен вашего бота Telegram>",
  "model_path": "<путь к скачанной модели VOSK>",
  "ffmpeg_path": "ffmpeg",
  "tmp_folder": "<путь к временной папке>",
  "no_acc_msg": "Доступ к боту запрещен. Обратитесь к администратору.",
  "bot_help_msg": "Бот распознает русскую речь в текст. Отправьте боту аудио с вашей речью.",
  "waiting_msg": "Секундочку..."
}
```

- 🔐 **`telegram_valid_id`** — список ID Telegram-пользователей, которым разрешён доступ к боту.  
  Если оставить список пустым (`[]`), бот смогут использовать **все пользователи**.

- 🌐 **`model_path`** — путь к распакованной модели VOSK.  
  Для распознавания других языков скачайте нужную модель на [официальном сайте VOSK](https://alphacephei.com/vosk/models) и укажите путь к ней.  
  **Рекомендуется использовать малые модели (`small`) для ускорения работы потока.**

---

## 📦 Необходимые предварительные установки

1. **Настройка Telegram Credentials в n8n**  
   Добавьте учётные данные Telegram Bot API в разделе **Credentials** n8n (введите токен от вашего бота).

2. **Установка `ffmpeg`**  
   Убедитесь, что утилита `ffmpeg` установлена в системе:
   - либо добавлена в системную переменную `PATH`
   - либо укажите **полный путь** в переменной `ffmpeg_path` в `wf_tgvoicetotxt_prefs.json`  
     Если `ffmpeg` доступен глобально, достаточно указать `"ffmpeg"`.

3. **[n8n](https://n8n.io/)** — установлен локально или на сервере

4. **[Python 3.7+](https://www.python.org/)**

5. **Установка VOSK для Python:**

   ```bash
   pip install vosk
   ```
6. **Скачанная модель VOSK (русская или другая)**  
   Скачать можно с [официального сайта VOSK](https://alphacephei.com/vosk/models)  
   Укажите путь к разархивированной модели в переменной `model_path` файла `wf_tgvoicetotxt_prefs.json`.  
   **Рекомендуется использовать малые модели** (например, `vosk-model-small-ru-0.22`) для ускорения работы потока.

---

## ▶️ Как использовать

1. Импортируйте файл `TG_Voice_to_Txt_RU.json` в n8n.
2. Отредактируйте файл `wf_tgvoicetotxt_prefs.json` под свою среду.
3. Убедитесь, что переменная окружения `WF_TGVOICETOTXT_PATH` указывает на путь, где лежит скрипт `voicetotxt.py`.
4. Запустите воркфлоу и отправьте голосовое сообщение своему боту в Telegram.   
