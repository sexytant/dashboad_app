# Python イメージをベースに使用
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 必要なライブラリをインストールするために requirements.txt をコピー
COPY requirements.txt ./

# ライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# Streamlit のポートを公開
EXPOSE 8501

# アプリケーションを起動
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
