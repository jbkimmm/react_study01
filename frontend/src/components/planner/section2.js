import React, {useMemo} from 'react';
import TextArea from "antd/lib/input/TextArea";
import {Row, Col, Table, InputNumber, Input, Form, Select} from "antd";

const Section2 = ({
  preContent,
  testContent,
  percent,
  book,
  coreList,
}) => {

  const percentDataSource = useMemo(() => {
    if ( percent === null ) {
      return [];
    }
    else {
      return [
        { label: '과제물', value: percent.task },
        { label: '기말고사', value: percent.final_exam },
        { label: '기타', value: percent.other },
        { label: '발표', value: percent.presentation },
        { label: '보고서', value: percent.report },
        { label: '실기', value: percent.practical },
        { label: '중간고사', value: percent.middle_exam },
        { label: '출석태도', value: percent.attendance },
        { label: '퀴즈', value: percent.quiz },
      ];
    }
  }, [percent]);

  const percentColumns = [
    { title: '평가방법', dataIndex: 'label' },
    { title: '비율(%)', dataIndex: 'value',
      render: (value, record, idx) => <InputNumber defaultValue={value} min={0} max={100} /> },
  ];

  const bookDataSource = useMemo(() => {
    if ( book === null ) {
      return [];
    }
    return [
      { label: '상담시간', value: book.consult_time },
      { label: '선수지식', value: book.pre_knowledge },
      { label: '주교재', value: book.main_note },
      { label: '부교재1', value: book.sub_note1 },
      { label: '부교재2', value: book.sub_note2 },
      { label: '부교재3', value: book.sub_note3 },
      { label: '관련웹', value: book.ref_web },
      { label: '지정도서', value: book.select_book},
    ];
  });

  const bookColumns = [
    { title: '교재', dataIndex: 'label' },
    { title: '내용', dataIndex: 'value',
      render: (value, record, idx) => <Input value={value} /> },
  ];

  const coreColumns = [
    { title: '성과기준번호', dataIndex: 'pk' },
    { title: '내용', dataIndex: 'content' },
    { title: '반영률', dataIndex: 'percent' }
  ];

  return (
    <>
      선수과목 및 지식조회
      <TextArea value={preContent} />

      학습평가방법 자율 입력 (선택사항)
      <Row gutter={24}>
        <Col span={12}>
          <Table dataSource={percentDataSource} columns={percentColumns} pagination={false} />
        </Col>
        <Col span={12}>
          <Table dataSource={bookDataSource} columns={bookColumns} pagination={false} />
        </Col>
      </Row>

      평가 관련 요구사항 입력수정 [필요시 세부 평가방안 기재 (예: 설계 PROjJECT)]
      <TextArea value={testContent} />

      핵심역량 (학습성과)
      <Table dataSource={coreList} columns={coreColumns} pagination={false} />
    </>
  );
};


export default Section2;
