import { Driver, DriverStyles, Product, WareHouse } from '@/shared';
import { SalePoint } from '@/shared/interfaces/sale-point';
import clsx from 'clsx';
import React from 'react';

interface DriverCardProps {
  driver: Driver;
  products: Product[];
  point_from: WareHouse | SalePoint;
  point_to: WareHouse | SalePoint;
}

const countTotalProductControlCount = (
  products: Product[],
  controlParameter: 'cost' | 'volume' | 'weight',
) => {
  let totalControlCount = 0;

  products.forEach(
    (product) => (totalControlCount += product[controlParameter]),
  );

  return totalControlCount;
};

export const DriverCard: React.FC<DriverCardProps> = ({
  driver,
  products,
  point_from,
  point_to,
}) => {
  const totalProductVolume = countTotalProductControlCount(products, 'volume');
  const usedDriverVolume = (totalProductVolume / driver.volume) * 100;

  console.log();

  return (
    <article className={DriverStyles.baseLayout}>
      <div className={DriverStyles.driverTitle}>
        <span>
          {point_from.name} - {point_to.name}
        </span>
        <span
          className={clsx(
            usedDriverVolume > 75 ? DriverStyles.textColorFullFilled : '',
            usedDriverVolume <= 75 && usedDriverVolume >= 30
              ? DriverStyles.textColorMiddleFilled
              : DriverStyles.textColorLightFilled,
          )}
        >
          {usedDriverVolume}%
        </span>
      </div>

      <div className={DriverStyles.driverInfo}>
        <div>
          Вес продукта: {countTotalProductControlCount(products, 'weight')}
        </div>
        <div>
          {driver.first_name.slice(0, 1)}. {driver.last_name}
        </div>
        <div>Телефон: {driver.phone}</div>
      </div>

      <div className={DriverStyles.truck}>
        <div
          className={clsx(
            DriverStyles.truckVolumeIndicator,
            usedDriverVolume > 75 ? DriverStyles.colorFullFilled : '',
            usedDriverVolume <= 75 && usedDriverVolume >= 30
              ? DriverStyles.colorMiddleFilled
              : DriverStyles.colorLightFilled,
          )}
          style={{ width: 1.5 * usedDriverVolume }}
        ></div>
        <img
          src='/truck-template.png'
          alt=''
          className={DriverStyles.truckImage}
        />
      </div>
    </article>
  );
};
