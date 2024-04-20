import { BaseAdminLayout } from '@/features';
import { BaseAdminStyles, CompanyLinks } from '@/shared';
import { WarehousesMap } from '@/widgets/';
import React from 'react';

interface WareHousesProps {}

export const WareHouses: React.FC<WareHousesProps> = () => {
  return (
    <BaseAdminLayout
      className={BaseAdminStyles.adminEntrypoint}
      backlink={{
        name: 'Администрация',
        link: '/admin',
      }}
      links={CompanyLinks}
    >
      <WarehousesMap />
    </BaseAdminLayout>
  );
};
