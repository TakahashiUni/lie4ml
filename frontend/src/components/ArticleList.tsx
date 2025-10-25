import { useEffect, useState } from "react";
import { getArticles } from "../api/articleAPI";

type Article = {
  title: string;
  content: string;
};

export default function ArticleList() {
  const [articles, setArticles] = useState<Article[]>([]);

  useEffect(() => {
    const fetchArticles = async () => {
      const data = await getArticles();
      console.log("API response:", data); // ← 念のため確認
      setArticles(data);
    };
    fetchArticles();
  }, []);

  if (articles.length === 0) return <p>記事がありません。</p>;

  return (
    <div>
      {articles.map((article, index) => (
        <div key={index}>
          <h2>{article.title}</h2>
          <p>{article.content}</p>
        </div>
      ))}
    </div>
  );
}

