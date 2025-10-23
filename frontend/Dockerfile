FROM node:20-slim

# 作業ディレクトリ
WORKDIR /app

# package.json と lockファイルをコピー
COPY package*.json ./

# 依存パッケージをインストール
RUN npm install

# ソースコードをコピー
COPY . .

# Vite を起動 (開発用)
CMD ["npm", "run", "dev", "--", "--host"]
