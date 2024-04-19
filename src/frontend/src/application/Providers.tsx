import { RootStore } from '@/entities';
import { RootStoreContext } from '@/shared';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import React, { ReactNode } from 'react';
import { BrowserRouter } from 'react-router-dom';

interface ProvidersProps {
  children: ReactNode;
}

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
    },
  },
});

export const Providers: React.FC<ProvidersProps> = ({ children }) => {
  return (
    <React.StrictMode>
      <BrowserRouter>
        <QueryClientProvider client={queryClient}>
          <RootStoreContext.Provider value={RootStore}>
            {children}
          </RootStoreContext.Provider>
        </QueryClientProvider>
      </BrowserRouter>
    </React.StrictMode>
  );
};
