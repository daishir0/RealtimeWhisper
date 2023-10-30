# RealtimeWhisper

## Overview
RealtimeWhisper is a real-time audio capturing and transcription utility. It records audio for a specified duration, transcribes the audio using OpenAI's Whisper ASR system, and uploads the transcriptions to a specified remote server via SSH. This utility is useful for generating text transcriptions of live audio feeds and ensuring they are securely stored on a remote server.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/daishir0/RealtimeWhisper/RealtimeWhisper.git
   ```
2. Navigate to the cloned repository:
   ```bash
   cd RealtimeWhisper
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Install FFmpeg on your machine. After installation, don't forget to add the executable to your path.

## Usage
1. Update the `SSH_HOST`, `SSH_USER`, `SSH_KEY_PATH`, and `REMOTE_DIR` variables in the `RealtimeWhisper.py` script with your SSH server's details.
2. Run the script:
   ```bash
   python RealtimeWhisper.py
   ```
3. The script will start recording audio. Press `Ctrl+C` to stop the recording.

## Precautions
- Ensure that your SSH server is properly configured and that the specified remote directory exists.
- Ensure that your OpenAI API credentials are correctly set in the script.
- Ensure that FFmpeg is properly installed and configured on your machine.

## License
RealtimeWhisper is licensed under the MIT License. See the `LICENSE` file for more details.

---

# RealtimeWhisper（リアルタイムウィスパー）

## 概要
RealtimeWhisperは、リアルタイムでオーディオをキャプチャし、OpenAIのWhisper ASRシステムを使用して書き起こし、SSHを介して書き起こしをリモートサーバーにアップロードするPythonスクリプトです。

## インストール方法
1. リポジトリをクローンします：
   ```bash
   git clone https://github.com/daishir0/RealtimeWhisper/RealtimeWhisper.git
   ```
2. クローンしたリポジトリに移動します：
   ```bash
   cd RealtimeWhisper
   ```
3. 必要なPythonパッケージをインストールします：
   ```bash
   pip install -r requirements.txt
   ```
4. FFmpegをマシンにインストールします。インストール後、実行ファイルへパスを通すことを忘れないでください。

## 使い方
1. `RealtimeWhisper.py`スクリプトの`SSH_HOST`、`SSH_USER`、`SSH_KEY_PATH`、および`REMOTE_DIR`変数を、SSHサーバーの詳細に更新します。
2. スクリプトを実行します：
   ```bash
   python RealtimeWhisper.py
   ```
3. スクリプトはオーディオの録音を開始します。録音を停止するには、`Ctrl+C`を押します。

## 注意点
- SSHサーバーが適切に設定されていて、指定されたリモートディレクトリが存在することを確認してください。
- スクリプト内のOpenAI API資格情報が正しく設定されていることを確認してください。
- FFmpegが適切にインストールおよび設定されていることを確認してください。

## ライセンス
RealtimeWhisperはMITライセンスの下でライセンスされています。詳細については、`LICENSE`ファイルを参照してください。
