from pages.registration_page import RegistrationPage
import allure


def test_registration_form():
    registration_page = RegistrationPage()

    with allure.step("Open browser"):
        registration_page.open()


    with allure.step("Fill first name"):
        registration_page.fill_first_name("Sergei")

    with allure.step("Fill second name"):
        registration_page.fill_second_name("Melnikov")

    with allure.step("Fill e-mail"):
        registration_page.fill_email("Sergei@Melnikov.com")

    with allure.step("Select gender"):
        registration_page.select_gender("Male")

    with allure.step("Fill phone number"):
        registration_page.fill_phone_number("4815162342")

    with allure.step("Fill date of birth"):
        registration_page.fill_date_of_birth("July", "1991", "29")

    with allure.step("Fill subjects"):
        registration_page.fill_subjects("Computer Science")

    with allure.step("Fill hobbies"):
        registration_page.fill_hobbies("Sports")

    with allure.step("Fill picture"):
        registration_page.upload_picture("2024-05-12 22.04.05.jpg")

    with allure.step("Fill current address"):
        registration_page.fill_current_address("Novi Sad")

    with allure.step("Fill state"):
        registration_page.fill_state("Haryana")

    with allure.step("Fill city"):
        registration_page.fill_city("Karnal")

    with allure.step("Submit form"):
        registration_page.submit_form()


    with allure.step("Check registered user"):
        registration_page.should_registered_user_info_with(
        "Sergei Melnikov",
        "Sergei@Melnikov.com",
        "Male",
        "4815162342",
        "29 July,1991",
        "Computer Science",
        "Sports",
        "2024-05-12 22.04.05.jpg",
        "Novi Sad",
        "Haryana Karnal",
    )
