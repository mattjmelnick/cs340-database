function showRaffleUpdate(raffle) {
    // set the update form's action to pass the row's raffle_id
	let raffleUpdateForm = document.getElementById("raffleUpdateForm");
	raffleUpdateForm.action = `/edit_raffle/${raffle.raffle_id}`;

    // set the form text to the column row values
	document.getElementById("raffleIDUpdate").textContent = raffle.raffle_id;
	document.querySelector("select[name='raffleSneakerIDUpdate']").value = raffle.sneaker_id;
	document.querySelector("textarea[name='raffleDescriptionUpdate']").value = raffle.raffle_description;
	document.querySelector("input[name='raffleEntryCostUpdate']").value = raffle.entry_cost;

    // show the form
	raffleUpdateForm.style.display = "block";
}

function showRaffleDelete(raffle_id) {
	// set the delete form's action to pass the row's raffle_id
	let raffleDeleteForm = document.getElementById("raffleDeleteForm");
	raffleDeleteForm.action = `/delete_raffle/${raffle_id}`;

	// set the form text to the raffle_id 
	document.getElementById("raffleIDDelete").textContent = raffle_id;

	// show the form
	raffleDeleteForm.style.display = "block";
}
