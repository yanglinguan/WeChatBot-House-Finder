import React from 'react'
import PropTypes from 'prop-types';
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
        <h4 className="center-align">House Search Request Form</h4>
        {errors.summary && <div className="row"><p className="error-message">{errors.summary}</p></div>}
        <div className="row">
          <div className="input-field col s6">
            <input className="validate" id="city" type="text" name="city" required="" aria-required="true" onChange={onChange}/>
            <label htmlFor="city">City</label>
          </div>
          <div className="input-field col s6">
            <input className="validate" id="areas" type="text" name="areas" required="" aria-required="true" onChange={onChange}/>
            <label htmlFor="areas">Areas</label>
          </div>
        </div>
        {errors.city && <div className="row"><p className="error-message">{errors.city}</p></div>}
        {errors.areas && <div className="row"><p className="error-message">{errors.areas}</p></div>}
        <div className="row">
          <div className="input-field col s6">
            <input className="validate" id="min_bedroom" name="min_bedroom" type="number" required="" aria-required="true" min="0" step="1" onChange={onChange}/>
            <label htmlFor="min_bedroom">Min Bedroom</label>
          </div>
          <div className="input-field col s6">
            <input className="validate" id="max_bedroom" name="max_bedroom" required="" aria-required="true" type="number" min="0" step="1" onChange={onChange}/>
            <label htmlFor="max_bedroom">Max Bedroom</label>
          </div>
        </div>
        {errors.min_bedroom && <div className="row"><p className="error-message">{errors.min_bedroom}</p></div>}
        {errors.max_bedroom && <div className="row"><p className="error-message">{errors.max_bedroom}</p></div>}
        <div className="row">
          <div className="input-field col s6">
            <input className="validate" id="min_price" type="number" required="" aria-required="true" name="min_price" min="0" step="1" onChange={onChange}/>
            <label htmlFor="min_price">Min Price</label>
          </div>
          <div className="input-field col s6">
            <input className="validate" id="max_price" type="number" required="" aria-required="true" name="max_price" min="0" step="1" onChange={onChange}/>
            <label htmlFor="max_price">Max Price</label>
          </div>
        </div>
        {errors.min_price && <div className="row"><p className="error-message">{errors.min_price}</p></div>}
        {errors.max_price && <div className="row"><p className="error-message">{errors.max_price}</p></div>}
        <div className="row">
          <div className="input-field col s6">
            <input className="validate" id="hour" type="number" name="time_to_work_hour" min="0" step="1" onChange={onChange}/>
            <label htmlFor="hour">Time to Work(Hour)</label>
          </div>
          <div className="input-field col s6">
            <input className="validate" id="minute" type="number" min="0" name="time_to_work_minute" step="1" max="59" onChange={onChange}/>
            <label htmlFor="minute">Time to Work(Minute)</label>
          </div>
        </div>
        {errors.time_to_work_hour && <div className="row"><p className="error-message">{errors.time_to_work_hour}</p></div>}
        {errors.time_to_work_minute && <div className="row"><p className="error-message">{errors.time_to_work_minute}</p></div>}
        <div className="row">
          <div className="input-field col s6">
            <input className="validate" id="hour" type="number" name="departure_to_work_hour" min="0" step="1" max="23" onChange={onChange}/>
            <label htmlFor="hour">Departure to Work(Hour)</label>
          </div>
          <div className="input-field col s6">
            <input className="validate" id="minute" type="number" min="0" name="departure_to_work_minute" step="1" max="59" onChange={onChange}/>
            <label htmlFor="minute">Departure to Work(Minute)</label>
          </div>
        </div>
        {errors.departure_to_work_hour && <div className="row"><p className="error-message">{errors.departure_to_work_hour}</p></div>}
        {errors.departure_to_work_minute && <div className="row"><p className="error-message">{errors.departure_to_work_minute}</p></div>}

        <div className="row">
          <div className="input-field col s12">
            <input className="validate" id="delta_minute" type="number" name="delta_minute" min="0" step="1" onChange={onChange}/>
            <label htmlFor="delta_minute">Time to Work Delta(Minute)</label>
          </div>
        </div>
        {errors.delta_minute && <div className="row"><p className="error-message">{errors.delta_minute}</p></div>}
                <div className="row">
          <div className="input-field col s12">
            <input className="validate" id="work_addr" type="text" required="" aria-required="true" name="work_addr" onChange={onChange}/>
            <label htmlFor="work_addr">Work Place Address</label>
          </div>
        </div>
        {errors.work_addr && <div className="row"><p className="error-message">{errors.work_addr}</p></div>}
        <div className="row">
          <label htmlFor="travel_mode">Travel Mode</label>
          <p>
            <input className="with-gap" name="travel_mode" value="transit" type="radio" id="transit" required   onChange={onChange} />
            <label htmlFor="transit">Transit</label>
          </p>
          <p>
            <input className="with-gap" required name="travel_mode" type="radio" value="driving" id="driving" onChange={onChange} />
            <label htmlFor="driving">Driving</label>
          </p>
          <p>
            <input className="with-gap" required name="travel_mode" type="radio" value="walking" id="walking" onChange={onChange}/>
            <label htmlFor="walking">Walking</label>
          </p>
          <p>
            <input className="with-gap" required name="travel_mode" type="radio" id="bicycling" value="bicycling" onChange={onChange} />
            <label htmlFor="bicycling">Bicycling</label>
          </p>    
        </div>

        <div className="row">
          <label>Private Bathroom</label>
          <p>
            <input className="with-gap" value="true" required name="private_bath" type="radio" id="private_bath_yes"  onChange={onChange} />
            <label htmlFor="private_bath_yes">Yes</label>
          </p>
          <p>
            <input className="with-gap" value="false" required name="private_bath" type="radio" id="private_bath_no" onChange={onChange} />
            <label htmlFor="private_bath_no">No</label>
          </p>

        </div>

        <div className="row right-align">
            <input type="submit" className="waves-effect waves-light btn indigo lighten-1" value='Submit'/>
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
