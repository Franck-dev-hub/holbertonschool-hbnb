// Example data
const places = [
  {
    id: 1,
    name: "Cozy Cottage",
    host: "Alice",
    pricePerNight: 120,
    description: "A cozy cottage in the woods.",
    amenities: ["WiFi", "Fireplace", "Kitchen"],
    reviews: [
      { user: "John", comment: "Loved it!", rating: 5 },
      { user: "Emma", comment: "Very peaceful", rating: 4 }
    ]
  },
  {
    id: 2,
    name: "Luxury Villa",
    host: "Bob",
    pricePerNight: 450,
    description: "A luxurious villa with pool.",
    amenities: ["Pool", "WiFi", "Parking"],
    reviews: []
  },
  {
    id: 3,
    name: "City Apartment",
    host: "Claude",
    pricePerNight: 200,
    description: "A nice place in town.",
    amenities: ["WiFi"],
    reviews: []
  },
  {
    id: 4,
    name: "Beach Bungalow",
    host: "Daniel",
    pricePerNight: 300,
    description: "A nice holiday pied-a-terre.",
    amenities: ["WiFi", "Parking"],
    reviews: []
  }
];

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
