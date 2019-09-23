import React, {useEffect, useState} from "react";
import {Icon, Table} from "antd";
import { blue } from '@ant-design/colors';
import API from "../../api";


const columns = [
  { title: '선택', dataIndex: 'is_selected', render(is_selected, record, index) {
      return is_selected ? <Icon type="check-circle" /> : false;
    } },
  {title: '분반', dataIndex: 'class_code' },
  {title: '인증구분', dataIndex: 'cert_type' },
  {title: '기준구분', dataIndex: 'base_type' },
  {title: '인증이수구분', dataIndex: 'auth_type'},
  {title: '설계이수구분', dataIndex: 'design_type'},
  {title: '설계학점', dataIndex: 'design_point'}
];


const KlassTable = ({ subject, setKlassPk }) => {
  const [klassList, setKlassList] = useState([]);

  useEffect(() => {
    if ( ! subject ) {
      setKlassList([]);
    }
    else {
      const fetch = async () => {
        const url = `/courses/${subject.pk}/classes/`;
        const {data} = await API.get(url);
        setKlassList(
          data.map(klass => ({
            ...klass,
            is_selected: false
          }))
        );
      };
      fetch();
    }
  }, [subject]);

  const onRow = (record, index) => {
    const { pk, is_selected } = record;
    return {
      onClick: (e) => {
        setKlassPk(record.pk);
        setKlassList(
          klassList.map(klass => ({
            ...klass,
            is_selected: pk === klass.pk
          }))
        );
      },
      style: {
        backgroundColor: is_selected ? blue[2] : null,
        cursor: 'pointer',
        fontWeight: is_selected ? 'bold': null
      }
    };
  };

  return (
    <>
      분반선택 후 입력 (기준구분별 학습성과 및 평가방법이 달라짐)
      <Table dataSource={klassList}
             columns={columns}
             onRow={onRow}
             pagination={false} />
    </>
  );
};


export default KlassTable;
