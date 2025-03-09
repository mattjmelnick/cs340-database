function showSOUpdate(sneaker_order_id, order_id, sneaker_id, quantity) {
    // set the update form's action to pass the row's sneaker_order_id
	let sneakerOrderUpdateForm = document.getElementById("sneakerOrderUpdateForm");
	sneakerOrderUpdateForm.action = `/edit_sneaker_order/${sneaker_order_id}`;

    // set the form text to the column row values
	document.getElementById("soIDUpdate").textContent = sneaker_order_id;
    document.querySelector("select[name='soOrderIDUpdate']").value = order_id;
    sneaker_id === "None" ? document.querySelector("select[name='soSneakerIDUpdate']").value = 0 :
	                        document.querySelector("select[name='soSneakerIDUpdate']").value = sneaker_id;
	document.querySelector("input[name='soQuantityUpdate']").value = quantity;

    // show the form
    sneakerOrderUpdateForm.style.display = "block";
}

function showSODelete(sneaker_order_id) {
	// set the delete form's action to pass the row's sneaker_order_id 
	let sneakerOrderDeleteForm = document.getElementById("sneakerOrderDeleteForm");
	sneakerOrderDeleteForm.action = `/delete_sneaker_order/${sneaker_order_id}`;

	// set the form text to the sneaker_order_id 
	document.getElementById("soIDDelete").textContent = sneaker_order_id;

	// show the form
	sneakerOrderDeleteForm.style.display = "block";
}
