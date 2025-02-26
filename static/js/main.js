function cancelForm(formName) {
		document.querySelector(formName).reset();
		document.querySelector(formName).style.display = "none";
}

function showAddForm(formName) {
	document.querySelector(formName).style.display = "block";
}

function showCustomerUpdate(id, name, email, phone) {
	let customerUpdateForm = document.getElementById("customerUpdateForm");
	customerUpdateForm.action = `/edit_customer/${id}`;

	document.getElementById("customerIDUpdate").textContent = id;
	document.querySelector("input[name='customerNameUpdate']").value = name;
	document.querySelector("input[name='customerEmailUpdate']").value = email;
	document.querySelector("input[name='customerPhoneUpdate']").value = phone;

	customerUpdateForm.style.display = "block";
}

function showCustomerDelete(id, name) {
	let customerDeleteForm = document.getElementById("customerDeleteForm");
	customerDeleteForm.action = `/delete_customer/${id}`;

	document.getElementById("customerIDDelete").textContent = id;
	document.getElementById("customerNameDelete").textContent = name;

	customerDeleteForm.style.display = "block";
}

function showROUpdate(id, order_id, raffle_id, order_ids, raffle_ids) {
	let roUpdateForm = document.getElementById("raffleOrderUpdateForm");
	roUpdateForm.action = `/edit_raffle_order/${id}`;

	document.getElementById("roIDUpdate").textContent = id;

	// create dropdown list for order ids
	let roOrderIDDropdown = document.getElementById("roOrderIDUpdate");
	// clear the options to prevent redundancy
	roOrderIDDropdown.options.length = 0;

	// iterate through the order_ids array of objects and create options
	order_ids.forEach(order => {
		let orderOption = document.createElement("option");
		orderOption.value = order.order_id.toString();
		orderOption.text = order.order_id.toString();
		// pre-select the row's raffle_id
		if (order.order_id.toString() === order_id) {
			orderOption.selected = true;
		}
		roOrderIDDropdown.appendChild(orderOption);
	});

	// create dropdown list for raffle ids
	let roRaffleIDDropdown = document.getElementById("roRaffleIDUpdate");
	// clear the options to prevent redundancy
	roRaffleIDDropdown.options.length = 0;

	const nullOption = document.createElement("option");
	nullOption.value = "0";
	nullOption.text = "NULL";

	roRaffleIDDropdown.appendChild(nullOption);

	// iterate through the raffle_ids array of objects and create options
	raffle_ids.forEach(raffle => {
		let raffleOption = document.createElement("option");
		raffleOption.value = raffle.raffle_id.toString(); 
		raffleOption.text = raffle.raffle_id.toString();
		// pre-select the row's raffle_id
		if (raffle.raffle_id.toString() === raffle_id) {
			raffleOption.selected = true;
		}
		roRaffleIDDropdown.appendChild(raffleOption);
	});

	roUpdateForm.style.display = "block";
}

function showRODelete(id) {
	let roDeleteForm = document.getElementById("raffleOrderDeleteForm");
	roDeleteForm.action = `/delete_raffle_order/${id}`;

	document.getElementById("roIDDelete").textContent = id;

	roDeleteForm.style.display = "block";
}