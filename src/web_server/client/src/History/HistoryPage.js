import React from 'react';
import PropTypes from 'prop-types';

class HistoryPage extends React.Component {
  constructor(props, context) {
    super(props, context);
  }

  render() {
    return (
        <div>
          <p>HistoryPage</p>
        </div>
    );
  }
}

HistoryPage.contextTypes = {
  router: PropTypes.object.isRequired
};

export default HistoryPage;

