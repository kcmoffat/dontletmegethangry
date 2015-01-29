document.getElementById("sendNotification").addEventListener("click", function() {
	console.debug("clicked send button");
	var senderName = document.getElementById("senderName").value;
	console.debug("senderName: " + senderName);
	var recipientEmail = document.getElementById("recipientEmail").value;
	console.debug("recipientEmail: " + recipientEmail);
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange=function() {
		// deal with result
		console.debug("onreadystatechange occurred");
		console.debug("readyState: " + xmlhttp.readyState);
		console.debug("status: " + xmlhttp.status);
		updateProgressBar(xmlhttp.readyState / 4 * 100);
		if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
			console.debug("SENT!");
			dismissModal("SENT!");
		} else if (xmlhttp.readyState == 4) {
			console.debug("failure");
			dismissModal("Error :(  Try again later.");
		}
	}
	var url = "http://dontletmegethangry.com/notifications";
	xmlhttp.open("POST", url, true);
	xmlhttp.setRequestHeader("Content-type", "application/json");
	var parameters = JSON.stringify({
		"sender_name": senderName,
		"recipient_email": recipientEmail
	});
	xmlhttp.send(parameters);
	showModal();
});

function updateProgressBar(progress) {
	console.debug("updating progress bar with percentage " + progress);
	var progressBar = document.getElementById("sendProgressBar");
	console.debug("Current aria-valuenow: " + progressBar.getAttribute("aria-valuenow"));
	console.debug("Current width: " + progressBar.width);
	progressBar.setAttribute("aria-valuenow", "" + progress);
	progressBar.style.width = progress + "%";
}

function showModal() {
	console.debug("showing modal");
	var modal = document.getElementById("modalDiv");
	modal.classList.remove("hide");
	var progressBar = document.getElementById("sendProgressBar");
	progressBar.classList.add("active");
}

function dismissModal(serverResponse) {
	console.debug("dismissing modal");
	var progressBar = document.getElementById("sendProgressBar");
	progressBar.classList.remove("active");
	setTimeout(function() {
		var progressBarLabel = document.getElementById("progressBarLabel");
		progressBarLabel.innerHTML = serverResponse;
		setTimeout(function() {
			var modal = document.getElementById("modalDiv");
			modal.classList.add("hide");
			progressBarLabel.innerHTML = "";
			progressBar.setAttribute("aria-valuenow", "" + 10);
			progressBar.style.width = 10 + "%";
		}, 1000);
	}, 1000);
}