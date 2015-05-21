function askForComment(event, rate) {
	var askForCommentElement = document.getElementById("askForComment");
	var commentRatingElement = document.getElementById("comment-rating");
	commentRatingElement.innerText = rate + " stars";
	askForCommentElement.style.top = event.clientY;
	askForCommentElement.style.left = event.clientX;
	askForCommentElement.style.display = "block";
}

function hideAskForComment() {
	var askForCommentElement = document.getElementById("askForComment");
	askForCommentElement.style.display = "none";
}