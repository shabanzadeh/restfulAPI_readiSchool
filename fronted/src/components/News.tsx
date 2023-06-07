import { Fragment, useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';



const News = () => {
  const [data, setTopProjects] = useState([]);

  const getTopProjects = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/news`
      );
      const jsonData = await response.json();
      console.log(jsonData)
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
  

};
export default News;