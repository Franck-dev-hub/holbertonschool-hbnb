// Get the place name from URL
const placeId = parseInt(new URLSearchParams(window.location.search).get("id"), 10);
const place = places.find(p => p.id === placeId);

// Display place info
const detailsSection = document.getElementById("place-details");
if (place) {
  const infoDiv = document.createElement("div");
  infoDiv.className = "place-info";
  infoDiv.innerHTML = `
    <h1>${place.name}</h1>
    <p><strong>Host:</strong> ${place.host}</p>
    <p><strong>Price per night:</strong> $${place.pricePerNight}</p>
    <p><strong>Description:</strong> ${place.description}</p>
    <p><strong>Amenities:</strong> ${place.amenities.join(", ")}</p>
  `;

  detailsSection.appendChild(infoDiv);

  // Display reviews
  const reviewsSection = document.getElementById("reviews");
  if (place.reviews.length > 0) {
    place.reviews.forEach(review => {
      const reviewCard = document.createElement("div");
      reviewCard.className = "review-card";
      reviewCard.innerHTML = `
        <p><strong>${review.user}:</strong> ${review.comment}</p>
        <p>Rating: ${review.rating}/5</p>
      `;
      reviewsSection.appendChild(reviewCard);
    });
  } else {
    reviewsSection.innerHTML += "<p>No reviews yet.</p>";
  }
}

async function loadPlaces() {
  try {
    const response = await fetch("http://localhost:5000/api/v1/places", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    if (!response.ok) {
      alert("Failed to fetch places");
      return;
    }

    const data = await response.json();

    setCookie("access_token", dataaccess_token);
    updateButtons()
    window.location.href = "index.html";

  } catch (err) {
    console.error("Login error:", err);
  }
}
