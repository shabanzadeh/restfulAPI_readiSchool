import { Fragment, useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Table from "react-bootstrap/Table";


const Gitlab = () => {
  const [data, setTopProjects] = useState([]);

  const getTopProjects = async () => {
    try {
      const response = await fetch(
        `http://localhost:3000/news`
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
  console.log(data);

  return (
    <Fragment>
      <div className="text-sm-center text-md-center text-l-center text-xl-center mt-0 text-dark">
        <h5>Top five projects from Valiton Gitlab</h5>
      </div>
      <div className="mt-5 table-responsive">
        <Table striped>
          <thead>
            <tr className="bg-success bg-opacity-75">
              <th>Project name</th>
              <th>Commits</th>
              <th>Created project</th>
              <th>Created at</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item) => (
              <tr key={item.project_id}>
                <td className="bg-success bg-opacity-25">
                  {item.name_project}
                </td>
                <td>{item.commit_count}</td>
                <td>{item.created_project.slice(0, 10)}</td>
                <td>{item.created_at.slice(0, 10)}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
    </Fragment>
  );
};
export default Gitlab;