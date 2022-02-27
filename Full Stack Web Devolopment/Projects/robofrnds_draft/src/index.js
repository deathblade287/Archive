import React from 'react';
import ReactDOM from 'react-dom';
import 'tachyons';
import Card from './Card';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { robots } from './robots.js';

console.log(robots)
function identities(robots){
  return <Card id={robots.id} name={robots.name} username={robots.username}/>
}
  
ReactDOM.render(
  <React.StrictMode>
    <div>
      {robots.map(identities)}
    </div>
  </React.StrictMode>,
  document.getElementById('root')
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
