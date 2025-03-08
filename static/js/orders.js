function showOrderUpdate(order_id, customer_id,purchase_date, total_price,entered_raffle) {
	// set the update form's action to pass the row's order_id
	let orderUpdateForm = document.getElementById("orderUpdateForm");
	orderUpdateForm.action = `/edit_order/${order_id}`;

	// set the form text to the column row values
	document.getElementById("orderIDUpdate").textContent = order_id;
    document.querySelector("select[name='orderCustomerIDUpdate']").value = customer_id;
	document.querySelector("input[name='orderDateUpdate']").value = purchase_date;
	document.querySelector("input[name='orderPriceUpdate']").value = total_price;
	document.querySelector("select[name='orderEnteredRaffleUpdate']").value = entered_raffle;

	// show the form
	orderUpdateForm.style.display = "block";
}

function showOrderDelete(order_id) {
	// set the delete form's action to pass the row's order_id
	let orderDeleteForm = document.getElementById("orderDeleteForm");
	orderDeleteForm.action = `/delete_order/${order_id}`;

	// set the form text to the order_id and customer_id
	document.getElementById("orderIDDelete").textContent = order_id;

	// show the form
	orderDeleteForm.style.display = "block";
}