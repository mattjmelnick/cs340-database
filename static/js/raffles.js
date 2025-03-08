function showRaffleUpdate(raffle_id, sneaker_id, raffle_description, entry_cost) {
    console.log(raffle_id, sneaker_id, raffle_description, entry_cost)
    // set the update form's action to pass the row's raffle_id
	let raffleUpdateForm = document.getElementById("raffleUpdateForm");
	raffleUpdateForm.action = `/edit_raffle/${raffle_id}`;

    	// set the form text to the column row values
	document.getElementById("raffleIDUpdate").textContent = raffle_id;
	document.querySelector("select[name='raffleSneakerIDUpdate']").value = sneaker_id;
	document.querySelector("textarea[name='raffleDescriptionUpdate']").value = raffle_description;
	document.querySelector("input[name='raffleEntryCostUpdate']").value = entry_cost;

    // show the form
	raffleUpdateForm.style.display = "block";

}

function showRaffleDelete(raffle_id) {

	// set the delete form's action to pass the row's raffle_id
	console.log(raffle_id)
	let raffleDeleteForm = document.getElementById("raffleDeleteForm");
	raffleDeleteForm.action = `/delete_raffle/${raffle_id}`;

	// set the form text to the raffle_id 
	document.getElementById("raffleIDDelete").textContent = raffle_id;

	// show the form
	raffleDeleteForm.style.display = "block";
}
