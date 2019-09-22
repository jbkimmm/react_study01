import React, {useEffect, useState} from 'react';
import {Alert, Breadcrumb, Button, Col, Form, Layout, PageHeader, Row, Select, Tabs} from "antd";
import ProfessorSelect from "./professor_select";
import KlassTable from "./klass_table";
import SubjectSelect from "./subject_select";
import ClassProfessorTable from "./class_professor_table";
import API from "../../api";
import Section1 from "./section1";
import Section2 from "./section2";

const {Content} = Layout;
const {Option} = Select;


const Planner = () => {
  const [professor, setProfessor] = useState(null);
  const [subject, setSubject] = useState(null);
  const [klassPk, setKlassPk] = useState(null);  // 상탯값으로 받기
  const [klass, setKlass] = useState(null);

  useEffect(() => {
    if ( ! klassPk ) {
      setKlass(null);
    }
    else {
      const fetch = async () => {
        const url = `/classes/${klassPk}/`;
        const {data} = await API.get(url);
        setKlass(data);
        console.log(data);
      };
      fetch();
    }
  }, [klassPk]);

  return (
    <>
      <PageHeader title="교수 계획표" subTitle="공학 교수계획표 관리" />

      <Content style={{ margin: '0 16px' }}>
        <Breadcrumb style={{ margin: '16px 0' }}>
          <Breadcrumb.Item>메뉴</Breadcrumb.Item>
          <Breadcrumb.Item>교수 계획표</Breadcrumb.Item>
        </Breadcrumb>
        <div style={{ padding: 24, background: '#fff', minHeight: 360 }}>
          <Form layout={"inline"} style={{ marginBottom: 24 }}>
            <Form.Item label="인증구분">
              <Select defaultValue={"공학교육인증"}>
                <Option value={"공학교육인증"}>공학교육인증</Option>
              </Select>
            </Form.Item>
            <Form.Item label="학년도">
              <Select defaultValue={2019}>
                <Option value={2019}>2019</Option>
              </Select>
            </Form.Item>
            <Form.Item label="학기">
              <Select defaultValue={"1학기"}>
                <Option value={"1학기"}>1학기</Option>
                <Option value={"2학기"}>2학기</Option>
              </Select>
            </Form.Item>
            <ProfessorSelect professor={professor} setProfessor={setProfessor} />
            <SubjectSelect professor={professor} subject={subject} setSubject={setSubject} />
          </Form>

          <Row gutter={24} style={{ marginBottom: 24 }}>
            <Col span={12}>
              <KlassTable subject={subject} setKlassPk={setKlassPk} />
            </Col>
            <Col span={12}>
              <ClassProfessorTable professorList={klass ? klass.professor_list : []} />
            </Col>
          </Row>

          {!klass &&
              <Alert message="분반을 선택해주세요." type="warning" />
          }

          {klass &&
              <>
                <Tabs defaultActiveKey="1" type="card">
                  <Tabs.TabPane tab="교과목 기본정보" key="1">
                    <Section1 subjectList={klass ? klass.subject_list : []}
                              klassContent={klass ? klass.content : ''}
                              targetList={klass ? klass.target_list : []}
                    />
                  </Tabs.TabPane>
                  <Tabs.TabPane tab="학습성과 / 학습평가방법 / 강의정보" key="2">
                    <Section2 preContent={klass ? klass.pre_content : ''}
                              testContent={klass ? klass.test_content : ''}
                              percent={klass ? klass.percent : null}
                              book={klass ? klass.book : null}
                              coreList={klass ? klass.core_list : []}
                    />
                  </Tabs.TabPane>
                  <Tabs.TabPane tab="주별 계획" key="3">
                    TODO: Content of Tab Pane 3
                  </Tabs.TabPane>
                  <Tabs.TabPane tab="TERM PROJECT" key="4" disabled={true}>
                    TODO: Content of Tab Pane 4
                  </Tabs.TabPane>
                </Tabs>

                <Button type="primary" onClick={() => alert("미구현")}>저장하기</Button>
              </>
          }
        </div>
      </Content>
    </>
  );
};


export default Planner;
