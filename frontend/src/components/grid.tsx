import Container from "react-bootstrap/Container";
import { Row, Col } from "react-bootstrap";
import News from "./News";
const grid = () => {
  return (
    <Container fluid>
      <Row
        style={{ height: "500px" }}
        className="rows justify-content-md-center d-flex g-0"
      >
        <Col
          className="colums bg-info bg-opacity-10 fs-6"
          xl={6}
          md={6}
          sl={12}
        >
          <div>
            <News/>
          </div>
        </Col>
      </Row>
    </Container>
  );
};
export default grid;