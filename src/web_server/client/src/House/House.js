import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router';
import './House.css';

class House extends React.Component {
  render() {
    return (
      <Link to={"/requestDetail/userId/" + this.props.user_id + "/requestId/" + this.props.request_id} className="collection-item">
        {this.props.listing.city}
      </Link>
    )
  }
}

House.propTypes = {
  listing: PropTypes.object.isRequired,
  request_id: PropTypes.string.isRequired,
  user_id: PropTypes.string.isRequired,
}

export default House
