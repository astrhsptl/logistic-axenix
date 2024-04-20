import { BaseAdminStyles, useStoreHook } from '@/shared';
import clsx from 'clsx';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { BaseModal } from '..';
import { AsideLayoutLink } from './interfaces';

interface AsideLayoutProps {
  backLink: AsideLayoutLink;
  links: AsideLayoutLink[];
}

export const AsideLayout: React.FC<AsideLayoutProps> = observer(
  ({ links, backLink }) => {
    const { pathname } = useLocation();
    const { adminModalStatement } = useStoreHook();

    return (
      <BaseModal
        statement={adminModalStatement}
        className={clsx(
          BaseAdminStyles.asideLayout,
          adminModalStatement.isActive ? BaseAdminStyles.active : '',
        )}
      >
        <section className={BaseAdminStyles.asideLogoBar}>
          <div className={BaseAdminStyles.asideLogotype}>
            <img src='/dev-lab-icon.svg' alt='logotype' />
            <span>DevLab</span>
          </div>
          <div
            className={clsx(
              BaseAdminStyles.asideModalSwitcher,
              adminModalStatement.isActive ? BaseAdminStyles.active : '',
            )}
            onClick={adminModalStatement.switchState}
          >
            <img src='/admin-side-arrow.svg' alt='' />
          </div>
        </section>
        <section className={BaseAdminStyles.linkContainer}>
          {links.map(({ link, name }) => (
            <Link
              key={link}
              to={link}
              className={clsx(
                BaseAdminStyles.adminLink,
                link === pathname ? BaseAdminStyles.active : '',
              )}
            >
              {name}
            </Link>
          ))}
        </section>
        <Link to={backLink.link} className={BaseAdminStyles.backLink}>
          {`<  ${backLink.name}`}
        </Link>
      </BaseModal>
    );
  },
);
