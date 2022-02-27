var ut1 = {
	username : "John",
	timeline : "Bored..."
};

var ut2 = {
	username : "Alix",
	timeline : "I Love Coding"
};

var ut3 = {
	username : "Jack",
	timeline : "I am just gr8"
};

var newsfeed = [ut1, ut2, ut3];

// Login...

var database = [
	{
		username: "deathblade287",
		password : "imgr8"
	},
	{
		username: "Aviral",
		password : "Dhingra"
	},
	{
		username: "Hello",
		password : "1234"
	}
];

function isUserValid(username, password) {
	for (var i=0; i<database.length; i++) {
		
		if (database[i].username===username && 
			database[i].password===password) {
				alert("Succesfully Loged In");
				console.log(newsfeed);
				return true;
		}
	}
	alert("Sorry... Wrong Username & Password");
	return false;
}

// function signIn(username, password) {
// }	


var usernamePrompt = prompt("Plase Enter Username : ");
var passwordPrompt = prompt("Please Enter Password : ");

var try1 = isUserValid(usernamePrompt, passwordPrompt);
console.log(try1)



