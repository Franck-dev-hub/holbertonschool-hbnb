document.addEventListener('DOMContentLoaded', () => {
  // Require auth, redirect to login if not
  const token = requireAuthentication();
  if (!token) return;

  // Populate rating options
  const ratingSelect = document.getElementById("review-rating");
  if (ratingSelect) {
    const placeholder = document.createElement("option");
    placeholder.value = '';
    placeholder.textContent = "Select a rating";
    ratingSelect.appendChild(placeholder);

    const labels = {
      1: "1 - Poor",
      2: "2 - Fair",
      3: "3 - Good",
      4: "4 - Very good",
      5: "5 - Excellent"
    };

    [1, 2, 3, 4, 5].forEach(v => {
      const opt = document.createElement("option");
      opt.value = String(v);
      opt.textContent = labels[v];
      ratingSelect.appendChild(opt);
    });
  }

  // Prefill place id from querystring
  const placeId = new URLSearchParams(window.location.search).get('id');
  if (!placeId) {
    document.getElementById("form-message").textContent = "Missing place id.";
    document.getElementById("form-message").classList.remove("hidden");
    return;
  }

  const reviewForm = document.getElementById("review-form");
  reviewForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const text = document.getElementById("review-text").value.trim();
    const rating = parseInt(document.getElementById("review-rating").value, 10);

    if (!text || !rating) {
      alert("Please provide review text and rating");
      return;
    }

    try {
      const response = await fetch(`${API_BACK}/reviews/`, {
        method: "POST",
        headers: getAuthHeaders(),
        body: JSON.stringify({ text, rating, place_id: placeId })
      });

      if (!response.ok) {
        const err = await response.json();
        alert(`Error: ${err.error || "Could not submit review"}`);
        return;
      }

      // On success, redirect back to place details
      window.location.href = `place.html?id=${encodeURIComponent(placeId)}`;
    } catch (err) {
      console.error(`Error submitting review:\n${err}`);
      alert(`Error submitting review.\n${err}`);
    }
  });
});
