import openai
import os
import sys
import time
import sounddevice as sd
import numpy as np
from pydub import AudioSegment
import tempfile
from datetime import datetime
import paramiko
import soundfile as sf


# ============================================================
# API情報
# ============================================================

openai.organization = ""
openai.api_key      = ""
print("OpenAI API information set.")

# ============================================================
# 設定
# ============================================================

DURATION = 30  # レコーディングの時間 (秒)
SAMPLE_RATE = 44100  # サンプルレート
CHANNELS = 1  # モノラル

# ============================================================
# SSH接続情報
# ============================================================

SSH_HOST = "your_ssh_host"
SSH_PORT = 22
SSH_USER = "ssh-user"
SSH_KEY_PATH = "C:/path-to-ssh-key-file/key.pem"
REMOTE_DIR = "/path-to-save-dir-at-remote-host/dir"
print("SSH connection information set.")

# ============================================================
# ディレクトリの確認と作成
# ============================================================

if not os.path.exists("./data"):
    os.makedirs("./data")

# ============================================================
# 音声ファイルの文字起こし関数
# ============================================================

def speech_to_text(audio_data, sample_rate):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        sf.write(temp_audio_file.name, audio_data, sample_rate)
        temp_audio_file.seek(0)
        response = openai.Audio.transcribe(model="whisper-1", file=temp_audio_file)
    return response.text

# ============================================================
# SSHでリモートホストにファイルをアップロード
# ============================================================

def upload_to_ssh(local_filepath, remote_filepath):
    key = paramiko.RSAKey(filename=SSH_KEY_PATH)
    with paramiko.Transport((SSH_HOST, SSH_PORT)) as transport:
        transport.connect(username=SSH_USER, pkey=key)
        with paramiko.SFTPClient.from_transport(transport) as sftp:
            sftp.put(local_filepath, remote_filepath)
    print(f"File uploaded to {SSH_USER}@{SSH_HOST}:{remote_filepath}")

# ============================================================
# メインロジック
# ============================================================

if __name__ == "__main__":
    print("Press Ctrl+C to stop the recording...")

    try:
        while True:
            print("Recording...")
            audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='int16')
            print("Recording complete. Waiting for audio to be processed...")
            sd.wait()
            audio_data = np.int16(audio_data)
            print("Converting audio to text...")
            result = speech_to_text(audio_data, SAMPLE_RATE)

            # 現在の日時を取得し、ファイル名とパスを生成
            current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")
            local_filepath = f"./data/{current_datetime}.txt"
            remote_filepath = f"{REMOTE_DIR}/{current_datetime}.txt"
            
            # 結果をローカルファイルに保存
            with open(local_filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(result)
            print(f"Result saved to {local_filepath}")
            
            # ローカルファイルをSSHでアップロード
            upload_to_ssh(local_filepath, remote_filepath)

            print(f"Result saved to {remote_filepath}")

    except KeyboardInterrupt:
        print("\nRecording stopped.")
