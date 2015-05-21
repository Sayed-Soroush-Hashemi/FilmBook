function showMoviesTab() {
	var moviesTab = document.getElementById("movies-tab");
	var moviesResultTab = document.getElementById("movie-result-tab");
	moviesTab.style.borderBottom = "2px solid WHITE";
	moviesResultTab.style.display = "";
}

function hideMoviesTab() {
	var moviesTab = document.getElementById("movies-tab");
	var moviesResultTab = document.getElementById("movie-result-tab");
	moviesTab.style.borderBottom = "2px solid GREEN";
	moviesResultTab.style.display = "none";
}

function showPeopleTab() {
	var moviesTab = document.getElementById("people-tab");
	var moviesResultTab = document.getElementById("people-result-tab");
	moviesTab.style.borderBottom = "2px solid WHITE";
	moviesResultTab.style.display = "";
}

function hidePeopleTab() {
	var moviesTab = document.getElementById("people-tab");
	var moviesResultTab = document.getElementById("people-result-tab");
	moviesTab.style.borderBottom = "2px solid GREEN";
	moviesResultTab.style.display = "none";
}