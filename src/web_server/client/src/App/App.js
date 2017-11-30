import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.js';

import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { Link } from 'react-router';
import PropTypes from 'prop-types';

class App extends Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      user_id: context.router.params.userId
    }
  }
  render() {
    return (
      <div>
        <div className='container'>
          <div className="collection">
            <Link to={"/requestForm/userId/" + this.state.user_id} className="collection-item">New Request</Link>
            <Link to={"/history/userId/" + this.state.user_id} className="collection-item">History</Link>
          </div>
        </div>
      </div>
    );
  }
}

App.contextTypes = {
  router: PropTypes.object.isRequired
}

export default App;
