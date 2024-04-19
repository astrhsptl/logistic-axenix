import { useAuthentication } from '@/shared/';
import React, { ReactNode, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

interface IsAuthenticatedProtectionProps {
  children: ReactNode;
}

export const IsAuthenticatedProtection: React.FC<
  IsAuthenticatedProtectionProps
> = ({ children }) => {
  const navigate = useNavigate();

  useEffect(() => {
    useAuthentication().then((response) => {
      if (!response) navigate('/sign-in');
      return;
    });
  });

  return <>{children}</>;
};
