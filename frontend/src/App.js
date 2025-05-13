import React, { useEffect, useState } from "react";
import SignUp from "./Home.js";
import About from "./About.js";
import "./App.css";
import spotifyIcon from "./images/Spotify_icon.svg";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  NavLink,
  useLocation,
  useNavigate,
} from "react-router-dom";

const AppContent = () => {
  return (
    <Routes>
      <Route path="/" element={<SignUp />} />
      <Route path="/about" element={<About />} />
    </Routes>
  );
};

const App = () => {
  return (
    <main className="app">
      <Router>
        <AppContent />
      </Router>
    </main>
  );
};

export default App;
