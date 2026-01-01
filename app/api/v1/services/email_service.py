import requests
from app.config.settings import settings

#Mail sender url
MAILERSEND_URL = "https://api.mailersend.com/v1/email"

#send verification email
def send_verification_email(to_email: str,username:str, token: str):
    
    verify_link = f"{settings.FRONTEND_VERIFY_URL}?token={token}"

    payload = {
    "from": {
        "email": settings.MAIL_FROM_EMAIL,
        "name": settings.MAIL_FROM_NAME,
    },
    "to": [
        {
            "email": to_email
        }
    ],
    "subject": "Verify your account",
    "text": f"Verify your account: {verify_link}",
    "html": f"""
        <p>Verify your account:</p>
        <a href="{verify_link}">Verify</a>
    """
}


    headers = {
        "Authorization": f"Bearer {settings.MAILERSEND_API_KEY}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        MAILERSEND_URL,
        json=payload,
        headers=headers,
        timeout=10,
    )

    print(response.status_code)
    print(response.text)



    response.raise_for_status()
