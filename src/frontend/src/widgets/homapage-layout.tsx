import { DefaultButton, HomepageStyles } from '@/shared';
import React from 'react';
import { useNavigate } from 'react-router-dom';

interface HomepageLayoutProps {}

export const HomepageLayout: React.FC<HomepageLayoutProps> = () => {
  const navigate = useNavigate();

  return (
    <div className={HomepageStyles.homapageContainer}>
      <div className={HomepageStyles.homapageText}>
        <p className={HomepageStyles.homapageTitle}>
          Место, где идеи становятся реальностью
        </p>
        <p className={HomepageStyles.homapageContent}>
          Наш подход к работе основан на глубоком понимании потребностей
          клиента, тщательном анализе рынка и создании уникальных решений,
          которые помогут достичь поставленных целей.
        </p>
        <DefaultButton
          onClick={() => {
            navigate('/sign-in', { replace: true });
          }}
        >
          Перейти
        </DefaultButton>
      </div>
      <div className={HomepageStyles.imageContainer}>
        <img src='/homepage-preview.png' alt='' />
      </div>
    </div>
  );
};
