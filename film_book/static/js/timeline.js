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

function openComment(imageUrl, post_id){
    form = document.querySelector('#commentForm');
    form.style.display = "block";
    form.postId = post_id;
    document.querySelector('#preventDiv').style.display = "block";
}

function closeComment(el){
    form = document.querySelector('#commentForm');
    form.style.display = "none";
    document.querySelector('#preventDiv').style.display = "none";
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(){
	getcoms()
/*	console.log(xhr.response);
	if(xhr.readyState != 4 || xhr.status != 200) 
	    return ;
	if(xhr.readyState === 4){
	    var res = JSON.parse(xhr.responseText);
	    comments = document.querySelector("#post_" + el.parentNode.postId + " .comments");
	    comments.innerHTML += "<div class='comment'><span class='commenter'>" + res.commenter + ": </span> " + res.content + "<span>" + res.pubDate + "</span></div>";
	}*/
    }
    xhr.open('POST', '/addcomment');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', csrf);
    var data = {
	'comment': el.parentNode.querySelector('textarea').value, 
	'postId': el.parentNode.postId,
    };
    xhr.send(JSON.stringify(data));
    console.log(JSON.stringify(data));
}

function cancelComment(){
    form = document.querySelector('#commentForm');
    form.style.display = "none";
    document.querySelector('#preventDiv').style.display = "none";    
}

setInterval(getcoms, 3000);

function getcoms(){
    console.log("getting...");
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(){
	console.log(xhr.responseText);
	if(xhr.readyState != 4 || xhr.status != 200) 
	    return ;
	if(xhr.readyState === 4){
	    var res = JSON.parse(xhr.responseText);
	    for(key in res){
		comments = document.querySelector("#post_" + key + " .comments");
		comments.innerHTML += "<div class='comment'><span class='commenter'>" + res[key]['commenter'] + ": </span> " + res[key]['content'] + "<span>" + res[key]['pubDate'] + "</span></div>";
	    }
	}
    }
    var date = new Date()
    var formattedDate = date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear() + "  " + date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
    xhr.open('GET', '/getcomments/' + formattedDate);
    xhr.send(null);
}
