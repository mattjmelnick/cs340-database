function showCustomerRaffleUpdate(customer_raffle_id, raffle_id, customer_id, won_raffle) {
	// set the update form's action to pass the row's customer_raffle_id
	let customerRaffleUpdateForm = document.getElementById("customerRaffleUpdateForm");
	customerRaffleUpdateForm.action = `/edit_customer_raffles/${customer_raffle_id}`;

	// set the form text to the column row values
	document.getElementById("crIDUpdate").textContent = customer_raffle_id;
	document.querySelector("select[name='crRaffleIDUpdate']").value = raffle_id;
	document.querySelector("select[name='crCustomerIDUpdate']").value = customer_id;
	document.querySelector("select[name='crWonRaffleUpdate']").value = won_raffle;

	// show the form
	customerRaffleUpdateForm.style.display = "block";
}

function showCustomerRaffleDelete(customer_raffle_id) {
	// set the delete form's action to pass the row's customer_raffle_id
	let customerRaffleDeleteForm = document.getElementById("customerRaffleDeleteForm");
	customerRaffleDeleteForm.action = `/delete_customer_raffles/${customer_raffle_id}`;
	
	// set the form text to the customer_raffle_id
	document.getElementById("customerRaffleIDDelete").textContent = customer_raffle_id;
		
	// show the form
	customerRaffleDeleteForm.style.display = "block";
}
