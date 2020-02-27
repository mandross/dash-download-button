import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'ramda';

function download(target){
    var tmp_div = document.body.appendChild(
        document.createElement('a')
    );
    tmp_div.download = 'export.html';
    tmp_div.href = '<html>\n<head><meta charset="utf-8" /></head>\n<body>\n' +
                   document.getElementById(target).innerHTML +
                   '\n</body>\n</html>'
    tmp_div.click();
    tmp_div.remove();
}

const DownloadButton = (props) => {
    return (
       <button
            onClick={() => download(props.target)}
            {...omit(['n_clicks', 'n_clicks_timestamp', 'loading_state', 'setProps'], props)}
         >
            {props.children}
        </button>
    );
};

DownloadButton.defaultProps = {};

DownloadButton.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The children of this component
     */
    'children': PropTypes.node,

    /**
     * Often used with CSS to style elements with common properties.
     */
    'className': PropTypes.string,

    /**
     * Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
     */
    'hidden': PropTypes.string,

    /**
     * Defines a default value which will be displayed in the element on page load.
     */
    'target': PropTypes.string
};

export default DownloadButton;
