"use strict";
const formElement = document.querySelector("form");
const overlayDiv = document.querySelector(".overlay");
const cancelFormBtn = document.getElementById("reset_btn");
const addListingBtns = document.querySelector(".new_listing_btns");
const fieldsetForRoomSizeInput = document.getElementById("room_size_input");

const toggleFormOverlay = function () {
  formElement.parentElement.classList.toggle("hidden");
  overlayDiv.classList.toggle("hidden");
  if (!overlayDiv.classList.contains("hidden")) {
    window.scroll({
      top: 0,
      left: 0,
      behavior: "smooth",
    });
  }
};

const toggleWithClick = function (e) {
  const elem = e.target;

  if (
    elem === overlayDiv ||
    elem === cancelFormBtn ||
    elem.parentNode === addListingBtns
  ) {
    toggleFormOverlay();

    if (elem.id === "new_home_listing-btn")
      fieldsetForRoomSizeInput.disabled = false;
    else fieldsetForRoomSizeInput.disabled = true;
  }
};

document.addEventListener("click", toggleWithClick);
