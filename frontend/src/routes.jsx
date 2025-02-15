import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LicenseList from "./components/LicenseList";
import LicenseDetail from "./components/LicenseDetail";
import UserList from "./pages/users/UserList"; 


const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LicenseList />} />
        <Route path="/licenses/:id" element={<LicenseDetail />} />
        <Route path="/usuarios" element={<UserList />} /> {/*Rota para pastas: models schemas services; e arquivos: user e user_service */}
      </Routes>
    </Router>
  );
};

export default AppRoutes;
