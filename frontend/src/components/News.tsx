import { useEffect, useState } from "react";
import { Card, Col, Row } from "react-bootstrap";

const NewsList = () => {
  const [articles, setArticles] = useState([]);

  const newsProjects = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/news`
      );
      const jsonData = await response.json();
      setArticles(jsonData); 
    } catch (err) {
      if (typeof err === "string") {
        console.log(err);
      } else if (err instanceof Error) {
        console.log(err.message);
      }
    }
  };

  useEffect(() => {
    newsProjects();
  }, []);

  return (
    <Row className='fluid-container'>
      <Col>
      
      <div>
          {articles.map((article) => {
            return (
              <div key={article}>
                <img className="news-img" src={article.urlToImage} alt={article.urlToImage}></img>
                <h3><a href={article.url}>{article.title}</a></h3>
                <p>{article.description}</p>
              </div>
            );
          })}
        </div>
    
      </Col>
      
    </Row>
  );
};

export default NewsList;
