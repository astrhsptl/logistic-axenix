import { BaseAdminStyles, useStoreHook } from '@/shared';
import clsx, { ClassValue } from 'clsx';
import { observer } from 'mobx-react-lite';
import React, { ReactNode } from 'react';
import { AsideLayout } from './aside-layout';
import { AsideLayoutLink } from './interfaces';

interface BaseAdminLayoutProps {
  children: ReactNode;
  links: AsideLayoutLink[];
  backlink: AsideLayoutLink;
  className?: ClassValue;
}

export const BaseAdminLayout: React.FC<BaseAdminLayoutProps> = observer(
  ({ className, backlink, children, links }) => {
    const {
      adminModalStatement: { isActive },
    } = useStoreHook();

    return (
      <div
        className={clsx(
          BaseAdminStyles.baseLayout,
          isActive ? BaseAdminStyles.active : '',
        )}
      >
        <AsideLayout links={links} backLink={backlink} />
        <section className={clsx(className)}>{children}</section>
      </div>
    );
  },
);
