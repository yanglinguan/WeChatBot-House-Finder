import Auth from '../Auth/Auth';
import React from 'react'
import PropTypes from 'prop-types'
import { Link } from 'react-router'
import './Base.css';

const Base = ({ children }) => (
  <div>
    <nav className="nav-bar indigo lighten-1">
      <div className="nav-wrapper">
        <a href="/" className="brand-logo">House Finder</a>
        <ul id="nav-mobile" className="right">
          <div>
            <li><Link to={"/history/userId/" + Auth.getUserId()}>History</Link></li>
          </div>
        </ul>
      </div>
    </nav>
    <br/>
    {children}
  </div>  
);

Base.propTypes = {
    children: PropTypes.object.isRequired
};

export default Base;
