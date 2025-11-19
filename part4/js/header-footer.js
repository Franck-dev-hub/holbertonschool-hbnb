// Logout by deleting cookie
function logout() {
  deleteCookie("access_token");
  updateButtons();
  window.location.href = "index.html";
}

// Update login/logout buttons
function updateButtons() {
  const token = getCookie("access_token");

  if (token) {
    document.getElementById("login-button")?.classList.add("hidden");
    document.getElementById("logout-button")?.classList.remove("hidden");
  } else {
    document.getElementById("login-button")?.classList.remove("hidden");
    document.getElementById("logout-button")?.classList.add("hidden");
  }
}

// Load header and footer
document.addEventListener('DOMContentLoaded', () => {
  // Load header
  fetch("header.html")
    .then(res => res.text())
    .then(html => {
      document.getElementById("header").innerHTML = html;
      updateButtons();
      // Logout listener
      const logoutBtn = document.getElementById("logout-button");
      if (logoutBtn) logoutBtn.addEventListener("click", logout);
    })
    .catch(err => console.error("Error loading header:", err));

  // Load footer
  fetch("footer.html")
    .then(res => res.text())
    .then(html => document.getElementById("footer").innerHTML = html)
    .catch(err => console.error("Error loading footer:", err));
});
