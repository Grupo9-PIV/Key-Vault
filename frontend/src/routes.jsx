import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LicenseList from "./pages/LicenseList/LicenseList";
import LicenseDetail from "./pages/LicenseDetail/LicenseDetail";
import UserList from "./pages/UsersList/UsersList"; 
import UserList from "./pages/UsersDetail/UsersDetail"; 

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LicenseList />} />
        <Route path="/licenses/:id" element={<LicenseDetail />} />
        <Route path="/users" element={<UserList />} /> {/*Rota para pastas: models schemas services; e arquivos: user e user_service */}
        <Route path="/users/:id" element={<UsersDetail />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
