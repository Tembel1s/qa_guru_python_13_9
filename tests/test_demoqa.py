from pages.registration_page import RegistrationPage


def test_registration_form():
    registraton_page = RegistrationPage()

    registraton_page.open()

    (
        registraton_page.fill_first_name("Sergei")
        .fill_second_name("Melnikov")
        .fill_email("Sergei@Melnikov.com")
        .select_gender("Male")
        .fill_phone_number("4815162342")
        .fill_date_of_birth("July", "1991", "29")
        .fill_subjects("Computer Science")
        .fill_hobbies("Sports")
        .upload_picture("2024-05-12 22.04.05.jpg")
        .fill_current_address("Novi Sad")
        .fill_state("Haryana")
        .fill_city("Karnal")
        .submit_form()
    )

    registraton_page.should_registered_user_info_with(
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
