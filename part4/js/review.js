document.addEventListener("DOMContentLoaded", () => {
  const token = requireAuthentication();
  if (!token) return;

  const userId = getUserIdFromToken() {
    if (!userId) {
      alert("Unable to fetch user ID");
      return;
    }
  }

  const placeId = new URLSearchParams(window.location.search).get("id");
  if (!placeId) return;

  const reviewForm = document.getElementById("review-form");
  if (!reviewForm) return;

  reviewForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const title = reviewForm.querySelector("#review-title").value.trim() || "No title";
    const text = reviewForm.querySelector("#review-text").value.trim();
    const rating = parseInt(reviewForm.querySelector("#review-rating").value, 10);

    try {
      const response = await fetch(`${API_BACK}/reviews/`, {
        method: "POST",
        headers: getAuthHeaders(),
        body: JSON.stringify({ title, text, rating, place_id: placeId , user_id: userID})
      });

      if (!response.ok) {
        const error = await response.json();
        alert(`Error: ${error.error || "Failed to submit review"}`);
        return;
      }

      reviewForm.reset();
      loadReviews(placeId);
      alert("Review submitted successfully!");
    } catch (err) {
      alert(`Error submitting review:\n${err}`);
    }
  });
});

function getUserIdFromToken() {
  try {
    const payload = token.split('.')[1];
    const decoded = JSON.parse(atob(payload));
    return decoded.user_id || decoded.sub;
  } catch (err) {
    console.error(`Error decoding token: ${err}`);
    return null;
  }
}
