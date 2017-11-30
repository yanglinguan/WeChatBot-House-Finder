import React from 'react';
import PropTypes from 'prop-types';
import House from '../House/House';

import $ from 'jquery'

class HistoryPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      user_id: context.router.params.userId,
      listings: null
    };
  }

  componentDidMount() {
    //let x = $('.collapsible');
   // x.collapsible;
    //    this.collapsible.collapsible();
    this.loadHistory();
    //$(document).ready(function(){
   // $('.collapsible').collapsible();
   // });
  
  }



 
  loadHistory() {
    let url = 'http://house.yanglinguan.me/history/userId/' + this.state.user_id;

    let request = new Request(encodeURI(url), {
      method: 'GET',
      cache: false
    });

    fetch(request)
      .then((res) => res.json())
      .then((listings) => {
        if(!listings || listings.length === 0 ) {
          return;
        }

        this.setState({
          listings: this.state.listings? this.state.listings.concat(listings) : listings
        });
      });
  }

  renderListings() {

    const house_list = Object.keys(this.state.listings).map((key) => {
      return (
          <House key={key} listing={this.state.listings[key]} request_id={key} user_id={this.state.user_id}/>
      );
    });

    return (
        <ul className='collection'>
          {house_list}
        </ul>
    )
  }

  render() {
    
        if (this.state.listings) {
          return (
            <div className="container">
              {this.renderListings()}
            </div>    
          );
        } else {
          return(
            <div className="preloader-wrapper active">
              <div className="spinner-layer spinner-red-only">
                <div className="circle-clipper left">
                  <div className="circle"></div>
                </div>
                <div className="gap-patch">
                  <div className="circle"></div>
                </div>
                <div className="circle-clipper right">
                  <div className="circle"></div>
                </div>
              </div>
            </div>
          );
        }
  
  }
}

HistoryPage.contextTypes = {
  router: PropTypes.object.isRequired
};

export default HistoryPage;

