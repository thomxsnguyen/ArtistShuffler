import React, { useEffect, useState } from "react";
import "./App.css";
import spotifyIcon from "./images/Spotify_icon.svg";
import { BrowserRouter as Router, useNavigate } from "react-router-dom";

const goToRoute = (navigate, path) => {
  navigate(path);
};

const AboutHeader = () => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const navigate = useNavigate();
  return (
    <header className={`header-container ${isVisible ? "visible" : ""}`}>
      <div className="left-header-container">
        <img className="spotify-icon" src={spotifyIcon} alt="icon" />
        <p>ArtistBlender</p>
      </div>
      <div onClick={() => goToRoute(navigate, "/")} className="about">
        Back
      </div>
    </header>
  );
};

const About = () => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  return (
    <>
      <AboutHeader />
      <div className={`about-page ${isVisible ? "visible" : ""}`}>
        <div className="about-container">
          <div className="about-title">About This Project</div>
          <div className="about-info">
            When using Spotify, shuffling songs is essential for variety and
            avoiding repetition. There’s a feature to shuffle all songs by a
            single artist, which helps discover new tracks. However, I recently
            encountered an inconvenience: the inability to shuffle songs from
            multiple artists simultaneously. Although creating a playlist with
            all their songs and shuffling is a workaround, it’s time consuming
            and too much of a hassle. My goal for this project is to develop a
            plugin that allows user to seamless shuffle songs from multiple
            artists without needing to simple playlist
          </div>
        </div>
      </div>
    </>
  );
};

export default About;
