===========
BizflyTwoFa
===========

:Info: A python sdk for BizflyTwoFa.

:Repository: https://github.com/shinrel22/python_bizfly_two_fa

:Author: Tri Nguyen (https://github.com/shinrel22)

:Maintainer: Tri Nguyen (https://github.com/shinrel22)


Installation
============

``pip install bizfly_two_fa``

Examples
========
Some simple examples of what DataReducer can do:

.. code :: python

    import BizflyTwoFa from bizfly_two_fa

    bizfly_2fa = BizflyTwoFa(
        secret_key='app_secret_key'
    )

    # generate 2fa session
    session_uid = bizfly_2fa.gen_session(
        email='user_email',
        phone='user_phone'
    )

    # send otp
    bizfly_2fa.send_otp(
        session_uid=session_uid,
        delivery_type='sms',
    )

    # verify otp
    result = bizfly_2fa.verify_otp(
        otp_value='user otp input',
        session_uid=session_uid
    )
    print('result: ', result)
