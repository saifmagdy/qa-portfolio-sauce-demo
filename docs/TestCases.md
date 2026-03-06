# Manual Test Cases - Sauce Demo

## Module 1: Authentication

### TC-001: Valid Login
- Priority: High | Type: Functional
- Steps: Navigate to saucedemo.com, enter standard_user/secret_sauce, click Login
- Expected: Redirected to /inventory.html, products displayed
- Status: PASS

### TC-002: Invalid Password
- Priority: High | Type: Negative
- Steps: Enter standard_user with wrong password, click Login
- Expected: Error message "Username and password do not match"
- Status: PASS

### TC-003: Empty Credentials
- Priority: Medium | Type: Negative
- Steps: Leave both fields empty, click Login
- Expected: Error "Username is required"
- Status: PASS

### TC-004: Locked Out User
- Priority: High | Type: Functional
- Steps: Login with locked_out_user/secret_sauce
- Expected: Error "Sorry, this user has been locked out"
- Status: PASS

### TC-005: Successful Logout
- Priority: Medium | Type: Functional
- Steps: Login, open burger menu, click Logout
- Expected: Redirected to login page, session cleared
- Status: PASS

### TC-006: Problem User Images
- Priority: Medium | Type: Functional
- Steps: Login with problem_user/secret_sauce, view product catalog
- Expected: All product images should match their descriptions
- Actual: All products show same wrong image (dog picture)
- Status: FAIL (BUG-003)

---

## Module 2: Product Catalog

### TC-007: Product Listing Display
- Priority: High | Type: Functional
- Steps: Login, navigate to inventory page
- Expected: 6 products visible with name, image, description, price, Add to Cart button
- Status: PASS

### TC-008: Sort by Price (Low to High)
- Priority: Medium | Type: Functional
- Steps: Login, select "Price (low to high)" from sort dropdown
- Expected: Products sorted ascending by price
- Status: PASS

### TC-009: Sort by Name (A-Z)
- Priority: Low | Type: Functional
- Steps: Login, select "Name (A to Z)" from dropdown
- Expected: Products sorted alphabetically
- Status: PASS

### TC-010: Product Detail Page
- Priority: Medium | Type: Functional
- Steps: Login, click on any product name
- Expected: Detail page shows full description, correct price, Add to Cart button
- Status: PASS

---

## Module 3: Shopping Cart

### TC-011: Add Single Item to Cart
- Priority: High | Type: Functional
- Steps: Login, click "Add to cart" on any product
- Expected: Cart badge shows "1", button changes to "Remove"
- Status: PASS

### TC-012: Add Multiple Items
- Priority: High | Type: Functional
- Steps: Add 3 different products to cart
- Expected: Cart badge shows "3", all items in cart
- Status: PASS

### TC-013: Remove Item from Cart
- Priority: High | Type: Functional
- Steps: Add item, click Remove
- Expected: Item removed, cart badge decremented
- Status: PASS

### TC-014: Cart Persistence After Navigation
- Priority: Medium | Type: Functional
- Steps: Add items, navigate to product detail, return to cart
- Expected: Cart items persist
- Status: PASS

### TC-015: Checkout with Empty Cart
- Priority: High | Type: Negative
- Steps: Navigate to cart with no items, click Checkout
- Expected: Error or prevention of checkout
- Actual: Checkout proceeds with empty cart
- Status: FAIL (BUG-001)

---

## Module 4: Checkout

### TC-016: Complete Checkout Flow
- Priority: High | Type: Functional
- Steps: Add item, checkout, fill info (John/Doe/12345), finish
- Expected: "Thank you for your order!" confirmation
- Status: PASS

### TC-017: Missing First Name Validation
- Priority: High | Type: Negative
- Steps: Start checkout, leave First Name blank, click Continue
- Expected: Error "First Name is required"
- Status: PASS

### TC-018: Missing Last Name Validation
- Priority: Medium | Type: Negative
- Steps: Fill first name only, click Continue
- Expected: Error "Last Name is required"
- Status: PASS

### TC-019: Missing Zip Code Validation
- Priority: Medium | Type: Negative
- Steps: Fill first and last name only, click Continue
- Expected: Error "Postal Code is required"
- Status: PASS

### TC-020: Order Summary Verification
- Priority: Medium | Type: Functional
- Steps: Add 2 items, go through checkout to summary
- Expected: Correct items, prices, and total shown
- Status: PASS

---

## Test Summary
| Module | Total | Pass | Fail |
|---|---|---|---|
| Authentication | 6 | 5 | 1 |
| Product Catalog | 4 | 4 | 0 |
| Shopping Cart | 5 | 4 | 1 |
| Checkout | 5 | 5 | 0 |
| **Total** | **20** | **18** | **2** |
