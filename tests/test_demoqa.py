from pages.registration_page import RegistrationPage
from data.user import User


def test_registration_form():
    registraton_page = RegistrationPage()
    user = User(
        first_name="Sergei",
        second_name="Melnikov",
        email="Sergei@Melnikov.com",
        gender="Male",
        phone_number="4815162342",
        date_of_birth=["29", "July", "1991"],
        subjects="Computer Science",
        hobbies="Sports",
        picture="2024-05-12 22.04.05.jpg",
        current_address="Novi Sad",
        state="Haryana",
        city="Karnal",
    )

    registraton_page.open()
    registraton_page.fill_form(user)
    registraton_page.submit_form()
    registraton_page.should_registered_user_info_with(user)
