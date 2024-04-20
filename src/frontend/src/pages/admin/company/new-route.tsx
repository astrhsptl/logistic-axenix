import { AdminDeliverPoints, BaseAdminLayout } from '@/features';
import { BaseAdminStyles, CompanyLinks } from '@/shared';
import { NewRouteMap } from '@/widgets';
import React from 'react';

interface NewRouteProps {}

export const NewRoute: React.FC<NewRouteProps> = () => {
  return (
    <BaseAdminLayout
      className={BaseAdminStyles.adminEntrypoint}
      backlink={{
        name: 'Администрация',
        link: '/admin',
      }}
      links={CompanyLinks}
    >
      <NewRouteMap />
      <AdminDeliverPoints />
    </BaseAdminLayout>
  );
};
