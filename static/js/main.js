function cancelForm(formName) {
		document.querySelector(formName).reset();
		document.querySelector(formName).style.display = "none";
}

function showAddForm(formName) {
	document.querySelector(formName).style.display = "block";
}

function hideAddForm() {
	const addForm = document.querySelector(".addForm");
	let requiredFields = addForm.querySelectorAll("[required]");
	requiredFields.forEach((field) => {
		field.removeAttribute("required");
	});
	addForm.style.display = "none";
}

function showUpdateForm() {
    const updateForm = document.querySelector(".updateForm");
    updateForm.style.display = "block";
}

function hideUpdateForm() {
    const updateForm = document.querySelector(".updateForm");
	let requiredFields = updateForm.querySelectorAll("[required]");
	requiredFields.forEach((field) => {
		field.removeAttribute("required");
	});
	updateForm.style.display = "none";
}

function showDeleteForm() {
    const deleteForm = document.querySelector(".deleteForm");
    deleteForm.style.display = "block";
}

function hideDeleteForm() {
    const deleteForm = document.querySelector(".deleteForm");
	let requiredFields = deleteForm.querySelectorAll("[required]");
	requiredFields.forEach((field) => {
		field.removeAttribute("required");
	});
	deleteForm.style.display = "none";
}