import React, {useState} from "react";
import {Icon, Menu, Layout} from "antd";
import "./App.css";
import logo from "./assets/logo_w.png";
import Planner from "./components/planner";

const {Footer, Sider} = Layout;
const {SubMenu} = Menu;


const App = () => {
  const [state, setState] = useState({collapsed: false});

  const onCollapse = (e) => {
    const { collapsed } = state;
    setState({...state, collapsed: !collapsed});
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Sider collapsible collapsed={state.collapsed} onCollapse={onCollapse}>
        <div>
          <img src={logo} style={{ padding: '10px' }} alt="logo" />
        </div>
        <Menu theme="dark" defaultSelectedKeys={['menu-planner']} mode="inline">
          <Menu.Item key="menu-planner">
            <Icon type="table" />
            <span>교수 계획표</span>
          </Menu.Item>
          <Menu.Item key="menu-2">
            <Icon type="desktop" />
            <span>Option 2</span>
          </Menu.Item>
          <SubMenu
            key="submenu-1"
            title={
              <span>
                  <Icon type="user" />
                  <span>User</span>
                </span>
            }
          >
            <Menu.Item key="menu-3">Tom</Menu.Item>
            <Menu.Item key="menu-4">Bill</Menu.Item>
            <Menu.Item key="menu-5">Alex</Menu.Item>
          </SubMenu>
        </Menu>
      </Sider>
      <Layout>
        <Planner />
        {/*<Header style={{ background: '#fff', padding: 0 }} />*/}
        {/*<Content style={{ margin: '0 16px' }}>*/}
        {/*  <Breadcrumb style={{ margin: '16px 0' }}>*/}
        {/*    <Breadcrumb.Item>User</Breadcrumb.Item>*/}
        {/*    <Breadcrumb.Item>Bill</Breadcrumb.Item>*/}
        {/*  </Breadcrumb>*/}
        {/*  <div style={{ padding: 24, background: '#fff', minHeight: 360 }}>*/}
        {/*    Bill is a cat.*/}
        {/*  </div>*/}
        {/*</Content>*/}
        <Footer style={{ textAlign: 'center' }}>
          부산대학교 ©2019. All rights reserved.
        </Footer>
      </Layout>
    </Layout>

  );
};


export default App;
