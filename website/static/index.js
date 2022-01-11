function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.reload();
  });
}

function deleteSemesterGrade(sgId) {
  fetch("/delete-sg", {
    method: "POST",
    body: JSON.stringify({ sgId: sgId }),
  }).then((_res) => {
    window.location.reload();
  });
}