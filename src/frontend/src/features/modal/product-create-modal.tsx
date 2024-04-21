import {
  DefaultButton,
  DeliverStyle,
  Driver,
  Product,
  driverAPI,
  productAPI,
  useStoreHook,
} from '@/shared';
import { useQuery } from '@tanstack/react-query';
import clsx from 'clsx';
import { observer } from 'mobx-react-lite';
import React, { useState } from 'react';
import toast from 'react-hot-toast';
import ReactSelect from 'react-select';
import { BaseModal } from '.';

interface ProductCreateProps {}

export const ProductCreateModal: React.FC<ProductCreateProps> = observer(() => {
  const { productCreateStatement } = useStoreHook();
  const [ProductId, setProductId] = useState<string | undefined>(undefined);
  const [driverId, setDriverId] = useState<string | undefined>(undefined);
  const drivers = useQuery({
    queryKey: ['drivers'],
    queryFn: async () => await driverAPI.fetchAll<Driver[]>(),
  });
  const products = useQuery({
    queryKey: ['products'],
    queryFn: async () => await productAPI.fetchAll<Product[]>(),
  });

  return (
    <BaseModal
      className={clsx(
        DeliverStyle.modalCreateBackground,
        productCreateStatement.isActive ? DeliverStyle.active : '',
      )}
      statement={productCreateStatement}
      onClick={(event) => {
        event.preventDefault();
        if (event.target === event.currentTarget) {
          productCreateStatement.close();
        }
      }}
    >
      <section className={DeliverStyle.center}>
        <p>Выберите водителя</p>
        <ReactSelect
          required={true}
          onChange={(s) => {
            setDriverId(s?.value);
          }}
          options={drivers?.data?.map((driver) => {
            return {
              value: driver.id,
              label: `${driver.first_name.slice(0, 1)} ${driver.last_name}`,
            };
          })}
        />
        <p>Выберите продукт</p>
        <ReactSelect
          required={true}
          onChange={(s) => {
            setProductId(s?.value);
          }}
          options={products?.data?.map((product) => {
            return {
              value: product.id,
              label: product.name,
            };
          })}
        />
        <DefaultButton
          className={DeliverStyle.createButton}
          onClick={() => {
            if (!ProductId) {
              toast.error('Не выбран продукт');
              return;
            }
            if (!driverId) {
              toast.error('Не выбран водитель');
              return;
            }
          }}
        >
          Утвердить
        </DefaultButton>
      </section>
    </BaseModal>
  );
});
