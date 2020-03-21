from bizfly_two_fa.utils.methods import do_request
from bizfly_two_fa.constants import (GEN_SESSION_ENDPOINT, SEND_OTP_ENDPOINT, GET_SESSION_INFO_ENDPOINT,
                                     VERIFY_OTP_ENDPOINT, SEND_MEMBER_SECRET_KEY_ENDPOINT,
                                     CONFIRM_SESSION_ENDPOINT, BASE_URL)


class BizflyTwoFa(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def generate_session(self,
                         email,
                         phone=None):

        """
        Create session for 2fa.
        This method will create new user if email doesn't exist.
        :param email:
        :param phone:
        :return:
        """

        url = BASE_URL + GEN_SESSION_ENDPOINT

        data = dict(
            app_secret=self.secret_key,
            email=email,
            phone=phone
        )

        response = do_request(
            method='post',
            url=url,
            json=data,
        )
        if response.status_code == 200:
            res_data = response.json()
            return res_data['session_uid']

        raise Exception(response.content)

    def send_otp(self,
                 session_uid,
                 delivery_type):
        """
        Send otp to your user.
        :param session_uid: str
        :param delivery_type: str (app/sms/email/call)
        :return:
        """

        url = BASE_URL + SEND_OTP_ENDPOINT

        data = dict(
            otp_session_uid=session_uid,
            delivery_type=delivery_type
        )

        response = do_request(
            method='post',
            url=url,
            json=data
        )

        if response.status_code == 200:
            return response.json()

        raise Exception(response.content)

    def get_session_info(self, session_uid):
        url = BASE_URL + GET_SESSION_INFO_ENDPOINT

        data = dict(
            uid=session_uid,
        )

        response = do_request(
            method='get',
            url=url,
            params=data
        )

        if response.status_code == 200:
            return response.json()

        raise Exception(response.content)

    def verify_otp(self,
                   session_uid,
                   otp_value,
                   confirm_later=None):
        """
        Verify your user otp
        :param session_uid: str
        :param otp_value: str
        :param confirm_later: bool, only for using Bizfly2FA JS Popup on frontend
        :return:
        """

        url = BASE_URL + VERIFY_OTP_ENDPOINT

        data = dict(
            otp_session_uid=session_uid,
            confirm_later=confirm_later,
            otp=otp_value
        )

        response = do_request(
            method='post',
            url=url,
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            return result['success']

        raise Exception(response.content)

    def send_member_secret_key(self,
                               delivery_type,
                               email=None,
                               session_uid=None):
        """
        Send member's secret key.
        Must pass at least email or session_uid
        :param delivery_type: str
        :param email: str
        :param session_uid: str
        :return:
        """

        if not email and not session_uid:
            raise Exception('Must pass at least email or session_uid')

        data = dict(
            app_secret=self.secret_key,
            delivery_type=delivery_type,
            email=email,
            session_uid=session_uid
        )

        url = BASE_URL + SEND_MEMBER_SECRET_KEY_ENDPOINT

        response = do_request(
            method='post',
            url=url,
            json=data
        )

        if response.status_code == 200:
            return response.json()

        raise Exception(response.content)

    def confirm_session(self, session_uid, email):
        """
        Confirm session for JS popup integration
        :param session_uid: str
        :param email: str
        :return:
        """

        url = BASE_URL + CONFIRM_SESSION_ENDPOINT

        data = dict(
            email=email,
            otp_session_uid=session_uid
        )

        response = do_request(
            method='post',
            url=url,
            json=data
        )

        if response.status_code == 200:
            return response.json()

        raise Exception(response.content)

    def list_members(self):
        pass


VERSION = (1, 0, 4)
