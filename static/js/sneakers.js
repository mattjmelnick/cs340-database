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
