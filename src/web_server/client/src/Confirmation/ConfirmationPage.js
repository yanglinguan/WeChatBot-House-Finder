import React from 'react'
import PropTypes from 'prop-types'
import { Link } from 'react-router'

class ConfirmationPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      user_id: context.router.params.userId
    }
  }

  render() {
    return (
      <div className="container">
        <h>Thank you for submitting your request...</h>
        <div className="row right-align">
          <Link to={"/home/userId/" + this.state.user_id} className="waves-effect waves-light btn">Home</Link>
        </div>
      </div>  
    );
  }  
}

ConfirmationPage.contextTypes = {
  router: PropTypes.object.isRequired
}

export default ConfirmationPage
