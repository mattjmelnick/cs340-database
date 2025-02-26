function cancelForm(formName) {
	// use a switch statement to select each form to hide based on the input parameter
	// this prevents redundant functions being created
	switch(formName) {
		case "customerAddForm":
			document.querySelector("#customerAddForm").reset();
			document.querySelector("#customerAddForm").style.display = "none";
			break;
		case "customerUpdateForm":
			document.querySelector("#customerUpdateForm").reset();
			document.querySelector("#customerUpdateForm").style.display = "none";
			break;
		case "customerDeleteForm":
			document.querySelector("#customerDeleteForm").reset();
			document.querySelector("#customerDeleteForm").style.display = "none";
			break;
	}
}

function showCustomerAdd() {
	document.querySelector("#customerAddForm").style.display = "block";
}

function showCustomerUpdate(id, name, email, phone) {
	let updateForm = document.getElementById("customerUpdateForm");
	updateForm.action = `/edit_customer/${id}`;

	document.getElementById("customerIDUpdate").textContent = id;
	document.querySelector("input[name='customerNameUpdate']").value = name;
	document.querySelector("input[name='customerEmailUpdate']").value = email;
	document.querySelector("input[name='customerPhoneUpdate']").value = phone;

	document.querySelector("#customerUpdateForm").style.display = "block";
}

function showCustomerDelete(id, name) {
	let deleteForm = document.getElementById("customerDeleteForm");
	deleteForm.action = `/delete_customer/${id}`;

	document.getElementById("customerIDDelete").textContent = id;
	document.getElementById("customerNameDelete").textContent = name;

	document.querySelector("#customerDeleteForm").style.display = "block";
}
