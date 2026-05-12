# Pick Perfect -  Testing

![Pick Perfect shown on a variety of screen sizes](/docs/mockup/mockup-all-framed.png)

Visit the deployed site: [Pick Perfect](https://pickperfect-2e4acff925d2.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javascript-validator)
  * [Lighthouse](#lighthouse)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

Testing was ongoing throughout the entire build. I utilised Chrome developer tools whilst building to pinpoint and troubleshoot any issues as I went along.

During development I made use of google developer tools to ensure everything was working correctly and to assist with troubleshooting when things were not working as expected.

I utilised the console in the developer tools to work through small sections of JavaScript and ensure that the code was working, and also to troubleshoot where issues were.

I have gone through each page using google chrome developer tools & Firefox inspector tool to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

* [Home](/docs/testing/html-validator/html/home.png) - Passed.
* [Shop](/docs/testing/html-validator/html/shop.png) - Passed.
* [Checkout](/docs/testing/html-validator/html/checkout.png) - Passed.
* [Shopping Cart](/docs/testing/html-validator/html/bag.png) - Passed.

* [style.css](/docs/testing/html-validator/css/) - Passed, no errors found.

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [javascript.js](/docs/testing/js-hint) - Passed.

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

### Desktop Results

All pages of the site are achieving a score of 100 across the 4 categories.

![Home](/docs/testing/lighthouse/home.png)

![shop](/docs/testing/lighthouse/shop.png)

![Details](/docs/testing/lighthouse/detail.png)

![Contact](/docs/testing/lighthouse/contact.png)

![Login](/docs/testing/lighthouse/login.png)

![Signup](/docs/testing/lighthouse/signup.png)

![Porfile](/docs/testing/lighthouse/profile.png)

![Order](/docs/testing/lighthouse/order.png)



### Mobile Results

Each page is achieving a score of 100 for the last three categories. The performance category is achieving a score of 98 for the first three pages and a score of 99 on the 404 & 500 page.

![Home](/docs/testing/lighthouse/mobile/home.png)

![Shop](/docs/testing/lighthouse/mobile/shop.png)

![Details](/docs/testing/lighthouse/mobile/details.png)

![Contact](/docs/testing/lighthouse/mobile/contact.png)#

![Profile](/docs/testing/lighthouse/mobile/profile.png)


## 🧪 MANUAL TESTING

Manual testing was conducted to ensure that the **Pick Perfect eCommerce website** functions correctly based on real-world user scenarios. This testing focused on validating key features such as product browsing, cart management, user authentication, and the checkout process to ensure a smooth and reliable shopping experience.

---

## 🧪 Testing User Stories

This section documents the manual testing performed for the **Pick Perfect eCommerce Website**.  
Each user story represents a core feature tested to confirm correct functionality and user experience.

---

### ✅ User Story 1 – Browse Products
**As** a customer  
**I want to** browse available products  
**So that** I can view items before making a purchase.

- [x] Products load correctly on the homepage and category pages  
- [x] Product images, names, prices, and descriptions display properly  
- [x] Category filtering works as expected  
- [x] No broken images or missing product data  

---

### ✅ User Story 2 – View Product Details
**As** a customer  
**I want to** view detailed information about a product  
**So that** I can decide whether to purchase it.

- [x] Product detail page loads correctly  
- [x] Displays full description, price, images, and stock status  
- [x] “Add to Cart” button works as expected  
- [x] Related products section displays correctly  

---

### ✅ User Story 3 – Add to Cart
**As** a customer  
**I want to** add products to my shopping cart  
**So that** I can purchase multiple items together.

- [x] Items added successfully to cart  
- [x] Cart icon updates with correct item count  
- [x] Duplicate items increase quantity correctly  
- [x] Cart persists during navigation  

---

### ✅ User Story 4 – Update / Remove Cart Items
**As** a customer  
**I want to** update or remove items in my cart  
**So that** I can manage my order before checkout.

- [x] Quantity updates correctly  
- [x] Remove item functionality works  
- [x] Cart total updates automatically  
- [x] Empty cart message displayed when no items remain  

---

### ✅ User Story 5 – User Registration
**As** a new user  
**I want to** create an account  
**So that** I can place orders and access my profile.

- [x] Registration form validates required fields  
- [x] Email format validation works correctly  
- [x] Duplicate email accounts are prevented  
- [x] Successful registration redirects to login page  

---

### ✅ User Story 6 – User Login
**As** a returning user  
**I want to** log into my account  
**So that** I can access my shopping activity.

- [x] Valid login credentials authenticate successfully  
- [x] Invalid credentials show error messages  
- [x] Session persists after login  
- [x] Logout clears session properly  

---

### ✅ User Story 7 – Checkout Process
**As** a customer  
**I want to** complete my purchase  
**So that** I can receive my order.

- [x] Checkout page loads correctly  
- [x] Shipping and billing details validated  
- [x] Order summary displays correct totals  
- [x] Order confirmation displayed successfully  

---

## 🧩 Additional Manual Tests
- [x] All forms validated with proper error messages  
- [x] Navigation links tested across all pages  
- [x] Responsive design tested on mobile, tablet, and desktop  
- [x] Cross-browser testing completed (Chrome, Firefox, Edge)  
- [x] No broken links or missing pages found  

---

## 🧭 Test Environment

- **Browsers:** Google Chrome, Firefox, Microsoft Edge  
- **Devices:** Desktop, Laptop, Android Mobile, iPhone, Tablet  
- **Date:** October 2025  
- **Tested By:** Your Name  
- **Project:** Pick Perfect eCommerce Website  

---

## 🧰 How to Perform Manual Tests

1. Open the Pick Perfect website in a browser  
2. Browse products from homepage or categories  
3. View product details  
4. Add items to cart and verify updates  
5. Update or remove items in cart  
6. Register and log in with a test account  
7. Complete checkout process  

