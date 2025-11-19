document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");

  if (loginForm) {
    loginForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      loginUser(email, password);
    });
  }
});

async function loginUser(email, password) {
  try {
    const response = await fetch("http://localhost:5000/api/v1/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    if (!response.ok) {
      alert("Login failed");
      return;
    }

    const data = await response.json();

    setCookie("access_token", data.access_token);
    updateButtons();
    window.location.href = "index.html";

  } catch (err) {
    console.error("Login error:", err);
  }
}
