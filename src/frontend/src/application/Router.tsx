import { IsAuthenticatedProtection } from '@/features';
import { LogOut, NotFoundPage, PenisForm } from '@/pages';
import { SignIn, SignUp } from '@/pages/';
import { RedirectNotFound } from '@/pages/redirect-not-found-page';
import '@/shared/styles/base.css';
import { Route, Routes } from 'react-router-dom';

export const AppRouter = () => {
  return (
    <Routes>
      <Route
        key={'home page'}
        element={
          <IsAuthenticatedProtection>
            <PenisForm />
          </IsAuthenticatedProtection>
        }
        path='/'
      />
      <Route
        key={'not found page'}
        element={<NotFoundPage />}
        path='/not-found'
      />
      <Route
        key={'redirect for not found'}
        element={<RedirectNotFound />}
        path='/*'
      />

      <Route key={'logout'} element={<LogOut />} path='/logout' />
      <Route key={'sign in'} element={<SignIn />} path='/sign-in' />
      <Route key={'sign up'} element={<SignUp />} path='/sign-up' />
    </Routes>
  );
};
