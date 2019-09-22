import React, {useCallback, useEffect, useMemo, useReducer} from 'react';
import {Checkbox, Table} from "antd";
import TextArea from "antd/es/input/TextArea";
import produce from "immer";


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


const targetColumns = [
    { title: '강의', dataIndex: 'e_course' },
    { title: '토론', dataIndex: 'e_discussion' },
    { title: '실험', dataIndex: 'e_experiment' },
    { title: '온라인', dataIndex: 'e_online' },
    { title: '발표', dataIndex: 'e_presentation' },
    { title: '예/체능', dataIndex: 'e_art' },
    { title: '세미나', dataIndex: 'e_seminar' },
    { title: '연구', dataIndex: 'e_study' },
    { title: '설계', dataIndex: 'e_design' },
    { title: '기타', dataIndex: 'e_other' },

    { title: '출석', dataIndex: 'w_attendance', disabled: true },
    { title: '중간고사', dataIndex: 'w_middle_exam' },
    { title: '기말고사', dataIndex: 'w_final_exam' },
    { title: '과제물', dataIndex: 'w_project' },
    { title: '퀴즈', dataIndex: 'w_quiz' },
    { title: '발표', dataIndex: 'w_presentation' },
    { title: '보고서', dataIndex: 'w_report' },
    { title: '실기', dataIndex: 'w_practical' },
    { title: '기타', dataIndex: 'w_other' }
];


const reducer = (state, action) => {
  return produce(state, draft => {
    const { idx, name, checked } = action;
    draft[idx][name] = checked;
  });
};


const Section1 = ({ subjectList, klassContent, targetList }) => {
  const [state, dispatch] = useReducer(reducer, targetList);

  const onChange = useCallback((e, idx) => {
    const { name, checked } = e.target;
    dispatch({ idx, name, checked});
  }, []);

  useEffect(() => {
    const apply = async() => {
    };

    console.log("changed state ---");
    console.log(state);
  }, [state]);

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

          <table style={{ fontSize: '0.9em', borderCollapse: 'collapse', border: '1px solid #333' }}>
            <thead>
              <tr>
                <th>번호</th>
                <th>교과목 목표내역</th>
                <th>핵심 역량</th>
                {targetColumns.map(({ title }) => <th>{title}</th>)}
              </tr>
            </thead>
            <tbody>
              {state.map((row, idx) => (
                <tr>
                  <td style={{ border: '1px solid #333333'}}>{idx}</td>
                  <td style={{ border: '1px solid #333333'}}>{row.target_name}</td>
                  <td style={{ border: '1px solid #333333'}}>{row.core_point}</td>
                  {targetColumns.map(col => {
                    const {dataIndex, disabled=false} = col;
                    return (
                      <td>
                        <input type="checkbox"
                               defaultChecked={row[dataIndex] === 'Y'}
                               name={dataIndex}
                               disabled={disabled}
                               onChange={(e) => onChange(e, idx)} />
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
    </>
  );
};

export default Section1;
