import { useEffect, useState } from "react";
import { Card, Col, Form, Row } from "react-bootstrap";

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
    <Row className="container-fluid mt-5" xl={6} md={4} sl={12}>
    {articles.map((article) => (
      <Col key={article} xl={4} md={4} sl={12}>
        <div>
          <div className="text-center">
            <img src={article.urlToImage} alt="Article"  style={{ width: "400px", height: "auto" }}/>
          </div>
          <h3 className="text-center">
            <a href={article.url}>{article.title}</a>
          </h3>
          <p className="text-center text-dark">{article.description}</p>
        </div>
      </Col>
    ))}
  </Row>
    
  );
};

export default NewsList;
