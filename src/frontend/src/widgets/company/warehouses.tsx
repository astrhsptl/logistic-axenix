import { DefaultStyle, WareHouse, warehouseAPI } from '@/shared';
import { useGeoLocation } from '@/shared/';
import { useQuery } from '@tanstack/react-query';
import { Map, Overlay } from 'pigeon-maps';

interface WarehousesMapProps {}

export const WarehousesMap: React.FC<WarehousesMapProps> = () => {
  const location = useGeoLocation();
  const { data } = useQuery({
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
      {data?.map((wh) => (
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
