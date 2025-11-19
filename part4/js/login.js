const API_URL = 'http://127.0.0.1:5000/api/v1/';

// Cookies
function setCookie(name, value, daysToLive) {
  const date = new Date();
  date.setTime(date.getTime() + daysToLive * 24 * 60 * 60 * 1000);
  let expires = "expires=" + date.toUTCString();
  document.cookie = `${name}=${value}; ${expires}; path=/`;
}

function getCookie(name) {
  const cDecoded = decodeURIComponent(document.cookie);
  const cArray = cDecoded.split("; ");
  let result;
  cArray.forEach(element => {
    if (element.indexOf(name) === 0) {
      result = element.substring(name.length + 1);
    }
  });
  return result;
}

function deleteCookie(name) {
  setCookie(name, "", -1);
}

// Global connexion state
let isLoggedIn = false;

// Check auth at loading
async function checkAuthentication() {
  const token = getCookie('token');
  isLoggedIn = !!token;
  // Toggle buttons
  toggleAuthUI();
  return token;
}

// Toggle login logout display
function toggleAuthUI() {
  const loginButton = document.getElementById("login-button");
  const logoutButton = document.getElementById("logout-button");

  if (loginButton && logoutButton) {
    if (isLoggedIn) {
      loginButton.classList.add("hidden");
      logoutButton.classList.remove("hidden");
    } else {
      loginButton.classList.remove("hidden");
      logoutButton.classList.add("hidden");
    }
  }
}

// Create an account
async function createAccount(first_name, last_name, email, password) {
  try {
    const response = await fetch(`${API_URL}users/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ first_name, last_name, email, password })
    });

    if (response.ok) {
      loginUser(email, password);
    } else {
      alert('Account creation failed: ' + response.statusText);
    }
  } catch (error) {
    console.error('Error creating account:', error);
  }
}

// Connect user
async function loginUser(email, password) {
  try {
      const response = await fetch(`${API_URL}auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });

    if (response.ok) {
      const data = await response.json();

      // Store token
      setCookie("token", data.access_token, 365);

      // Update state
      isLoggedIn = true;
      toggleAuthUI();

      // Redirect after login
      window.location.href = "index.html";
    } else {
      alert('Login failed: ' + response.statusText);
    }
  } catch (error) {
    console.error('Login error:', error);
    alert('Login error: ' + error.message);
  }
}

// Logout user
function logout() {
  deleteCookie('token');
  isLoggedIn = false;
  toggleAuthUI();
  window.location.href = 'index.html';
}

// Init connexion to the DOM
document.addEventListener('DOMContentLoaded', () => {
  // Check auth
  checkAuthentication();

  // Manage form submission
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      loginUser(email, password);
    });
  }

  // Manage logout button
  const logoutButton = document.getElementById('logout-button');
  if (logoutButton) {
    logoutButton.addEventListener('click', logout);
  }
});
