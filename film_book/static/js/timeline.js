function addComment(buttonElement) {

    var formElement = buttonElement.parentElement;
    var addNewCommentElement = formElement.parentElement;
    var commentsElement = addNewCommentElement.parentElement

    var newComment = document.createElement("div")
    newComment.setAttribute("class", "comment")
    
    var newCommentUser = document.createElement("div")
    newCommentUser.setAttribute("class", "commenter-username")
    newCommentUser.innerText = "Username"
    
    var newCommentContent = document.createElement("div")
    newCommentContent.setAttribute("class", "comment-content")
    newCommentContent.innerText = formElement.children[0].value
    
    var newCommentDate = document.createElement("span")
    newCommentDate.setAttribute("class", "comment-date")
    var date = new Date()
    newCommentDate.innerText = date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear() + "  " + date.getHours() + ":" + date.getMinutes()
    
    newComment.appendChild(newCommentUser)
    newComment.appendChild(newCommentContent)
    newComment.appendChild(newCommentDate)

    commentsElement.insertBefore(newComment, addNewCommentElement)

    var breakLine = document.createElement("br")
    commentsElement.insertBefore(breakLine, addNewCommentElement)

    return false;
}

function showMovieDetails(movieImageElement) {
	var detailBoxElement = movieImageElement.nextElementSibling;
	detailBoxElement.style.display = "inline-block";
}

function moveMovieDetails(event, movieImageElement) {
	var detailBoxElement = movieImageElement.nextElementSibling;
	detailBoxElement.style.top = event.clientY;
	detailBoxElement.style.left = event.clientX;
}

function hideMovieDetails(movieImageElement) {
	var detailBoxElement = movieImageElement.nextElementSibling;
	detailBoxElement.style.display = "none";
}