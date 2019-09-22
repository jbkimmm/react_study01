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
       <h1>React study</h1> 
      </Content>
    </>
  );
};

export default Home;
