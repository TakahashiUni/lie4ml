from pydantic import BaseModel

class Article(BaseModel):
    title: str
    content: str | None = None

class ArticleCreate(Article):
    pass

class ArticleCreateResponse(ArticleCreate):
    id: int
    
    class Config:
        orm_mode = True    
