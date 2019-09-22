import React from "react";
import {Alert, Breadcrumb, Button, Table, Col, Form, Layout, PageHeader, Row, Select, Tabs} from "antd";


const columns = [
  { title: '구분', dataIndex: 'professor_type' },
  { title: '교수번호', dataIndex: 'number' },
  { title: '교수명', dataIndex: 'name' },
  { title: '소속학과명', dataIndex: 'department_name' },
  { title: '교내번호', dataIndex: 'school_number' },
  { title: '이메일', dataIndex: 'email' }
];


const ClassProfessorTable = ({ professorList }) => {
  return (
    <>
      교과목 담당 교수 / 책임교수 정보 조회
      <Table dataSource={professorList}
             columns={columns}
             pagination={false} />
    </>
  );
};


export default ClassProfessorTable;
