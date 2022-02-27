
const array = [1, 2, 10, 16];

// Map
const mapArray = array.map(num => num*2);
// Filter
const fileterArray = array.filter(num => num>5);
// Reduce
const reduceArray = array.reduce((acc, num) => {
	return acc + num
}, 0);
