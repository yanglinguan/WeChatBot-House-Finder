import './RequestFormPage.css'
import React from 'react'
import RequestForm from './RequestForm';

class RequestFormPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      error: {},
      message: '',
      user_id: context.router.params.userId,
      request_form: {
        areas: [],
        city: '',
        departure_to_work: 0,
        max_bedroom: 0,
        min_bedroom: 0,
        max_price: 0,
        min_price: 0,
        time_to_work: 0,
        time_to_work_delta: 0,
        travel_mode: '',
        work_addr: ''
      }
    };

    this.processForm = this.processForm.bind(this);
    this.changeUser = this.changeUser.bind(this);
  }

  processForm(event) {
    event.preventDefault();
    
    const user_id = this.state.user_id;

    let url = 'http://localhost:3000/requestForm/userId/' + this.state.user_id;

    let request = new Request(encodeURI(url), {
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        areas:this.state.request_form.areas,
        city: this.state.request_form.city,
        departure_to_work: this.state.request_form.departue_to_work,
        max_bedroom: this.state.request_form.max_bedroom,
        min_bedroom: this.state.request_form.min_bedroom,
        max_price: this.state.request_form.max_price,
        min_price: this.state.request_form.min_price,
        time_to_work: this.state.request_form.time_to_work,
        time_to_work_delta: this.state.request_form.time_to_work_delta,
        travel_mode: this.state.request_form.travel_mode,
        work_addr: this.state.request_form.work_addr
      })
      cache: false
    });

    fetch(request)
      .then((res) => res.json())
      .then((result) => {
        if (!result.success) {
          const errors = this.state.errors;
          errors.summary = result.message;
          this.setState({
            errors
          });
        } else {
          this.context.router.replace('/confirmation');
        }
      });
  }

  changeUser(event) {
    const field = event.target.name;
    const request_form = this.state.request_form;
    if (field === 'max_bedroom' || 
        field === 'min_bedroom' || 
        field === 'max_price' || 
        field === 'min_price' ) {

      request_form[field] = parseInt(event.target.value);
      if (isNaN(request_form[field])) {
        const errors = this.state.errors;
        errors[field] = field + ": provide integer number for this field";
        this.setState({errors});
      } else {
        const errors = this.state.errors;
        errors.password = '';
        this.setState({errors});
      } 
    }
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
