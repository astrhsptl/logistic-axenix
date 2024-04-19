import { HeaderStyles, useStoreHook } from '@/shared';
import clsx from 'clsx';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { Link } from 'react-router-dom';
import { BaseModal } from '.';

interface BurgerMenuProps {
  isAuthenticated?: boolean;
}

export const BurgerMenu: React.FC<BurgerMenuProps> = observer(
  ({ isAuthenticated }) => {
    const { burgerStatement } = useStoreHook();

    return (
      <BaseModal
        className={clsx(
          HeaderStyles.burgerModal,
          burgerStatement.isActive ? HeaderStyles.activeModal : '',
        )}
        statement={burgerStatement}
      >
        <nav className={HeaderStyles.nav}>
          <div className={HeaderStyles.navHead}>
            <img src='/dev-lab-icon-white.svg' alt='icon' />
            <span>DevLab</span>
          </div>
          {isAuthenticated ? (
            <>
              <Link to='/logout' onClick={burgerStatement.switchState}>
                Выход
              </Link>
            </>
          ) : (
            <>
              <Link to='/sign-in' onClick={burgerStatement.switchState}>
                Вход
              </Link>
              <Link to='/sign-up' onClick={burgerStatement.switchState}>
                Регистрация
              </Link>
            </>
          )}
        </nav>

        <div onClick={burgerStatement.switchState}></div>
      </BaseModal>
    );
  },
);
