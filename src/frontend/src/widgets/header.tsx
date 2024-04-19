import { BurgerMenu } from '@/features';
import { HeaderStyles, useAuthentication, useStoreHook } from '@/shared';
import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

interface HeaderProps {}

const HeaderFc: React.FC<HeaderProps> = () => {
  const {
    burgerStatement: { switchState },
  } = useStoreHook();
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    useAuthentication().then((response) => {
      if (!response) return navigate('/sign-in');
      setIsAuthenticated(true);
      return;
    });
  });

  return (
    <header className={HeaderStyles.header}>
      <article className={HeaderStyles.icon}>
        <img src='/dev-lab-icon.svg' alt='icon' />
        <span>DevLab</span>
      </article>
      <article className={HeaderStyles.linkContainer}>
        {isAuthenticated ? (
          <>
            <Link to='/logout'>Выход</Link>
          </>
        ) : (
          <>
            <Link to='/sign-in'>Вход</Link>
            <Link to='/sign-up'>Регистрация</Link>
          </>
        )}
      </article>
      <article className={HeaderStyles.burger}>
        <img src='/burger.svg' alt='Меню' onClick={switchState} />
        <BurgerMenu isAuthenticated={isAuthenticated} />
      </article>
    </header>
  );
};

export const Header = React.memo(HeaderFc);
