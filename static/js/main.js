function cancelForm(formName) {
		document.querySelector(formName).reset();
		document.querySelector(formName).style.display = "none";
}

function showAddForm(formName) {
	document.querySelector(formName).style.display = "block";
}
