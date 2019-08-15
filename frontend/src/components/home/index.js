import React from "react";
import {Layout, PageHeader} from "antd";
// import queryString from "query-string";
const {Content} = Layout;


const Home = ({history, location, match}) => {
  // const qs = queryString.parse(location.search);
  return (
    <>
      <PageHeader title={"Home"} />

      <Content>
        Home Component
      </Content>
    </>
  );
};


export default Home;
