import React, { useEffect, useState } from "react";
import spotifyIcon from "./images/Spotify_icon.svg";

import { BrowserRouter as Router, NavLink } from "react-router-dom";

const Header = () => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  return (
    <header className={`header-container ${isVisible ? "visible" : ""}`}>
      <div className="left-header-container">
        <img className="spotify-icon" src={spotifyIcon} alt="icon" />
        <p>ArtistBlender</p>
      </div>
      <NavLink to="/about" className="about">
        About
      </NavLink>
    </header>
  );
};

const ArtistBlender = () => {
  const [isVisible, setIsVisible] = useState(false);
  const [accessToken, setToken] = useState("");

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const handleLogin = async () => {
    try {
      window.location.href = "http://localhost:8000/login";
    } catch (error) {
      console.error("Login redirect failed:", error);
    }
  };

  return (
    <div className={`title-container ${isVisible ? "visible" : ""}`}>
      <h1 className="artistblender">ArtistBlender</h1>
      <p className="subtitle">
        Select your favorite artists and enjoy and their shuffled songs
      </p>
      <button className="sign-up" onClick={handleLogin}>
        Start listening now!
      </button>
    </div>
  );
};

const SignUp = () => {
  return (
    <div>
      <Header />
      <ArtistBlender />
    </div>
  );
};

export default SignUp;
