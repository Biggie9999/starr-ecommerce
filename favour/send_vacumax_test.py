import os
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import sys

def send_test_email(to_email):
    HOSTINGER_EMAIL = "Doan.Pendleton@vacu-max.com"
    HOSTINGER_PASSWORD = "@Echelon99"
    HOSTINGER_SENDER_NAME = "Doan Pendleton"
    SMTP_SERVER = "smtp.hostinger.com"
    SMTP_PORT = 465

    subject = "Procurement Proposal for Vac-U-Max Partner"
    
    with open("vacumax_email_template.html", "r", encoding="utf-8") as f:
        base_html = f.read()
        
    custom_body = """
    <p>Hello John,</p>
    <p>I hope you are doing well.</p>
    <p>Vac-U-Max has a proposal for a partnership on a procurement project that I want you to attend to as soon as possible.</p>
    <p>A reply at your earliest convenience would be much appreciated.</p>
    """
    
    final_html = base_html.replace("<!-- BODY_PLACEHOLDER -->", custom_body)
    
    # 1. Parent MUST be 'related' when embedding CID images
    msg = MIMEMultipart('related')
    msg["From"] = email.utils.formataddr((HOSTINGER_SENDER_NAME, HOSTINGER_EMAIL))
    msg["To"] = to_email
    msg["Subject"] = subject
    msg["Date"] = email.utils.formatdate(localtime=True)
    msg["Message-ID"] = email.utils.make_msgid(domain="vacu-max.com")
    
    # 2. Alternative part for text/html
    msg_alt = MIMEMultipart('alternative')
    msg.attach(msg_alt)
    
    plain_text = "Hello, Vac-U-Max has a proposal for a partnership on a procurement project..."
    msg_alt.attach(MIMEText(plain_text, "plain", "utf-8"))
    msg_alt.attach(MIMEText(final_html, "html", "utf-8"))

    # 3. Attach image
    img_path = "vacumax_logo.png"
    if os.path.exists(img_path):
        with open(img_path, 'rb') as img_file:
            img_data = img_file.read()
            image = MIMEImage(img_data, name="vacumax_logo.png")
            image.add_header('Content-ID', '<vacumax_logo.png>')
            image.add_header('Content-Disposition', 'inline', filename="vacumax_logo.png")
            msg.attach(image)
    else:
        print(f"Warning: Logo {img_path} not found.")

    try:
        print(f"Connecting to {SMTP_SERVER}:{SMTP_PORT} via SSL...")
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=60)
        server.login(HOSTINGER_EMAIL, HOSTINGER_PASSWORD)
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()
        print(f"✅ Full format test email successfully sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send test email: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_test_email(sys.argv[1])
    else:
        print("Usage: python3 send_vacumax_test.py target_email@domain.com")
