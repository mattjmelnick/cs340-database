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

// get the phone inputs
const phoneInputs = document.querySelectorAll(".phoneInput");
// iterate over the inputs to add the event listener
phoneInputs.forEach(phoneInput => {
    phoneInput.addEventListener('input', (num) => {
        // prevent non-numerical characters
        let number = num.target.value.replace(/\D/g, '');
        let enteredValue = '';
        
        // add hyphen after third and sixth numbers
        if (number.length > 0) {
            enteredValue += number.substring(0, 3);
            if (number.length > 3) {
                enteredValue += '-' + number.substring(3, 6);
                if (number.length > 6) {
                    enteredValue += '-' + number.substring(6, 10);
                }
            }
        }

        num.target.value = enteredValue;
    });
});
