var button = document.getElementById("enter");
var input = document.getElementById("userinput");
var ul = document.querySelector("ul");

function inputLength() {
	return input.value.length;
}

function createListElement() {
	var li = document.createElement("li");
	li.appendChild(document.createTextNode(input.value));
	ul.appendChild(li);
	input.value = "";
}

function addItemAfterClick() {
	if (inputLength() > 0) {
		createListElement();
	}
}

function addItemAfterKeypress(event) {
	if (inputLength() > 0 && event.keyCode === 13) {
		createListElement();
	}
}

function doneTask(task) {
	if (task.target.tagName === "LI"){
		task.target.classList.toggle("done");
	}
}

function crossItemAfterClick(element) {
	console.log(typeof(ul))
	console.log(ul)
	console.log()
	console.log(ul[0])
	console.log(typeof(ul[0]))
	doneTask(element)
}

button.addEventListener("click", addItemAfterClick);
input.addEventListener("keypress", addItemAfterKeypress);
ul.addEventListener("click", crossItemAfterClick);