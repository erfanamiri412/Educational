/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("add-to-cart");
  btn.addEventListener("click", function () {
    const productId = this.dataset.id;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // بررسی شناسه محصول
    if (!productId || productId === 'null') {
      alert("⚠️ محصول معتبر نیست!");
      return;
    }

    // ارسال درخواست AJAX
    fetch("{% url 'cart_add' %}", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": csrfToken
      },
      body: `product_id=${productId}`
    })
    .then(response => response.json())
    .then(data => {
      const cartQty = document.getElementById('cart-quantity');
      if (cartQty && data.qty !== undefined) {
        cartQty.textContent = data.qty;
      }

      if (data.exists) {
        const confirmAdd = confirm("این محصول قبلاً در سبد خرید شما هست! آیا می‌خواهید دوباره اضافه شود؟");
        if (!confirmAdd) return;
      }

      alert("✅ محصول با موفقیت به سبد خرید افزوده شد!");
    })
    .catch(error => {
      console.error("❌ خطا در افزودن محصول:", error);
      alert("مشکلی در افزودن محصول رخ داد.");
    });
  });
});
