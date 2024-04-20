import { BaseAdminLayout } from '@/features';
import { BaseAdminStyles, CompanyLinks } from '@/shared';
import React from 'react';

interface AdminCompanyProps {}

export const AdminCompany: React.FC<AdminCompanyProps> = () => {
  return (
    <BaseAdminLayout
      className={BaseAdminStyles.adminEntrypoint}
      backlink={{
        name: 'Администрация',
        link: '/admin',
      }}
      links={CompanyLinks}
    >
      Предприятие
    </BaseAdminLayout>
  );
};
