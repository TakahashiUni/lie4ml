from fastapi import APIRouter
from ..schemas.articles import Article

router = APIRouter(prefix="/articles", tags=["Articles"])

# レスポンスにスキーマを適用
@router.get("/", response_model=list[Article])
def get_articles():
    sample_articles = [
        {"id": 1, "title": "What is a Lie Group?", "content": "Introduction to Lie groups..."},
        {"id": 2, "title": "Lie Algebra Basics", "content": "Lie algebras are..."}
    ]
    return sample_articles
