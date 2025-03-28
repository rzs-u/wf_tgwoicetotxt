import sys, os, json
import subprocess
import wave
from vosk import Model, KaldiRecognizer


def main():
    # Считываем настройки из файла JSON и сохраняем в словарь prefs
    current_dir = os.path.dirname(os.path.abspath(__file__))
    prefs_file = os.path.join(current_dir, 'wf_tgvoicetotxt_prefs.json')
    
    with open(prefs_file, "r", encoding="utf-8") as f:
        prefs = json.load(f)
    if len(sys.argv) < 2:
        print("Usage: python voicetotxt.py <TelegramChatID>")
        sys.exit(1)

    tgchatid = sys.argv[1]
    input_oga = prefs["tmp_folder"] + "voice_" + tgchatid + ".oga"
    output_wav = prefs["tmp_folder"] + "voice_" + tgchatid + ".wav"  # Временный WAV
    output_txt = prefs["tmp_folder"] + "voice_" + tgchatid + ".txt"  # Результат распознавания

    MODEL_PATH = prefs["model_path"]
    # 1. Конвертация OGA -> WAV (16000 Hz, моно)
    # -y: не спрашивать подтверждения при перезаписи
    # -ar 16000: задаем частоту дискретизации 16 kHz
    # -ac 1: один канал (моно)
    # ffmpeg_command = [
    #     "F:/program/ffmpeg/bin/ffmpeg.exe",         # "ffmpeg",
    #     "-y",
    #     "-i", input_oga,
    #     "-ar", "16000",
    #     "-ac", "1",
    #     output_wav
    # ]
    #
    # try:
    #     subprocess.run(ffmpeg_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # except subprocess.CalledProcessError:
    #     print("Ошибка конвертации OGA в WAV. Убедитесь, что ffmpeg установлен и доступен.")
    #     sys.exit(1)

    # 2. Инициализация модели Vosk
    if not os.path.exists(MODEL_PATH):
        print(f"Vosk model not found at {MODEL_PATH}. Correct <model_path> in wf_tgvoicetotxt_prefs.json settings file.")
        sys.exit(1)

    model = Model(MODEL_PATH)

    # 3. Распознавание речи
    try:
        wf = wave.open(output_wav, "rb")
    except FileNotFoundError:
        print(f"File {output_wav} not found after conversion.")
        sys.exit(1)

    if wf.getnchannels() != 1 or wf.getframerate() != 16000:
        print("The WAV file is in the wrong format. It needs 1 channel (mono) and 16000 Hz.")
        wf.close()
        sys.exit(1)

    rec = KaldiRecognizer(model, wf.getframerate())

    text_result = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # частичное распознавание
            pass
    wf.close()

    # Итоговый результат
    final_result = rec.FinalResult()
    text_result.append(final_result)

    # 4. Запись результата в файл
    # final_result обычно содержит JSON-строку, нужно вытащить из неё ключ "text"

    try:
        result_dict = json.loads(final_result)
        recognized_text = result_dict.get("text", "")
    except json.JSONDecodeError:
        recognized_text = ""

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(recognized_text.strip() + "\n")

    # Удаляем временный файл, если не нужен
    if os.path.exists(output_wav):
        os.remove(output_wav)

    # Удаляем временный файл, если не нужен
    if os.path.exists(input_oga):
        os.remove(input_oga)

    print(f"The recognition result is saved in {output_txt}")


if __name__ == "__main__":
    main()
