import { BaseAdminStyles } from '@/shared';
import clsx, { ClassValue } from 'clsx';
import React, { ReactNode } from 'react';
import { AsideLayout } from './aside-layout';
import { AsideLayoutLink } from './interfaces';

interface BaseAdminLayoutProps {
  children: ReactNode;
  links: AsideLayoutLink[];
  backlink: AsideLayoutLink;
  className?: ClassValue;
}

export const BaseAdminLayout: React.FC<BaseAdminLayoutProps> = ({
  className,
  backlink,
  children,
  links,
}) => {
  return (
    <div className={BaseAdminStyles.baseLayout}>
      <AsideLayout links={links} backLink={backlink} />
      <section className={clsx(className)}>{children}</section>
    </div>
  );
};
