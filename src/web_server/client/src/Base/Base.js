import Auth from '../Auth/Auth';
import React, { PropTypes } from 'react'
import { Link } from 'react-router'
import './Base.css';

const Base = ({ children }) => (
  <div>
    <nav className="nav-bar indigo lighten-1">
      <div className="nav-wrapper">
        <a href="/" className="brand-logo">House Finder</a>
        <ul id="nav-mobile" className="right">
          <div>
            <li><Link to="/history"> History </Link></li>
          </div>
        </ul>
      </div>
    </nav>
    <br/>
    {children}
  </div>  
);

Base.propType = {
  children: PropType.object.isRequired
};

export default Base;
