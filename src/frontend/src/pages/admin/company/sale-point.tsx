import { BaseAdminLayout } from '@/features';
import { BaseAdminStyles, CompanyLinks } from '@/shared';
import { SalePointMap } from '@/widgets/company/sale-point';
import React from 'react';

interface SalePointProps {}

export const SalePoint: React.FC<SalePointProps> = () => {
  return (
    <BaseAdminLayout
      className={BaseAdminStyles.adminEntrypoint}
      backlink={{
        name: 'Администрация',
        link: '/admin',
      }}
      links={CompanyLinks}
    >
      <SalePointMap />
    </BaseAdminLayout>
  );
};
