import React from 'react';
import PropTypes from 'prop-types';
import House from '../House/House';

class HistoryPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      user_id: context.router.params.userId,
      listings: null
    };
  }

  componentDidMount() {
    this.loadHistory();
  }

  loadHistory() {
    let url = 'http://localhost:3001/history/userId/' + this.state.user_id;

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
    const house_list = this.state.listings.map(function(listing) {
      return (
          <a className='list-group-item' href="#">
            <House listing={listing} />
          </a>
      );
    });

    return (
        <div className='container-fluid'>
          <div className='list-group'>
            {house_list}
          </div>
        </div>
    )
  }

  render() {
    
        if (this.state.listings) {
          return (
            <div>
              {this.renderListings()}
            </div>    
          );
        } else {
          return(
            <div>
              <div id='msg-app-loading'>
                Loading...
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

