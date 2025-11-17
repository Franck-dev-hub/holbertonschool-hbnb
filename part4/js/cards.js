// Exemple data
const places = [
  { id: 1, name: "Cozy Cottage", pricePerNight: 120 },
  { id: 2, name: "Luxury Villa", pricePerNight: 450 },
  { id: 3, name: "City Apartment", pricePerNight: 200 },
  { id: 4, name: "Beach Bungalow", pricePerNight: 300 }
];

// Function to display places as cards
function displayPlaces(placesList) {
  const container = document.getElementById("places-list");
  container.innerHTML = "";

  placesList.forEach(place => {
    // Create card div
    const card = document.createElement("div");
    card.className = "place-card";

    // Add place name
    const name = document.createElement("h3");
    name.textContent = place.name;
    card.appendChild(name);

    // Add price per night
    const price = document.createElement("p");
    price.textContent = `Price per night: ${place.pricePerNight}€`;
    card.appendChild(price);

    // Add "View Details" button
    const button = document.createElement("button");
    button.className = "details-button";
    button.textContent = "View Details";
    button.addEventListener("click", () => {
      window.location.href = `place.html?id=${place.id}`
    });
    card.appendChild(button);

    // Append card to container
    container.appendChild(card);
  });
}

// Initialize
displayPlaces(places);
