const btn_update = document.querySelectorAll(".btn_update");

btn_update.forEach((btn) => {
  btn.addEventListener("click", function () {
    let productId = btn.dataset.id;
    let action = btn.dataset.action;
    if (user !== "AnonymousUser") {
      updateOrder(productId, action);
      console.log("123");
    } else {
      addCookieItem(productId, action);
    }
  });
});

const updateOrder = (productId, action) => {
  const url = "/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
    mode: "same-origin",
  })
    .then((resolve) => {
      return resolve.json();
    })
    .then((resolve) => {
      location.reload();
      console.log(resolve);
    })
    .catch((reject) => {
      console.log(reject);
    });
};

const addCookieItem = (productId, action) => {
  if (action == "add") {
    if (!cart[productId]) {
      cart[productId] = { quantity: 1 };
    } else {
      cart[productId]["quantity"] += 1;
    }
  }
  if (action == "remove") {
    cart[productId]["quantity"] -= 1;
    if (cart[productId]["quantity"] <= 0) {
      delete cart[productId];
      console.log(`item has empty`);
    }
  }
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
  location.reload();
};