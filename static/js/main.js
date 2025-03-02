function cancelForm(formName) {
		document.querySelector(formName).reset();
		document.querySelector(formName).style.display = "none";
}

function showAddForm(formName) {
	document.querySelector(formName).style.display = "block";
}

function showCustomerUpdate(customer) {
	// set the update form's action to pass the row's customer_id
	let customerUpdateForm = document.getElementById("customerUpdateForm");
	customerUpdateForm.action = `/edit_customer/${customer.customer_id}`;

	// set the form text to the column row values
	document.getElementById("customerIDUpdate").textContent = customer.customer_id;
	document.querySelector("input[name='customerNameUpdate']").value = customer.name;
	document.querySelector("input[name='customerEmailUpdate']").value = customer.email;
	document.querySelector("input[name='customerPhoneUpdate']").value = customer.phone_number;

	// show the form
	customerUpdateForm.style.display = "block";
}

function showCustomerDelete(customer) {
	// set the delete form's action to pass the row's customer_id
	let customerDeleteForm = document.getElementById("customerDeleteForm");
	customerDeleteForm.action = `/delete_customer/${customer.customer_id}`;

	// set the form text to the customer_id and name
	document.getElementById("customerIDDelete").textContent = customer.customer_id;
	document.getElementById("customerNameDelete").textContent = customer.name;

	// show the form
	customerDeleteForm.style.display = "block";
}

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

function showSneakerUpdate(sneaker) {
    // set the delete form's action to pass the row's sneaker_id
    let sneakerUpdateForm = document.getElementById("sneakerUpdateForm");
    sneakerUpdateForm.action = `/edit_sneaker/${sneaker.sneaker_id}`;

    // set the form's input values to the row's values
    document.getElementById("sneakerIDUpdate").textContent = sneaker.sneaker_id;
	document.querySelector("input[name='sneakerBrandUpdate']").value = sneaker.brand;
	document.querySelector("input[name='sneakerModelUpdate']").value = sneaker.model_name;
	document.querySelector("input[name='sneakerSizeUpdate']").value = sneaker.size;
	document.querySelector("input[name='sneakerColorwayUpdate']").value = sneaker.colorway;
	document.querySelector("input[name='sneakerPriceUpdate']").value = sneaker.price;
	document.querySelector("input[name='sneakerStockUpdate']").value = sneaker.stock_count;
    console.log(document.querySelector("input[name='sneakerModelUpdate']").value);

    // show the form
    sneakerUpdateForm.style.display = "block";
}

function showSneakerDelete(sneaker) {
    // set the delete form's action to pass the row's sneaker_id
    let sneakerDeleteForm = document.getElementById("sneakerDeleteForm");
    sneakerDeleteForm.action = `/delete_sneaker/${sneaker.sneaker_id}`;

    // set the form text to the sneaker_id and model_name
    document.getElementById("sneakerIDDelete").textContent = sneaker.sneaker_id;
    document.getElementById("sneakerModelDelete").textContent = sneaker.model_name;
    
    // show the form
    sneakerDeleteForm.style.display = "block";
}
