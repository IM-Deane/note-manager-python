function deleteNote(noteId) {
	fetch("/delete-note", {
		method: "DELETE",
		body: JSON.stringify({ noteId: noteId }),
	}).then((_res) => {
		// Force page reload
		window.location.href = "/";
	});
}

function editNote(noteId) {
	const note = document.getElementById(`editNoteInput${noteId}`);
	fetch("/edit-note", {
		method: "PATCH",
		body: JSON.stringify({ noteId: noteId, updatedText: note.value }),
	}).then((_res) => {
		note.value = "";
		window.location.href = "/";
	});
}
