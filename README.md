# BDD Saucedemo Project – Test Automation with Behave & Selenium
## Description

This project represents an automated test suite written using
Behavior-Driven Development (BDD) with Behave, together with the Page Object Model (POM).
The tests validate the essential functionalities of a web application:
Login, Products, Cart, and Checkout.
The project is structured to be easy to extend, maintain, and integrate
into a real-world QA Automation environment.

## Technologies Used

Python 3.13

Behave – BDD framework

Selenium WebDriver

Page Object Model (POM)

Chrome / Edge / Firefox WebDriver

## Installation

1. Clone the project:
```bash
   git clone https://github.com/28mirceas/Proiect-BDD.git
   cd Proiect-BDD
```
2. Install dependencies:
```bash   
pip install -r requirements.txt
```

3. Make sure you have the appropriate WebDriver installed

ChromeDriver / EdgeDriver / GeckoDriver
- Can be configured in browser.py

## Running the Tests
Simple run:
behave
Verbose run:
behave -v
Run a specific feature:
behave features/login.feature

## Included Test Scenarios
  Login
   • Login with valid credentials
   • Login with invalid email
   • Error on incorrect password
Products
   • Navigate to products page
   • View product list
   • Add product to cart
Shopping Cart
   • Verify products in cart
   • Update quantity
   • Remove products
Checkout
   • Fill in user details
   • Validate required fields
   • Order confirmation

## Project Structure
```bash 
BDD-Saucedemo-Project/
│
│ behave.ini # Behave configuration (report settings, language, etc.)
│ browser.py # Selenium WebDriver initialization
│ environment.py # Behave hooks (before_all, after_scenario etc.)
│ requirements.txt # Python dependencies
│ README.md # Project documentation
│
├───features/ # BDD scenarios (.feature files)
│ cart.feature
│ checkout.feature
│ login.feature
│ products.feature
│
├───pages/ # Page Object Model
│ base_page.py
│ cart_page.py
│ checkout_page.py
│ login_page.py
│ products_page.py
│
├───steps/ # Behave step implementations
│ cart_steps.py
│ checkout_steps.py
│ login_steps.py
│ products_steps.py
│
└───pycache/ # Auto-generated files
```

Page Object Model
All pages are defined in the folder:
pages/
Each file contains:
• element locators
• available page actions
• reusable methods for scenarios
Examples:
• login_page.py
• products_page.py
• cart_page.py
• checkout_page.py

Behave Configuration
The behave.ini file allows default configuration:
• language (Gherkin)
• report format
• run options

Behave Hooks
In environment.py, the following are defined:
• before_all
• before_scenario
• after_scenario
• after_all
These ensure:
• driver initialization and teardown
• attaching screenshots to reports (if enabled)
• resource cleanup

Reports
Depending on the configuration in behave.ini, you can generate:
• HTML reports
• JSON reports
• screenshots on failures

## License
[MIT](https://choosealicense.com/licenses/mit/)
