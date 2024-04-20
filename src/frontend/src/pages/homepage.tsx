import { Header } from '@/widgets';
import React from 'react';
import { DefaultButton } from '@/shared';
import HomepageProps from './homepage.module.scss';

interface HomepageProps {}

const HomepageFC: React.FC<HomepageProps> = () => {
  return (
    <>
      <Header />
      <section className='wrapper'>
        <article className='but'>
          <h2>
            Место, где идеи
            <br/>
            становятся реальностью
          </h2>
          <p>
            Наш подход к работе основан на глубоком понимании потребностей
            клиента, тщательном анализе рынка и создании уникальных решений,
            которые помогут достичь поставленных целей.
          </p>
          <DefaultButton style='d'>Админ панель</DefaultButton>
        </article>
        <article className='logo'>
          <img src='Group 25.svg' alt='' />
        </article>
      </section>
    </>
  );
};

export const Homepage = React.memo(HomepageFC);