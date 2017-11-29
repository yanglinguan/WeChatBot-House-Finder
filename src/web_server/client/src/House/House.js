import Auth from "../Auth/Auth";
import React from 'react';
import { Link } from 'react-router';
import './House.css';

class House extends React.Component {
  
  render() {
    return (
    <div className="container">
      <div className="row">
        <div className="col s8">
          <Link to={"/requestForm/userId/" + Auth.getUserId() + "/requestId/" + this.props.listings.request_id}>{this.props.listings.city}</Link>
        </div>
      </div>  
    </div>
    )
  }
  
}

export default House
