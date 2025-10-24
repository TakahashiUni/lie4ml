from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db

import api.v1.schemas.articles as article_schema
import api.v1.cruds.articles as article_crud


router = APIRouter(prefix="/articles", tags=["Articles"])


@router.post("/", response_model=article_schema.ArticleCreateResponse)
async def create_article(
    article_body: article_schema.ArticleCreate,
    db: Session = Depends(get_db),
):
    return article_crud.create_article(db, article_body)


@router.put("/{article_id}", response_model=article_schema.ArticleCreateResponse)
async def update_article(
    article_id: int,
    article_body: article_schema.ArticleCreate,
    db: Session = Depends(get_db)
):
    article = article_crud.get_article(db, article_id=article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    
    return article_crud.update_article(db, article_body, original=article)


@router.delete("/{article_id}", response_model=None)
async def delete_article(
    article_id: int,
    db: Session = Depends(get_db)
):
    article = article_crud.get_article(db, article_id=article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    
    return article_crud.delete_article(db, original=article)


@router.get("/", response_model=list[article_schema.Article])
async def get_articles(db: Session = Depends(get_db)):
    return article_crud.get_articles(db)
