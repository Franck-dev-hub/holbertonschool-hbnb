document.addEventListener('DOMContentLoaded', () => {
  // Display header
  fetch("header.html")
    .then(response => response.text())
    .then(data => {
      document.getElementById("header").innerHTML = data;
    })
    .catch(err => console.error("Error loading header :", err));

  // Display footer
  fetch("footer.html")
    .then(response => response.text())
    .then(data => {
      document.getElementById("footer").innerHTML = data;
    })
    .catch(err => console.error("Error loading footer :", err));

});

function toggleAuthUI() {
  if(isLoggedIn) {
    document.getElementById("login-button").classList.add("hidden");
    document.getElementById("logout-button").classList.remove("hidden");
  } else {
    document.getElementById("login-button").classList.remove("hidden");
    document.getElementById("logout-button").classList.add("hidden");
  }
}
