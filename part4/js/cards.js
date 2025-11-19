// Function to load places from API
async function loadPlaces() {
  try {
    const response = await fetch("http://localhost:5000/api/v1/places");
    const places = await response.json();
    const container = document.getElementById("places-list");
    container.innerHTML = "";

    places.forEach(place => {
      // Create card div
      const card = document.createElement("div");
      card.className = "place-card";

      // Add place name
      const name = document.createElement("h3");
      name.textContent = place.title;
      card.appendChild(name);

      // Add description
      const desc = document.createElement("p");
      desc.textContent = place.description;
      card.appendChild(desc);

      // Add price per night
      const price = document.createElement("p");
      const label = document.createElement("strong");
      label.textContent = "Price per night: ";
      const value = document.createTextNode(`${place.price}€`);
      price.appendChild(label);
      price.appendChild(value);
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
  } catch (err) {
    console.error("Error loading places: ", err);
  }
}
document.addEventListener("DOMContentLoaded", loadPlaces);
