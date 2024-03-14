// Toggle password visibility
const passToggleBtn = document.getElementById("pass-toggle-btn");
const passwordInput = document.getElementById("password");

passToggleBtn.addEventListener("click", () => {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    passToggleBtn.className = "fa-solid fa-eye-slash"; // Change icon to eye-slash when password is visible
  } else {
    passwordInput.type = "password";
    passToggleBtn.className = "fa-solid fa-eye"; // Change icon to eye when password is hidden
  }
});
// Add event listener for toggling search box
const searchIcon = document.querySelector("#searchIcon");
const nav = document.querySelector(".nav");

searchIcon.addEventListener("click", () => {
  nav.classList.toggle("openSearch");
});

// Close search box when window is resized above a certain width
window.addEventListener("resize", () => {
  if (window.innerWidth > 768) {
    nav.classList.remove("openSearch");
  }
});

document.addEventListener("DOMContentLoaded", function() {
  const nav = document.querySelector(".nav"),
    searchIcon = document.querySelector("#searchIcon"),
    navOpenBtn = document.querySelector(".navOpenBtn"),
    navCloseBtn = document.querySelector(".navCloseBtn");

  searchIcon.addEventListener("click", () => {
    nav.classList.toggle("openSearch");
    nav.classList.remove("openNav");
    if (nav.classList.contains("openSearch")) {
      return searchIcon.classList.replace("uil-search", "uil-times");
    }
    searchIcon.classList.replace("uil-times", "uil-search");
  });

  navOpenBtn.addEventListener("click", () => {
    nav.classList.add("openNav");
    nav.classList.remove("openSearch");
    searchIcon.classList.replace("uil-times", "uil-search");
  });

  navCloseBtn.addEventListener("click", () => {
    nav.classList.remove("openNav");
  });
});

const cards = document.querySelectorAll('.card');

cards.forEach((card) => {
  card.addEventListener('mouseover', () => {
    card.style.transform = 'scale(1.05)';
  });

  card.addEventListener('mouseout', () => {
    card.style.transform = 'scale(1)';
  });
});

// Get the menu button and floating menu elements
const menuBtn = document.getElementById("menuBtn");
const floatingMenu = document.getElementById("floatingMenu");

// Menu items data
const menuItemsData = [
  "Kidneys and Your Health",
  "How Your Kidneys Work",
  "About Kidney Disease",
  "Social Determinants of Kidney Disease",
  "Newly Diagnosed? Start Here"
];

// Function to toggle the visibility of the floating menu
function toggleMenu() {
  floatingMenu.style.display = floatingMenu.style.display === "block" ? "none" : "block";
}

// Function to create menu items dynamically
function createMenuItems() {
  const menuItems = document.getElementById("menuItems");
  menuItems.innerHTML = ""; // Clear previous items

  menuItemsData.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item;
    menuItems.appendChild(li);
  });
}


// Add event listener to the menu button
menuBtn.addEventListener("click", () => {
  console.log("Menu button clicked");
  toggleMenu();
  createMenuItems();
});
