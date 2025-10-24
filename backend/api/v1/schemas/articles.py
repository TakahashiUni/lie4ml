from pydantic import BaseModel

# 記事の基本情報（レスポンス用）
class Article(BaseModel):
    id: int
    title: str
    content: str | None = None

    class Config:
        orm_mode = True
