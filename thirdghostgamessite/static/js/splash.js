document.addEventListener("DOMContentLoaded", () => {
  const logo = document.querySelector(".splash-logo");
  const button = document.getElementById("continue-btn");

  setTimeout(() => {
    logo.classList.add("visible");
  }, 500); // delay before fade-in starts

  setTimeout(() => {
    button.classList.remove("hidden");
    button.classList.add("show");
  }, 2500); // show button after image fade-in

  button.addEventListener("click", () => {
    window.location.href = "{% url 'home' %}"; 
  });
});
