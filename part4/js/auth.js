function setCookie(name, value) {
  document.cookie = `${name}=${value}; path=/; SameSite=Lax`;
}

function getCookie(name) {
  const cookies = document.cookie.split("; ");
  for (const c of cookies) {
    const [key, value] = c.split("=");
    if (key === name) return value;
  }
  return null;
}

function deleteCookie(name) {
  document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
}

// Check if user is connected
function isAuthenticated() {
    return getCookie("access_token") !== null;
}

// Send to login.html if not logged
function requireAuthentication() {
    const token = getCookie("access_token");
    if (!token) {
        window.location.href = "login.html";
        return null;
    }
    return token;
}

// Add token to auth
function getAuthHeaders() {
    const headers = { "Content-Type": "application/json" };
    const token = getCookie("access_token");
    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }
    return headers;
}
