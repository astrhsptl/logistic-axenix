import {
  AdminCompany,
  AdminEntrypoint,
  Drivers,
  Homepage,
  LogOut,
  NewRoute,
  NotFoundPage,
  RedirectNotFound,
  SalePoint,
  SalePoints,
  SignIn,
  SignUp,
} from '@/pages';
import { WareHouses } from '@/pages/admin/company/warehouses';
import '@/shared/styles/base.css';
import { Route, Routes } from 'react-router-dom';

export const AppRouter = () => {
  return (
    <Routes>
      <Route key={'homepage'} element={<Homepage />} path='/' />
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

      <Route
        key={'admin entrypoint'}
        element={<AdminEntrypoint />}
        path='/admin'
      />
      <Route
        key={'admin company'}
        element={<AdminCompany />}
        path='/admin/company'
      />

      <Route
        key={'admin route'}
        element={<NewRoute />}
        path='/admin/company/route'
      />
      <Route
        key={'admin drivers'}
        element={<Drivers />}
        path='/admin/company/drivers'
      />
      <Route
        key={'admin warehouses'}
        element={<WareHouses />}
        path='/admin/company/warehouses'
      />
      <Route
        key={'admin sale-point'}
        element={<SalePoints />}
        path='/admin/company/sale-point'
      />
      <Route
        key={'admin sale-point'}
        element={<SalePoint />}
        path='/admin/company/sale-point/:id'
      />
    </Routes>
  );
};
