import React, {useEffect, useState} from 'react';
import {Form, Icon, Input, Modal, Table} from 'antd';
import { blue } from '@ant-design/colors';
import API from '../../api';


const columns = [
  { title: '선택', dataIndex: 'is_selected', render(is_selected, record, index) {
      return is_selected ? <Icon type="check-circle" /> : false;
    } },
  { title: '교수번호', dataIndex: 'number' },
  { title: '학과', dataIndex: 'department_name' },
  { title: '교수명', dataIndex: 'name' }
];


const ProfessorSelect = ({ professor, setProfessor }) => {
  const [query, setQuery] = useState('');
  const [professorList, setProfessorList] = useState([]);
  const [visibleModal, setVisibleModal] = useState(false);

  useEffect(() => {
    if ( query.length === 0 ) {
      setProfessorList([]);
    }
    else {
      const fetch = async() => {
        const params = { query };
        const {data} = await API.get("/professors/", { params });
        setProfessorList(
          data.map(professor => ({
            ...professor,
            is_selected: false
          }))
        );
      };
      fetch();
    }
  }, [query]);

  const onRow = (record, index) => {
    const { pk, is_selected } = record;
    return {
      onClick: (e) => {
        setProfessor(record);
        setProfessorList(
          professorList.map(professor => ({
            ...professor,
            is_selected: pk === professor.pk
          }))
        );
        setVisibleModal(false);
      },
      style: {
        backgroundColor: is_selected ? blue[2] : null,
        cursor: 'pointer'
      }
    };
  };

  return (
    <Form.Item label="교수">
      <Input placeholder="교수 검색 ..."
             readOnly={true}
             value={
               professor !== null
                 ? `${professor.number} ${professor.name}`
                 : null}
             onClick={() => setVisibleModal(true)} />
      <Modal title="교수 검색"
             visible={visibleModal}
             style={{ padding: 0 }}
             closable={false}
             footer={null}>
        <Input style={{ marginBottom: 12 }}
               placeholder="교수번호/교수명 검색"
               onChange={e => setQuery(e.target.value)} />
        <Table columns={columns}
               dataSource={professorList}
               onRow={onRow}
               pagination={false} />
      </Modal>
    </Form.Item>
  );
};


export default ProfessorSelect;
