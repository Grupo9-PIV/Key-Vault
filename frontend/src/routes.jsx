import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LicenseList from "./pages/LicenseList/LicenseList";
import LicenseDetail from "./pages/LicenseDetail/LicenseDetail";
import UsersList from "./pages/UsersList/UsersList"; 
import UsersDetail from "./pages/UsersDetail/UsersDetail"; 
import Notifications from "./pages/Notifications/Notifications";
import Renewals from "./pages/Renewals/Renewals";
import RenewalsDetail from "./pages/RenewalDetail/RenewalDetail";
import Initial from "./pages/initial";


const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LicenseList />} />
        <Route path="/licenses/:id" element={<LicenseDetail />} />
        <Route path="/users" element={<UsersList />} /> {/*Rota para pastas: models schemas services; e arquivos: user e user_service */}
        <Route path="/users/:id" element={<UsersDetail />} />
        <Route path="/notifications" element={<Notifications />} />
        <Route path="/renewal_requests" element={<Renewals />} />
        <Route path="/renewals/:id" element={<RenewalsDetail />} />
        <Route path="/initial" element={<Initial />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
