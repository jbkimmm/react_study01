import React, {useEffect, useState} from 'react';
import {Form, Select} from "antd";
import API from '../../api';


const SubjectSelect = ({ professor, subject, setSubject }) => {
  const [subjectList, setSubjectList] = useState([]);

  useEffect(() => {
    const fetch = async() => {
      if ( professor ) {
        // TODO: QueryString 인자로 year, season, cert_type 인자 처리하기
        const url = `/professors/${professor.pk}/courses/`;
        const {data} = await API.get(url);
        if ( data.length === 0 ) {
          setSubjectList([]);
          setSubject(null);
        }
        else {
          setSubjectList(data);
        }
      }
    };
    fetch();
  }, [setSubject, professor]);

  const onChange = (subject_pk) => {
    setSubject(subjectList.find(s => s.pk === subject_pk));
  };

  return (
    <Form.Item label="교과목명">
      <Select onChange={subject_pk => onChange(subject_pk)}
              style={{ width: 120 }}>
        {subjectList.map(subject =>
          <Select.Option value={subject.pk} key={subject.pk}>
            {subject.display_name}
          </Select.Option>)}
      </Select>
    </Form.Item>
  );
};


export default SubjectSelect;
