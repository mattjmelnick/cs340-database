function showROUpdate(id, order_id, raffle_id) {
	// set the update form's action to pass the row's raffle_order_id
	let roUpdateForm = document.getElementById("raffleOrderUpdateForm");
	roUpdateForm.action = `/edit_raffle_order/${id}`;

    // set the form text to the column row values
	document.getElementById("roIDUpdate").textContent = id;
    document.querySelector("select[name='roOrderIDUpdate']").value = order_id;
    raffle_id === "None" ? document.querySelector("select[name='roRaffleIDUpdate']").value = 0 :
	                        document.querySelector("select[name='roRaffleIDUpdate']").value = raffle_id;

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
