import Auth from '../Auth/Auth'
import './RequestFormPage.css';
import React from 'react';
import PropTypes from 'prop-types';
import RequestForm from './RequestForm';

class RequestFormPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      errors: {},
      message: '',
      user_id: context.router.params.userId,
      request_form: {
        areas: '',
        city: '',
        departure_to_work_hour: 0,
        departure_to_work_minute: 0,
        max_bedroom: 0,
        min_bedroom: 0,
        max_price: 0,
        min_price: 0,
        private_bath: true,
        time_to_work_hour: 0,
        time_to_work_minute: 0,
        delta_minute: 0,
        travel_mode: 'transit',
        work_addr: ''
      }
    };

    this.processForm = this.processForm.bind(this);
    this.changeUser = this.changeUser.bind(this);
  }

  componentDidMount() {
    console.log("log");
    console.log(this.state.user_id);
    Auth.authenticateUser(this.state.user_id);
  }

  processForm(event) {
    event.preventDefault();
    
    const user_id = this.state.user_id;

    let url = 'http://localhost:3001/requestForm/userId/' + this.state.user_id;

    const request_form = this.state.request_form
    const areaArray = request_form.areas.split(",");
    let areaList = []
    for(var a in areaArray){
      areaList.push(areaArray[a]);
    }
    
    const form = JSON.stringify({
        areas:areaList,
        city: this.state.request_form.city,
        departure_to_work_hour: this.state.request_form.departure_to_work_hour,
        departure_to_work_minute: this.state.request_form.departure_to_work_minute,
        max_bedroom: this.state.request_form.max_bedroom,
        min_bedroom: this.state.request_form.min_bedroom,
        max_price: this.state.request_form.max_price,
        min_price: this.state.request_form.min_price,
        time_to_work: this.state.request_form.time_to_work_hour * 60 * 60 + this.state.request_form.time_to_work_minute * 60,
        time_to_work_delta: this.state.request_form.delta_minute,
        travel_mode: this.state.request_form.travel_mode,
        work_addr: this.state.request_form.work_addr,
        private_bath: this.state.request_form.private_bath
      });

    console.log(form);

    fetch(url, {
      method: "POST",
      body: form,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      cache: false
    })
      .then((res) => res.json())
      .then((result) => {
        if (!result.success) {
          const errors = this.state.errors;
          errors.summary = result.message;
          this.setState({
            errors
          });
        } else {
          this.context.router.replace('/confirmation/userId/' + this.state.user_id);
        }
      });
  }

  changeUser(event) {
    const field = event.target.name;
    const request_form = this.state.request_form;
    const errors = this.state.errors
    //console.log(field)
    //console.log(event.target.value);
    const value = event.target.value;

    if(!event.target.validity.valid) {
      errors[field] = event.target.validationMessage;
      this.setState({errors});
      return;
    } else {
      errors[field] = "";
      this.setState({errors});
    }

    if(field === "private_bath") {
      if(value === "true") {
        request_form[field] = true;
      } else {
        request_form[field] = false;
      }

      this.setState({request_form});
      return;
    }

    if(field === "delta_minute"){
      const sec = value * 60;
      request_form[field] = sec;
      this.setState({request_form});
      return;
    }

   
    request_form[field] = event.target.value;

    this.setState({request_form});
  }

  render() {
    return (
      <RequestForm
        onSubmit={this.processForm}
        onChange={this.changeUser}
        errors={this.state.errors}
        request_form={this.state.request_form}
      />  
    );
  }
}

RequestFormPage.contextTypes = {
  router: PropTypes.object.isRequired
}

export default RequestFormPage;
