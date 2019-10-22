import React from 'react';
import ReactDOM from 'react-dom';

// import './index.css';
//import 'font-awesome/css/font-awesome.css';

import Timeline from './components/Timeline/Timeline';
import Container from './Container';
import Header from './Header';

export const load = () => {
    console.log('Loading day 4');

    ReactDOM.render(<Timeline />, document.getElementById('demo1'));
    ReactDOM.render(<Container />, document.getElementById('demo2'));
    ReactDOM.render(<Header title="Timeline" />, document.getElementById('headerDemo'));
};

load();