import { Fragment, useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';



const News = ({title, description, url, urlToImage}) => {
  const [data, setTopProjects] = useState([]);

  const getTopProjects = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/news`
      );
      const jsonData = await response.json();
      setTopProjects(jsonData);
    } catch (err) {
      if (typeof err === "string") {
        console.log(err);
      } else if (err instanceof Error) {
        console.log(err.message);
      }
    }
  };
  useEffect(() => {
    getTopProjects();
  }, []);
  return(
    <div className="news-app">
      <div className="news-item" src={urlToImage} alt={urlToImage}>
        <img className="news-img">
        <h3><a href={url}>{title}</a></h3>
        <p>{description}</p>
        </img>

      </div>

    </div>
  )
};
export default News;