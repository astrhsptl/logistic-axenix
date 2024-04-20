import { BaseAdminLayout } from '@/features';
import { BaseAdminStyles, EntrypointLinks } from '@/shared';
import React from 'react';

interface AdminEntrypointProps {}

export const AdminEntrypoint: React.FC<AdminEntrypointProps> = () => {
  return (
    <BaseAdminLayout
      className={BaseAdminStyles.adminEntrypoint}
      links={EntrypointLinks}
      backlink={{
        name: 'Домой',
        link: '/',
      }}
    >
      Администрация
    </BaseAdminLayout>
  );
};
