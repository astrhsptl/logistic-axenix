import { Header } from '@/widgets';
import { SignInLayout } from '@/widgets/';
import React from 'react';

interface SignInProps {}

export const SignIn: React.FC<SignInProps> = () => {
  return (
    <>
      <Header />
      <SignInLayout />
    </>
  );
};
