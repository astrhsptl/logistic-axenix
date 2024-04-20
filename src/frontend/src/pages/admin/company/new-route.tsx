import { BaseAdminLayout } from '@/features';
import { BaseAdminStyles, CompanyLinks } from '@/shared';
import { useGeoLocation } from '@/shared/internal-tools/geolocation';
import { Map } from 'pigeon-maps';
import React from 'react';

interface NewRouteProps {}

export const NewRoute: React.FC<NewRouteProps> = () => {
  const location = useGeoLocation();

  return (
    <BaseAdminLayout
      className={BaseAdminStyles.adminEntrypoint}
      backlink={{
        name: 'Администрация',
        link: '/admin',
      }}
      links={CompanyLinks}
    >
      <Map
        defaultCenter={
          location ? [location?.latitude, location?.longitude] : undefined
        }
        center={
          location ? [location?.latitude, location?.longitude] : undefined
        }
        defaultZoom={15}
      ></Map>
    </BaseAdminLayout>
  );
};
