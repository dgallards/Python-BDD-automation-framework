# VS Monitor Web Elements - Improved and Fixed Selectors
# XPath Selectors - Homepage & Navigation
GET_LOGIN_BUTTON_AT_HOMEPAGE = "//span[normalize-space(text())='Login'] | //button[normalize-space(text())='Login'] | //a[normalize-space(text())='Login']"

# XPath Selectors - Login Page
GET_LOGIN_LABEL_AT_LOGIN_PAGE = "//h1[normalize-space(text())='Log-in'] | //h1[contains(normalize-space(text()), 'Login')] | //h1[contains(normalize-space(text()), 'Sign in')]"
GET_LOGIN_BUTTON_AT_LOGIN_PAGE = "//button[normalize-space(text())='Log-in'] | //button[normalize-space(text())='Login'] | //button[normalize-space(text())='Sign in'] | //input[@type='submit' and contains(@value, 'Log')]"

# XPath Selectors - Dashboard
GET_DASHBOARD_LABEL = "//h1[normalize-space(text())='Dashboard'] | //h2[normalize-space(text())='Dashboard'] | //*[contains(@class, 'dashboard') and contains(normalize-space(text()), 'Dashboard')]"

# XPath Selectors - User Navigation (Fixed concatenation)
GET_USER_NAVIGATION_MENU_BUTTON = "//div[@aria-label='nav-user-button'] | //button[@aria-label='nav-user-button'] | //*[contains(@aria-label, 'user') and contains(@aria-label, 'nav')]"
GET_OPEN_SIDEBAR = "//button[@aria-label='open-sidebar-btn'] | //button[contains(@aria-label, 'sidebar')] | //*[@data-testid='sidebar-toggle']"

# Fixed navigation menu selectors (proper XPath concatenation)
GET_USER_NAVIGATION_MENU_DESKTOP = "//div[@id='nav-desktop']//div[contains(@aria-label, 'nav-user-button')] | //div[@id='nav-desktop']//button[contains(@aria-label, 'user')]"
GET_USER_NAVIGATION_MENU_MOBILE = "//div[@id='nav-mobile']//div[contains(@aria-label, 'nav-user-button')] | //div[@id='nav-mobile']//button[contains(@aria-label, 'user')]"
GET_MY_USER_ACCOUNT_LABEL = "//span[normalize-space(text())='My user account'] | //*[contains(normalize-space(text()), 'user account')] | //*[contains(normalize-space(text()), 'Account')]"

# ID Selectors - Login Form
GET_USERNAME_INPUT_AT_LOGIN_PAGE = "username"
GET_USERNAME_INPUT_FALLBACK = "//input[@id='username'] | //input[@name='username'] | //input[@placeholder*='username'] | //input[@type='text'][1]"

GET_PASSWORD_INPUT_AT_LOGIN_PAGE = "password"
GET_PASSWORD_INPUT_FALLBACK = "//input[@id='password'] | //input[@name='password'] | //input[@type='password']"

# ID Selectors - Error Messages
GET_LOGIN_ERROR_MESSAGE = "error-password"
GET_LOGIN_ERROR_FALLBACK = "//*[@id='error-password'] | //*[contains(@class, 'error')] | //*[contains(@class, 'alert')] | //*[@role='alert']"

# ID Selectors - User Profile
GET_USER_PROFILE = "user-profile"
GET_USER_PROFILE_FALLBACK = "//*[@id='user-profile'] | //*[contains(@class, 'user-profile')] | //*[@data-testid='user-profile']"

# Changed these to be primary XPaths, as they are more robust.
# You can still have a simple ID if you wish, but for "visibility"
# and reliability, XPath fallbacks are often better.
GET_USER_FIRST_NAME = "//input[@id='firstName'] | //input[@name='firstName'] | //input[@name='first_name'] | //*[contains(@class, 'first-name')]"
GET_USER_LAST_NAME = "//input[@id='lastName'] | //input[@name='lastName'] | //input[@name='last_name'] | //*[contains(@class, 'last-name')]"
GET_USER_EMAIL = "//input[@id='email'] | //input[@name='email'] | //input[@type='email'] | //*[contains(@class, 'email')]"


# Additional Robust Selectors for Common Elements
GET_LOGOUT_BUTTON = "//button[normalize-space(text())='Logout'] | //a[normalize-space(text())='Logout'] | //*[contains(@class, 'logout')]"
GET_LOADING_SPINNER = "//*[contains(@class, 'loading')] | //*[contains(@class, 'spinner')] | //*[@data-testid='loading']"
GET_SUCCESS_MESSAGE = "//*[contains(@class, 'success')] | //*[contains(@class, 'alert-success')] | //*[@role='alert'][contains(@class, 'success')]"