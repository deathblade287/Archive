import React from 'react';

const Scroll = (props) => {
  return (
    // , border: '5px solid black'
    <div style={{ overflow: 'scroll', height: '800px'}}>
      {props.children}
    </div>
  );
};

export default Scroll;