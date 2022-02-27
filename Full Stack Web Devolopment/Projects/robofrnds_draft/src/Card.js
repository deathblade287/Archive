import React from 'react';

const card=() => {
	return (
		// <h1>RoboFriends</h1>
		<div className='bg-light-green dib br3 pa3 ma2 grow bw2 shadow-5'> 
		    <img alt='robots' src='https://robohash.org/test?200x200'/>
		    <div>
		        <h2>{this.props.name}</h2>
		        <p>{this.props.username}</p>
		    </div>
		</div>
		);

}

export default card;