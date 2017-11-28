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
            <input className="validate" id="city" type="text" onChange={onChange}/>
            <label htmlFor="city">City</label>
          </div>
        </div>
        {errors.city && <div className="row"><p className="error-message">{errors.city}</p></div>}
        <div className="row">
          <div className="input-field col s12">
            <input className="validate" id="area" type="text" onChange={onChange}/>
            <label htmlFor="area">Areas</label>
          </div>
        </div>
        {errors.areas && <div className="row"><p className="error-message">{errors.areas}</p></div>}
        <div className="row">
          <div className="input-field col s12">
            <input className="validate" id="min_bedroom" type="number" min="0" step="1" onChange={onChange}/>
            <label htmlFor="min_bedroom">Min Bedroom</label>
          </div>
        </div>
        {errors.min_bedroom && <div className="row"><p className="error-message">{errors.min_bedroom}</p></div>}
        <div className="row">
          <div className="input-field col s12">
            <input className="validate" id="max_bedroom" type="number" min="0" step="1" onChange={onChange}/>
            <label htmlFor="max_bedroom">Max Bedroom</label>
          </div>
        </div>
        {errors.max_bedroom && <div className="row"><p className="error-message">{errors.max_bedroom}</p></div>}
        <div className="row">
          <div className="input-field col s12">
            <input className="validate" id="min_price" type="number" min="0" step="1" onChange={onChange}/>
            <label htmlFor="min_price">Min Price</label>
          </div>
        </div>
        {errors.min_price && <div className="row"><p className="error-message">{errors.min_price}</p></div>}
        <div className="row">
          <div className="input-field col s12">
            <input className="validate" id="max_price" type="number" min="0" step="1" onChange={onChange}/>
            <label htmlFor="max_price">Max Price</label>
          </div>
        </div>
        {errors.max_price && <div className="row"><p className="error-message">{errors.max_price}</p></div>}
        <div className="row">
          <label>Private Bathroom</label>
          <div className="switch">
            <label>
              Off
              <input type="checkbox" onChange={onChange}/>
              <span class="lever"></span>
              On
            </label>
          </div>
        </div>
        <div className="row">
          <label>Time to Work</label>
          <div className="input-field col s6">
            <input className="validate" id="hour" type="number" min="0" step="1" onChange={onChange}/>
            <label htmlFor="hour">Hour</label>
          </div>
          <div className="input-field col s6">
            <input className="validate" id="minute" type="number" min="0" step="1" onChange={onChange}/>
            <label htmlFor="minute">Minute</label>
          </div>
        </div>
        {errors.hour && <div className="row"><p className="error-message">{errors.hour}</p></div>}
        {errors.minute && <div className="row"><p className="error-message">{errors.minute}</p></div>}
        <div className="row">
          <label>Time to Work Delta</label>
          <div className="input-field col s12">
            <input className="validate" id="delta_minute" type="number" min="0" step="1" onChange={onChange}/>
            <label htmlFor="delta_minute">Minute</label>
          </div>
        </div>
        {errors.minute && <div className="row"><p className="error-message">{errors.minute}</p></div>}
        <div className="row">
          <div className="input-field col s12">
            <select>
              <option value="" disabled selected>Choose your option</option>
              <option value="1">transit</option>
              <option value="2">driving</option>
              <option value="3">walking</option>
              <option value="4">bicycling</option>
            </select>
            <label htmlFor="travel_mode">Travel Mode</label>
          </div>
        </div>
        <div className="row">
          <div className="input-field col s12">
            <input className="validate" id="work_addr" type="text" onChange={onChange}/>
            <label htmlFor="work_addr">Work Place Address</label>
          </div>
        </div>
      </form>
    </div>
  </div>
)

RequestForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  onChange: PropTypes.func.isRequired,
  errors: PropTypes.object.isRequired,
  request_form: PropTypes.object.isRequired
}

export default RequestForm
