// Function to load places from API
async function loadPlaces() {
  try {
    const response = await fetch(`${API_BACK}/places`);
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
        window.location.href = `place.html?id=${place.id}`;
      });
      card.appendChild(button);

      // Append card to container
      container.appendChild(card);
    });
  } catch (err) {
    console.error("Error loading places: ", err);
  }
}

// Function to populate price filter dropdown
async function loadPriceFilter() {
  try {
    const response = await fetch(`${API_BACK}/places`);
    const places = await response.json();
    const filterSelect = document.getElementById("price-filter");

    // Get unique prices and sort them
    const prices = [...new Set(places.map(p => p.price))].sort((a, b) => a - b);

    // Add default option
    const defaultOption = document.createElement("option");
    defaultOption.value = "";
    defaultOption.textContent = "All Prices";
    filterSelect.appendChild(defaultOption);

    // Add price options
    prices.forEach(price => {
      const option = document.createElement("option");
      option.value = price;
      option.textContent = `Less than ${price}€`;
      filterSelect.appendChild(option);
    });

    // Add filter change listener
    filterSelect.addEventListener("change", filterPlacesByPrice);
  } catch (err) {
    console.error("Error loading price filter: ", err);
  }
}

// Function to filter places by price
async function filterPlacesByPrice() {
  try {
    const selectedPrice = document.getElementById("price-filter").value;
    const response = await fetch(`${API_BACK}/places`);
    const places = await response.json();
    const container = document.getElementById("places-list");
    container.innerHTML = "";

    // Filter places based on selected max price
    const filtered = selectedPrice ? places.filter(p => p.price <= selectedPrice) : places;

    filtered.forEach(place => {
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
        window.location.href = `place.html?id=${place.id}`;
      });
      card.appendChild(button);

      // Append card to container
      container.appendChild(card);
    });
  } catch (err) {
    console.error("Error filtering places: ", err);
  }
}

// Initialize on page load
document.addEventListener("DOMContentLoaded", () => {
  loadPlaces();
  loadPriceFilter();
});
