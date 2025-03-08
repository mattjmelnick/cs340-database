function showDrawingUpdate(drawing_id, raffle_id, draw_date, draw_day) {
	console.log(drawing_id, raffle_id, draw_date, draw_day)
	// set the update form's action to pass the row's drawing_id
	let drawingUpdateForm = document.getElementById("drawingUpdateForm");
	drawingUpdateForm.action = `/edit_drawing/${drawing_id}`;

	// set the form text to the column row values
	document.getElementById("drawingIDUpdate").textContent = drawing_id;
	document.querySelector("select[name='drawingRaffleIDUpdate']").value = raffle_id;
	document.querySelector("input[name='drawingDateUpdate']").value = draw_date;
	document.querySelector("select[name='drawingDayUpdate']").value = draw_day;
   
	// show the form
	drawingUpdateForm.style.display = "block";
}

function showDrawingDelete(drawing_id) {
	// set the delete form's action to pass the row's drawing_id
	console.log(drawing_id)
	let drawingDeleteForm = document.getElementById("drawingDeleteForm");
	drawingDeleteForm.action = `/delete_drawing/${drawing_id}`;

	// set the form text to the drawing_id 
	document.getElementById("drawingIDDelete").textContent = drawing_id;

	// show the form
	drawingDeleteForm.style.display = "block";
}
