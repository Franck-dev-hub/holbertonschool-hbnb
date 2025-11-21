document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("account-form");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const first_name = document.getElementById("first-name").value;
    const last_name = document.getElementById("last-name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
      const response = await fetch(`${API_BACK}/users/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          first_name,
          last_name,
          email,
          password,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || "Registration failed");
      }

      // Success
      alert("Account created successfully!");
      window.location.href = "login.html";

    } catch (error) {
      alert(error.message);
    }
  });
});
