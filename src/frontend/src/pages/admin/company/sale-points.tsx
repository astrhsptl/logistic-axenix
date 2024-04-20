import { BaseAdminLayout } from '@/features';
import { BaseAdminStyles, CompanyLinks } from '@/shared';
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
      Торговые точки
    </BaseAdminLayout>
  );
};
