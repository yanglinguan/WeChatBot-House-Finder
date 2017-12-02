import React from 'react';
import PropTypes from 'prop-types'
class DetailPage extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      user_id: context.router.params.userId,
      request_id: context.router.params.requestId,
      host: props.route.serverHost
    };
  }

  componentDidMount() {
    this.loadDetail();
  }

  loadDetail() {
    let url = 'http://' + this.state.host + '/requestDetail/userId/' 
      + this.state.user_id + "/requestId/" + this.state.request_id;

    let request = new Request(encodeURI(url), {
      method: 'GET',
      cache: false
    });

    fetch(request)
      .then((res) => res.json())
      .then((listing) => {
        if(!listing) {
          return;
        }

        this.setState({
          listing: listing
        });
      });
  }

  renderBody() {
    const body = Object.keys(this.state.listing).map((key) => {
      return (
        <p key={key}>
          {key}: {this.state.listing[key]}
        </p>
      );
    });

    return body;
  }

  deleteRequest() {}

  editRequest() {}

  render() {
    if(this.state.listing) {
      return (
        <div className="container">
          <div className="row">
            <div className="col s12 m5">
              {this.renderBody()}
            </div>
          </div>
          <div className="row">
            <div className="waves-effect waves-light btn indigo lighthen-1" onClick={this.deleteRequest()}>Delete</div>
            <div className="waves-effect waves-light btn indigo lighthen-1" onClick={this.editRequest()}>Edit</div>
          </div>
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

DetailPage.contextTypes = {
  router: PropTypes.object.isRequired
}

export default DetailPage;
