function showROUpdate(id, order_id, raffle_id, order_ids, raffle_ids) {
	// set the update form's action to pass the row's raffle_order_id
	let roUpdateForm = document.getElementById("raffleOrderUpdateForm");
	roUpdateForm.action = `/edit_raffle_order/${id}`;

	// set the form text to the raffle_order_id
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

	// create a null value option
	const nullOption = document.createElement("option");
	nullOption.value = "0";
	nullOption.text = "NULL";

	// append the null option to the dropdown list
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

	// show the form
	roUpdateForm.style.display = "block";
}

function showRODelete(id) {
	// set the delete form's action to pass the row's raffle_order_id
	let roDeleteForm = document.getElementById("raffleOrderDeleteForm");
	roDeleteForm.action = `/delete_raffle_order/${id}`;

	// set the form text to the raffle_order_id
	document.getElementById("roIDDelete").textContent = id;

	// show the form
	roDeleteForm.style.display = "block";
}
