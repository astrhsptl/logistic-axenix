import {
  SERVER_URL,
  SalePointStyles,
  salePointAPI,
  useStoreHook,
} from '@/shared';
import { SalePoint } from '@/shared/interfaces/sale-point';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';
import clsx from 'clsx';
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import ReactSelect from 'react-select';
import { BaseModal } from '.';
import { Char } from '../chart';

interface SalePointProps {}

export const SalePointModal: React.FC<SalePointProps> = () => {
  const { salePointStatement } = useStoreHook();
  const { id } = useParams();
  const [Season, setSeason] = useState(1);
  const { data } = useQuery({
    queryKey: ['salepoint'],
    queryFn: async () => await salePointAPI.fetchByID<SalePoint>(`${id}`),
  });
  const chartData = useQuery({
    queryKey: ['chart'],
    queryFn: async () => {
      const { data } = await axios.post(
        `${SERVER_URL}/predictions/salepoint-category/`,
        {
          id_sale_point: id,
          season_id: Season,
        },
      );
      return data;
    },
  });
  console.log(chartData.data);

  useEffect(() => {
    salePointStatement.open();
  }, []);

  return (
    <BaseModal
      className={clsx(
        SalePointStyles.modalBackground,
        salePointStatement.isActive ? SalePointStyles.active : '',
      )}
      statement={salePointStatement}
      onClick={(event) => {
        event.preventDefault();
        if (event.target === event.currentTarget) {
          salePointStatement.close();
        }
      }}
    >
      <section className={SalePointStyles.center}>
        <div>Торговая точка: {data?.data?.name}</div>
        <div>Адрес: {data?.data?.address}</div>
        <ReactSelect
          onChange={(s) => {
            setSeason(s!.value);
            chartData.refetch();
          }}
          options={[
            { value: 1, label: 'Зима' },
            { value: 2, label: 'Весна' },
            { value: 3, label: 'Лето' },
            { value: 4, label: 'Осень' },
          ]}
        />
        {chartData.data ? <Char data={chartData.data} /> : ''}
      </section>
    </BaseModal>
  );
};
