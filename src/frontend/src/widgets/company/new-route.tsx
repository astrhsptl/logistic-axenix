import {
  DefaultStyle,
  WareHouse,
  salePointAPI,
  useGeoLocation,
  warehouseAPI,
} from '@/shared';
import { SalePoint } from '@/shared/interfaces/sale-point';
import { useQuery } from '@tanstack/react-query';
import { Map, Overlay } from 'pigeon-maps';
import React from 'react';

interface NewRouteMapProps {}

export const NewRouteMap: React.FC<NewRouteMapProps> = () => {
  const location = useGeoLocation();
  const salePointsQuery = useQuery({
    queryKey: ['salepoint'],
    queryFn: async () => await salePointAPI.fetchAll<SalePoint>(),
  });
  const wirehousesQuery = useQuery({
    queryKey: ['warehouse'],
    queryFn: async () => await warehouseAPI.fetchAll<WareHouse>(),
  });

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
              console.log('asd');
            }}
          />
        </Overlay>
      ))}
      {wirehousesQuery.data?.map((wh) => (
        <Overlay key={wh.id} anchor={[wh.lon, wh.lat]}>
          <img
            className={DefaultStyle.mapPin}
            src='/warehouse.png'
            alt='warehouse'
            onClick={() => {
              console.log('asd');
            }}
          />
        </Overlay>
      ))}
    </Map>
  );
};
