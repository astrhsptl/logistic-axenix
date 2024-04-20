import { Header } from '@/widgets';
import { HomepageLayout } from '@/widgets/homapage-layout';
import React from 'react';

interface HomepageProps {}

export const Homepage: React.FC<HomepageProps> = () => {
  return (
    <>
      <Header />
      <HomepageLayout />
    </>
  );
};
