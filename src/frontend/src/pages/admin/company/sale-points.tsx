import { BaseAdminLayout } from '@/features';
import { BaseAdminStyles, CompanyLinks } from '@/shared';
import { SalePointsMap } from '@/widgets';
import React from 'react';

interface SalePointsProps {}

export const SalePoints: React.FC<SalePointsProps> = () => {
  return (
    <BaseAdminLayout
      className={BaseAdminStyles.adminEntrypoint}
      backlink={{
        name: 'Администрация',
        link: '/admin',
      }}
      links={CompanyLinks}
    >
      <SalePointsMap />
    </BaseAdminLayout>
  );
};
