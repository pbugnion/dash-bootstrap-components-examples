import React from 'react';

import {Badge} from 'dash-bootstrap-components';

const MyBadge = () => {
  return <Badge>Hello dbc!</Badge>
}

MyBadge.propTypes = {
  /**
   * The ID of this component, used to identify dash components
   * in callbacks. The ID needs to be unique across all of the
   * components in an app.
   */
  id: PropTypes.string,

  /**
   * Badge color, options: primary, secondary, success, info, warning, danger,
   * link. Default: secondary.
   */
  color: PropTypes.string,
}

export default MyBadge;
