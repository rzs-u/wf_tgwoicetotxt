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

# Description in English

# 🗣 TG Voice to Text (RU) — n8n workflow with speech recognition via VOSK

This project is an **n8n workflow** that allows you to recognize Russian voice messages sent to a Telegram bot.  
It uses the **offline VOSK engine**, which does not require cloud services.  
The output is the recognized text, which can be sent back to the bot or passed to the next processing stage (e.g., an AI agent).

---

## ⚙️ Variables and settings from `wf_tgvoicetotxt_prefs.json`

Before running the workflow, configure the following JSON file:

```json
{
  "telegram_valid_id": [111111111, 222222222],
  "tg_bot_token": "<your Telegram bot token>",
  "model_path": "<path to downloaded VOSK model>",
  "ffmpeg_path": "ffmpeg",
  "tmp_folder": "<path to temporary folder>",
  "no_acc_msg": "Access to the bot is denied. Contact the administrator.",
  "bot_help_msg": "The bot recognizes Russian speech and converts it to text. Send an audio message to the bot.",
  "waiting_msg": "Just a second..."
}
```

- 🔐 **`telegram_valid_id`** — list of Telegram user IDs who are allowed to use the bot.  
  If the list is left empty (`[]`), **all users** will be able to use the bot.

- 🌐 **`model_path`** — path to the unpacked VOSK model folder.  
  To use other languages, download the appropriate model from the [official VOSK website](https://alphacephei.com/vosk/models) and specify its path.  
  **It's recommended to use small models (e.g., `vosk-model-small-ru`) for better performance.**
  
---

## 📦 Prerequisites

1. **Set up Telegram Credentials in n8n**  
   Add Telegram Bot API credentials in the **Credentials** section of n8n (insert your bot token).

2. **Install `ffmpeg`**  
   Make sure the `ffmpeg` utility is installed:
   - Either added to the system `PATH`, or  
   - Provide the full path in the `ffmpeg_path` field in `wf_tgvoicetotxt_prefs.json`  
     If `ffmpeg` is available globally, you can simply write `"ffmpeg"`.

3. **[n8n](https://n8n.io/)** — installed locally or on your server

4. **[Python 3.7+](https://www.python.org/)**

5. **Install VOSK for Python:**

```bash
pip install vosk
```

6. **Downloaded VOSK model (Russian or another language)**  
   You can download it from the [official VOSK models page](https://alphacephei.com/vosk/models).  
   Specify the path to the unpacked model folder in the `model_path` variable inside `wf_tgvoicetotxt_prefs.json`.  
   **Using small models is recommended to speed up the workflow.**

---

## ▶️ How to use

1. Import the file `TG_Voice_to_Txt_RU.json` into your n8n instance.
2. Edit `wf_tgvoicetotxt_prefs.json` with the correct paths and values for your setup.
3. Ensure the environment variable `WF_TGVOICETOTXT_PATH` points to the folder where `voicetotxt.py` is located.
4. Start the workflow and send a voice message to your Telegram bot.
