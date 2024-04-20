import { BaseAdminLayout, DriverCard } from '@/features';
import { BaseAdminStyles, CompanyLinks, Driver, DriverStyles } from '@/shared';
import { driverAPI } from '@/shared/api';
import { useQuery } from '@tanstack/react-query';
import React from 'react';

interface DriversProps {}

export const Drivers: React.FC<DriversProps> = () => {
  const { data } = useQuery({
    queryKey: ['drivers'],
    queryFn: () => driverAPI.fetchAll<Driver>(),
  });

  console.log('data', data);

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
        {[1, 2, 3, 4].map((a) => (
          <DriverCard
            key={a}
            driver={{
              first_name: 'Vasya',
              last_name: 'Pidorov',
              id: 'Pidorov',
              phone: 79604469320,
              volume: 1000,
            }}
            point_from={{
              address: 'Pidorkovo 19 s',
              id: 'asdfasdg',
              lat: 99,
              lon: 112,
              name: 'Shaitanovo',
              volume: 12241234,
            }}
            point_to={{
              address: 'Pidorkovo 19 s',
              id: 'asdfasdg',
              lat: 99,
              lon: 112,
              name: 'Shaitanovo',
              volume: 12241234,
            }}
            products={[
              {
                cost: 777,
                expiration_date: Date.now().toString(),
                id: 'asdfasdf',
                id_category: 'asdf',
                id_sale_point: 'asdf',
                id_shipment: 'asdfgashg',
                id_warehouse: ' asdfasgd',
                name: 'someonekovo',
                product_quantity: 1234,
                volume: 123,
                weight: 777,
              },
              {
                cost: 777,
                expiration_date: Date.now().toString(),
                id: 'asdfasdf',
                id_category: 'asdf',
                id_sale_point: 'asdf',
                id_shipment: 'asdfgashg',
                id_warehouse: ' asdfasgd',
                name: 'someonekovo',
                product_quantity: 1234,
                volume: 123,
                weight: 777,
              },
              {
                cost: 777,
                expiration_date: Date.now().toString(),
                id: 'asdfasdf',
                id_category: 'asdf',
                id_sale_point: 'asdf',
                id_shipment: 'asdfgashg',
                id_warehouse: ' asdfasgd',
                name: 'someonekovo',
                product_quantity: 1234,
                volume: 123,
                weight: 777,
              },
              {
                cost: 777,
                expiration_date: Date.now().toString(),
                id: 'asdfasdf',
                id_category: 'asdf',
                id_sale_point: 'asdf',
                id_shipment: 'asdfgashg',
                id_warehouse: ' asdfasgd',
                name: 'someonekovo',
                product_quantity: 1234,
                volume: 123,
                weight: 777,
              },
            ]}
          />
        ))}
      </section>
    </BaseAdminLayout>
  );
};
