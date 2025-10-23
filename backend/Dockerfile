FROM python:3.11-slim

# 環境変数
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 依存関係を先にコピーしてキャッシュ利用
COPY pyproject.toml poetry.lock* /app/

# Install pip and poetry
RUN apt-get update && apt-get install -y curl build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - --version 1.6.1 \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry \
    && poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev

# アプリコードをコピー
COPY . /app

# 作業ディレクトリを API ディレクトリが参照できるように /app にしておく
WORKDIR /app

EXPOSE 8000

# 開発用（--reload）: Docker Compose で使うときは再読み込みが便利
CMD ["uvicorn", "api.v1.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
