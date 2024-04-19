import { AppRouter, Providers } from '@/application/';
import ReactDOM from 'react-dom/client';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <Providers>
    <AppRouter />
  </Providers>,
);
