import { DefaultStyle, salePointAPI } from '@/shared';
import { useGeoLocation } from '@/shared/';
import { SalePoint } from '@/shared/interfaces/sale-point';
import { useQuery } from '@tanstack/react-query';
import { Map, Overlay } from 'pigeon-maps';

interface SalePointsMapProps {}

export const SalePointsMap: React.FC<SalePointsMapProps> = () => {
  const location = useGeoLocation();
  const { data } = useQuery({
    queryKey: ['salepoint'],
    queryFn: async () => await salePointAPI.fetchAll<SalePoint>(),
  });

  return (
    <Map
      defaultCenter={
        location ? [location?.latitude, location?.longitude] : undefined
      }
      center={location ? [location?.latitude, location?.longitude] : undefined}
      defaultZoom={15}
    >
      {data?.map((sp) => (
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
    </Map>
  );
};
