import React, {PropTypes} from 'react'
import { Link } from 'react-router'

import './RequestForm.css'

const RequestForm = ({
  onSubmit,
  onChange,
  errors,
  user
}) => (
  <div className="container">
    <div className="request-panel">
      <form className="col s12" action="/" onSubmit={onSubmit}>
        <h4 className="center-align">House Search Request</h4>
        {errors.summary && <div className="row"><p className="error-message">{errors.summary}</p></div>}
        <div className="row">
          <div className="input-field col s12">
            <input className="validate" id="city" type="text">
            <lable for="city">City</lable>
          </div>
          <div className="input-field"
        </div>
      </form>
    </div>
  </div>
)
