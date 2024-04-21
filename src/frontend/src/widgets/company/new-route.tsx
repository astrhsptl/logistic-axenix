import {
  DefaultStyle,
  WareHouse,
  salePointAPI,
  useGeoLocation,
  useStoreHook,
  warehouseAPI,
} from '@/shared';
import { SalePoint } from '@/shared/interfaces/sale-point';
import { useQuery } from '@tanstack/react-query';
import { observer } from 'mobx-react-lite';
import { Map, Overlay } from 'pigeon-maps';
import React from 'react';
import toast from 'react-hot-toast';

interface NewRouteMapProps {}

export const NewRouteMap: React.FC<NewRouteMapProps> = observer(() => {
  const { pointsStatement, pointsChooseStatement } = useStoreHook();
  const location = useGeoLocation();
  const salePointsQuery = useQuery({
    queryKey: ['salepoints'],
    queryFn: async () => await salePointAPI.fetchAll<SalePoint[]>(),
  });
  const warehousesQuery = useQuery({
    queryKey: ['warehouses'],
    queryFn: async () => await warehouseAPI.fetchAll<WareHouse[]>(),
  });

  const addToStatement = (point: SalePoint | WareHouse) => {
    const result = pointsStatement.addPoint(point);

    if (result === 'first') {
      toast.success('Выбран первый адрес');
      pointsChooseStatement.switchState();
      return;
    }

    toast.success('Адрес доставки добавлен');
  };

  return (
    <Map
      defaultCenter={
        location ? [location?.latitude, location?.longitude] : undefined
      }
      center={location ? [location?.latitude, location?.longitude] : undefined}
      defaultZoom={15}
    >
      {salePointsQuery.data?.map((sp) => (
        <Overlay key={sp.id} anchor={[sp.lon, sp.lat]}>
          <img
            className={DefaultStyle.mapPin}
            src='/salepoint-map.png'
            alt='salepoint'
            onClick={() => {
              addToStatement(sp);
            }}
          />
        </Overlay>
      ))}
      {warehousesQuery.data?.map((wh) => (
        <Overlay key={wh.id} anchor={[wh.lon, wh.lat]}>
          <img
            className={DefaultStyle.mapPin}
            src='/warehouse.png'
            alt='warehouse'
            onClick={() => {
              addToStatement(wh);
            }}
          />
        </Overlay>
      ))}
    </Map>
  );
});
