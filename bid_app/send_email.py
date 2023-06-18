from django.shortcuts import render
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from django.contrib import messages
def sendemail(to, name, otp):
    sender = "Online Auction"
    toemail = to
    toname = name
    fromemail = 'suhasj989@gmail.com'
    subject = "OTP Verification"
    message = "Dear "+ name +", Your Email Verification code is : "+str(otp)
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = subject
    html_content = message
    sender = {"name": sender, "email": fromemail}
    to = [{"email": toemail, "name": toname}]
    headers = {"Some-Custom-Name": "unique-id-1234"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers,html_content=html_content, sender=sender, subject=subject)
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
        return True
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)