import { BaseAdminLayout, DriverCard } from '@/features';
import {
  BaseAdminStyles,
  CompanyLinks,
  Driver,
  DriverStyles,
  driverAPI,
} from '@/shared';
import { useQuery } from '@tanstack/react-query';
import React from 'react';

interface DriversProps {}

export const Drivers: React.FC<DriversProps> = () => {
  const { data } = useQuery({
    queryKey: ['drivers'],
    queryFn: async () => await driverAPI.fetchAll<Driver[]>(),
  });

  return (
    <BaseAdminLayout
      className={BaseAdminStyles.adminEntrypoint}
      backlink={{
        name: 'Администрация',
        link: '/admin',
      }}
      links={CompanyLinks}
    >
      <section></section>
      <section className={DriverStyles.driverContainer}>
        {data?.map((driver) => (
          <DriverCard
            key={driver.id}
            driver={driver}
            point_from={{
              address: 'Склад 2',
              id: 'asdfasdg',
              lat: 99,
              lon: 112,
              name: 'Склад 2',
              volume: 12241234,
            }}
            point_to={{
              address: 'Клиент 1',
              id: 'asdfasdg',
              lat: 99,
              lon: 112,
              name: 'Клиент 1',
              volume: 12241234,
            }}
            products={[]}
          />
        ))}
      </section>
    </BaseAdminLayout>
  );
};
