from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result

import api.v1.models.articles as article_model
import api.v1.schemas.articles as article_schema


def create_article(
    db: Session,
    article_create: article_schema.Article,
) -> article_model.Article:
    article = article_model.Article(**article_create.dict())
    db.add(article)
    db.commit()
    db.refresh(article)
    
    return article


def get_article(
    db: Session,
    article_id: int,
) -> article_model.Article | None:
    result: Result = db.execute(
        select(
            article_model.Article
        ).filter(
            article_model.Article.id == article_id
        )
    )
    
    return result.scalars().first()


def update_article(
    db: Session,
    article_create: article_schema.ArticleCreate,
    original: article_model.Article,
) -> article_model.Article:
    original.title = article_create.title
    db.add(original)
    db.commit()
    db.refresh(original)
    
    return original


def delete_article(
    db: Session,
    original: article_model.Article,
) -> None:
    db.delete(original)
    db.commit()


def get_articles(
    db: Session,
) -> list[tuple[int, str, str]]:
    result: Result = db.execute(
        select(
            article_model.Article.id,
            article_model.Article.title,
            article_model.Article.content,
        )
    )
    
    return result.all()
