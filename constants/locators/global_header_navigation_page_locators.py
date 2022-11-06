from selenium.webdriver.common.by import By


class GlobalHeaderNavigationLocator:
    # log in
    log_in_button = (By.CLASS_NAME, 'login')
    username = (By.ID, 'edit-name')
    password = (By.ID, 'edit-pass')
    submit_button = (By.ID, 'edit-submit')

    # logged in user
    user_avatar = (By.CLASS_NAME, 'avatar-image')
    user_name = (By.CLASS_NAME, 'user-name')
    level_game = (By.CLASS_NAME, 'user-xp')
    log_out_button = (By.CLASS_NAME, 'logout')
    user_page_button = (By.CLASS_NAME, 'my-page')
    user_profile_page = (By.CLASS_NAME, 'container')
    close_button = (By.CLASS_NAME, 'btn-close')

    # sign up
    sign_up_button = (By.CLASS_NAME, 'free-account')
    confirm_password = (By.ID, 'edit-confirm-pass')
    sign_up_avatar_wrapper = (By.ID, 'edit-field-avatar-id-wrapper')
    sign_up_theme_selector = (By.ID, 'edit-theme-selector')
    default_nickname = (By.CLASS_NAME, 'form-group')
    generate_nickname = (By.ID, 'edit-regen-public-name')
    create_nickname = (By.ID, 'edit-custom-public-name')
    sign_up = (By.ID, 'edit-submit')
