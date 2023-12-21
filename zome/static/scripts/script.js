"use strict";

function handleClickedListing(e) {
  const listing = e.target.closest(".listing");
  if (!listing) return;

  listing.querySelector(".listing_link").click();
}

document.addEventListener("click", handleClickedListing);
