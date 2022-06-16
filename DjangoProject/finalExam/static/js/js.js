const btn_update = document.querySelectorAll(".btn_update");

btn_update.forEach((btn) => {
  btn.addEventListener("click", function () {
    if (user) {
      let productId = btn.dataset.id;
      let action = btn.dataset.action;
      updateOrder(productId, action);
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
