import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LicenseList from "./components/LicenseList";
import LicenseDetail from "./components/LicenseDetail";

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LicenseList />} />
        <Route path="/licenses/:id" element={<LicenseDetail />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
