# Bug Reports - Sauce Demo E-Commerce App

---

## BUG-001: Checkout Proceeds with Empty Cart

- **Severity:** High
- **Priority:** High
- **Status:** Open
- **Reporter:** Saif Magdy
- **Date Found:** March 2026

### Steps to Reproduce
1. Login with standard_user / secret_sauce
2. Do NOT add any items to cart
3. Click the cart icon
4. Click "Checkout"

### Expected Result
System should prevent checkout and display: "Your cart is empty. Please add items before checking out."

### Actual Result
Checkout flow proceeds normally with no items, allowing user to enter info and reach order confirmation with an empty order.

### Impact
Users can complete the checkout flow without any items, potentially causing empty orders in the system.

---

## BUG-002: Sort Dropdown Non-Functional for Problem User

- **Severity:** Medium
- **Priority:** Medium
- **Status:** Open
- **Reporter:** Saif Magdy

### Steps to Reproduce
1. Login with problem_user / secret_sauce
2. On the inventory page, click the sort dropdown
3. Select any sort option (e.g., "Price (low to high)")

### Expected Result
Products should re-order according to the selected sort option.

### Actual Result
Products remain in the same order regardless of sort selection. Sort dropdown does not function.

### Impact
Problem user account cannot sort products, degrading usability.

---

## BUG-003: All Product Images Incorrect for Problem User

- **Severity:** Medium
- **Priority:** Medium
- **Status:** Open
- **Reporter:** Saif Magdy

### Steps to Reproduce
1. Login with problem_user / secret_sauce
2. View the product catalog

### Expected Result
Each product should display its correct corresponding image.

### Actual Result
All 6 products display the same incorrect image (a dog/animal picture unrelated to the products).

### Impact
Visual product identification is impossible for problem_user, breaking the shopping experience.

---

## BUG-004: Add to Cart Broken on Product Detail Page for Problem User

- **Severity:** Medium
- **Priority:** Medium
- **Status:** Open
- **Reporter:** Saif Magdy

### Steps to Reproduce
1. Login with problem_user / secret_sauce
2. Click on any product to open the detail page
3. Click "Add to cart"

### Expected Result
Product is added to cart; cart badge increments by 1.

### Actual Result
Clicking "Add to cart" on product detail page has no effect. Cart badge does not update and product is not added.

### Impact
Problem user cannot add products from the detail page, only from the main catalog listing.

---

## Summary
| Bug ID | Description | Severity | Status |
|---|---|---|---|
| BUG-001 | Checkout proceeds with empty cart | High | Open |
| BUG-002 | Sort dropdown broken for problem_user | Medium | Open |
| BUG-003 | All product images wrong for problem_user | Medium | Open |
| BUG-004 | Add to cart broken on detail page | Medium | Open |
