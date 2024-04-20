import { BaseAdminLayout } from '@/features';
import { BaseAdminStyles, CompanyLinks } from '@/shared';
import React from 'react';

interface DriversProps {}

export const Drivers: React.FC<DriversProps> = () => {
  return (
    <BaseAdminLayout
      className={BaseAdminStyles.adminEntrypoint}
      backlink={{
        name: 'Администрация',
        link: '/admin',
      }}
      links={CompanyLinks}
    >
      Водители
    </BaseAdminLayout>
  );
};
