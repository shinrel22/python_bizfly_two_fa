import os

from bizfly_two_fa import BizflyTwoFa

if __name__ == '__main__':
    app_secret = os.getenv('TEST_APP_SECRET')
    email = os.getenv('TEST_USER_EMAIL')
    phone = os.getenv('TEST_USER_PHONE')

    bizfly_2fa = BizflyTwoFa(
        secret_key=app_secret
    )
    session_uid = bizfly_2fa.generate_session(
        email=email,
        phone=phone
    )
    print(session_uid)
