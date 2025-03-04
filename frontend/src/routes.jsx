import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LicenseList from './pages/LicenseList';
import LicenseDetail from './pages/LicenseDetail';
import UsersList from './pages/UsersList';
import UsersDetail from './pages/UsersDetail';
import Notifications from './pages/Notifications';
import Renewals from './pages/Renewals';
import RenewalsDetail from './pages/RenewalDetail';
import Initial from './pages/Initial';
import Login from './pages/Login';

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/licenses" element={<LicenseList />} />
        <Route path="/licenses/:id" element={<LicenseDetail />} />
        <Route path="/users" element={<UsersList />} />{' '}
        {/*Rota para pastas: models schemas services; e arquivos: user e user_service */}
        <Route path="/users/:id" element={<UsersDetail />} />
        <Route path="/notifications" element={<Notifications />} />
        <Route path="/renewals" element={<Renewals />} />
        <Route path="/renewals/:id" element={<RenewalsDetail />} />
        <Route path="/initial" element={<Initial />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
