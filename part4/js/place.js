// Fetch place id's from URL
const placeId = new URLSearchParams(window.location.search).get("id");

// Display a templated paragraph
function boldParagraph(parent, label, value) {
  const paragraph = document.createElement("p");
  const labelSpan = document.createElement("span");
  labelSpan.textContent = label;
  labelSpan.style.fontWeight = "bold";
  paragraph.appendChild(labelSpan);
  paragraph.appendChild(document.createTextNode(value));
  parent.appendChild(paragraph);
}

// Display error text
function errorText(parent, text) {
  const error = document.createElement("p");
  error.textContent = text;
  parent.appendChild(error);
}

// Render Add review button if authenticated
function renderAddReviewButton() {
  const addReviewSection = document.getElementById("add-review");
  addReviewSection.innerHTML = "";
  if (!isAuthenticated()) {
    return;
  }

  const btn = document.createElement("button");
  btn.textContent = "Add a review";
  btn.className = "btn-add-review";
  btn.addEventListener("click", () => {
    window.location.href = `add_review.html?id=${encodeURIComponent(placeId)}`;
  });

  addReviewSection.appendChild(btn);
}

// Fetch and render place details from API
async function loadPlaceDetails() {
  // If id exist
  if (!placeId) {
    const detailsSection = document.getElementById("place-details");
    errorText(detailsSection, "Error: Place ID not found in URL.");
    return;
  }

  try {
    // Fetch details from API
    const response = await fetch(`${API_BACK}/places/${placeId}`);

    if (!response.ok) {
      throw new Error("Place not found");
    }

    const place = await response.json();
    const detailsSection = document.getElementById("place-details");

    // Prepare owner name
    const ownerName = place.owner
      ? `${place.owner.first_name} ${place.owner.last_name}`
      : "Unknown";

    // Prepare amenities list
    const amenitiesList = place.amenities && place.amenities.length > 0
      ? place.amenities.map(a => a.name).join(", ")
      : "No amenities";

    // Display place infos
    const infoDiv = document.createElement("div");
    infoDiv.className = "place-info";

    // Display place title
    const placeTitle = document.createElement("h1");
    placeTitle.textContent = place.title;
    infoDiv.appendChild(placeTitle);

    // Display details
    boldParagraph(infoDiv, "Host: ", ownerName);
    boldParagraph(infoDiv, "Price per night: ", `${place.price}€`);
    boldParagraph(infoDiv, "Description: ", place.description || "No description available");
    boldParagraph(infoDiv, "Rooms: ", place.rooms);
    boldParagraph(infoDiv, "Capacity: ", place.capacity);
    boldParagraph(infoDiv, "Surface: ", `${place.surface} m²`);
    boldParagraph(infoDiv, "Amenities: ", amenitiesList);
    detailsSection.appendChild(infoDiv);

    renderAddReviewButton();

    // Load reviews
    await loadReviews(placeId);

  } catch (err) {
    console.error(`Error loading place details:\n${err}`);
    const detailsSection = document.getElementById("place-details");
    errorText(detailsSection, `Error loading place details.\n${err}`);
  }
}

// Load reviews
async function loadReviews(placeId) {
  try {
    const response = await fetch(`${API_BACK}/places/${placeId}/reviews`);

    if (!response.ok) {
      throw new Error(`Failed to load reviews, error : ${response.status}`);
    }

    const reviews = await response.json();
    const reviewsSection = document.getElementById("reviews");
    reviewsSection.innerHTML = "";

    // Display reviews if exists
    if (reviews && reviews.length > 0) {
      reviews.forEach(review => {
        const reviewCard = document.createElement("div");
        reviewCard.className = "review-card";

        // Display review text
        const reviewText = document.createElement("p");
        reviewText.textContent = review.text;
        reviewCard.appendChild(reviewText);

        // Display details
        boldParagraph(reviewCard, "Rating: ", `${review.rating}/5`);

        reviewsSection.appendChild(reviewCard);
      });
    } else {
      errorText(reviewsSection, "No reviews yet.");
    }

  } catch (err) {
    console.error(`Error loading reviews:\n${err}`);
    const reviewsSection = document.getElementById("reviews");
    errorText(reviewsSection, `Error loading reviews.\n${err}`);
  }
}

// Handle new review
async function handleReviewSubmit(event) {
  event.preventDefault();

  // Check if user is connected
  const accessToken = getCookie("access_token");
  if (!accessToken) {
    alert("Please log in to submit a review.");
    return;
  }

  // Fetch form datas
  const text = document.getElementById("review-text") ? document.getElementById("review-text").value : null;
  const rating = document.getElementById("review-rating") ? parseInt(document.getElementById("review-rating").value, 10) : null;

  try {
    // Send to API
    const response = await fetch(`${API_BACK}/reviews/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${accessToken}`
      },
      body: JSON.stringify({
        text: text,
        rating: rating,
        place_id: placeId
      })
    });

    if (!response.ok) {
      const error = await response.json();
      alert(`Error: ${error.error || "Failed to submit review"}`);
      return;
    }

    // Load review to display
    await loadReviews(placeId);

    alert("Review submitted successfully!");

  } catch (err) {
    console.error(`Error submitting review:\n${err}`);
    alert(`Error submitting review.\n${err}`);
  }
}

// Init place details if DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  const placeId = new URLSearchParams(window.location.search).get("id");
  if (!placeId) return;

  loadPlaceDetails(placeId);

  const reviewForm = document.getElementById("review-form");
  if (reviewForm) {
    reviewForm.addEventListener("submit", handleReviewSubmit);
  }
});
