import { SalePointModal } from '@/features/modal/sale-point';
import { DefaultStyle, salePointAPI } from '@/shared';
import { useGeoLocation } from '@/shared/';
import { SalePoint } from '@/shared/interfaces/sale-point';
import { useQuery } from '@tanstack/react-query';
import { Map, Overlay } from 'pigeon-maps';
import { useNavigate } from 'react-router-dom';

interface SalePointMapProps {}

export const SalePointMap: React.FC<SalePointMapProps> = () => {
  const location = useGeoLocation();
  const navigate = useNavigate();
  const { data } = useQuery({
    queryKey: ['salepoints'],
    queryFn: async () => await salePointAPI.fetchAll<SalePoint[]>(),
  });

  return (
    <Map
      defaultCenter={
        location ? [location?.latitude, location?.longitude] : undefined
      }
      center={location ? [location?.latitude, location?.longitude] : undefined}
      defaultZoom={15}
      onClick={() => navigate('/admin/company/sale-point')}
    >
      {data?.map((sp) => (
        <Overlay key={sp.id} anchor={[sp.lon, sp.lat]}>
          <img
            className={DefaultStyle.mapPin}
            src='/salepoint-map.png'
            alt='salepoint'
          />
        </Overlay>
      ))}
      <SalePointModal />
    </Map>
  );
};
