import { BaseAdminLayout } from '@/features';
import { BaseAdminStyles } from '@/shared';
import React from 'react';

interface AdminEntrypointProps {}

const links = [
  { name: 'Администрация', link: 'admin' },
  { name: 'Аналитика', link: 'analytics' },
  { name: 'Грузилово', link: 'gruzilovo' },
];

export const AdminEntrypoint: React.FC<AdminEntrypointProps> = () => {
  return (
    <BaseAdminLayout className={BaseAdminStyles.adminEntrypoint} links={links}>
      Администрация
    </BaseAdminLayout>
  );
};
