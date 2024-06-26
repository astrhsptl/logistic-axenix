import { DefaultStyle, salePointAPI } from '@/shared';
import { useGeoLocation } from '@/shared/';
import { SalePoint } from '@/shared/interfaces/sale-point';
import { useQuery } from '@tanstack/react-query';
import { Map, Overlay } from 'pigeon-maps';
import { useNavigate } from 'react-router-dom';

interface SalePointsMapProps {}

export const SalePointsMap: React.FC<SalePointsMapProps> = () => {
  const location = useGeoLocation();
  const navigate = useNavigate();
  const { data, isLoading } = useQuery({
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
    >
      {data && isLoading === false
        ? data.map((sp) => (
            <Overlay key={sp.id} anchor={[sp.lon, sp.lat]}>
              <img
                className={DefaultStyle.mapPin}
                src='/salepoint-map.png'
                alt='salepoint'
                onClick={() => {
                  navigate(`/admin/company/sale-point/${sp.id}`, {
                    replace: true,
                  });
                }}
              />
            </Overlay>
          ))
        : ''}
    </Map>
  );
};
