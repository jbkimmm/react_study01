import React from 'react';
import {Checkbox, Table} from "antd";
import TextArea from "antd/es/input/TextArea";

const subjectColumns = [
  { title: '개설학년', dataIndex: 'grade' },
  { title: '교과구분', dataIndex: 'subject_type' },
  { title: '교과목코드', dataIndex: 'subject_code' },
  { title: '교과목명', dataIndex: 'subject_name' },
  { title: '요일', dataIndex: 'subject_day' },
  { title: '강의시간', dataIndex: 'full_time' },
  { title: '건물명', dataIndex: 'building' },
  { title: '강의실명', dataIndex: 'class_name' },
  { title: '개설학과명', dataIndex: 'make_department' },
  { title: '학점', dataIndex: 'subject_point' }
];

const checkboxRenderer = (value) =>
  <Checkbox defaultChecked={value === 'Y'} />;

const targetColumns = [
  { title: '번호', dataIndex: 'pk', render(pk, record, index) { return index+1; } },
  { title: '교과목 목표내역', dataIndex: 'target_name' },
  { title: '핵심 역량', dataIndex: 'core_point' },

  { title: '강의', dataIndex: 'e_course', render: checkboxRenderer},
  { title: '토론', dataIndex: 'e_discussion', render: checkboxRenderer},
  { title: '실험', dataIndex: 'e_experiment', render: checkboxRenderer},
  { title: '온라인', dataIndex: 'e_online', render: checkboxRenderer},
  { title: '발표', dataIndex: 'e_presentation', render: checkboxRenderer},
  { title: '예/체능', dataIndex: 'e_art', render: checkboxRenderer},
  { title: '세미나', dataIndex: 'e_seminar', render: checkboxRenderer},
  { title: '연구', dataIndex: 'e_study', render: checkboxRenderer},
  { title: '설계', dataIndex: 'e_design', render: checkboxRenderer},
  { title: '기타', dataIndex: 'e_other', render: checkboxRenderer},

  { title: '출석', dataIndex: 'w_attendance', render: (value) =>
      <Checkbox defaultChecked={value === 'Y'} disabled={true} /> },
  { title: '중간고사', dataIndex: 'w_middle_exam', render: checkboxRenderer},
  { title: '기말고사', dataIndex: 'w_final_exam', render: checkboxRenderer},
  { title: '과제물', dataIndex: 'w_project', render: checkboxRenderer},
  { title: '퀴즈', dataIndex: 'w_quiz', render: checkboxRenderer},
  { title: '발표', dataIndex: 'w_presentation', render: checkboxRenderer},
  { title: '보고서', dataIndex: 'w_report', render: checkboxRenderer},
  { title: '실기', dataIndex: 'w_practical', render: checkboxRenderer},
  { title: '기타', dataIndex: 'w_other', render: checkboxRenderer},
];

const Section1 = ({ subjectList, klassContent, targetList }) => {
  return (
    <>
      <div style={{ marginBottom: 24 }}>
        개설 교과목 정보 조회
        <Table dataSource={subjectList}
               columns={subjectColumns}
               pagination={false}
               style={{ fontSize: '0.9em'}} />
      </div>

      <div style={{ marginBottom: 24 }}>
        교과목 개요 입력 수정
        <TextArea value={klassContent} style={{ fontSize: '0.9em'}}/>
      </div>

      <div style={{ marginBottom: 24 }}>
        교과목 목표별 교육방법 및 평가방법 수정
        <Table dataSource={targetList}
               columns={targetColumns}
               pagination={false}
               style={{ fontSize: '0.9em' }}/>
      </div>
    </>
  );
};

export default Section1;
