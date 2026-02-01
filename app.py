from flask import Flask, request, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

EMAIL_ADDRESS = 'melissaunlu4@gmail.com'
EMAIL_PASSWORD = 'btcq xmgs zknm pqnj'

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    email_message = EmailMessage()
    email_message['Subject'] = f'New message from {name} via portfolio site'
    email_message['From'] = EMAIL_ADDRESS
    email_message['To'] = EMAIL_ADDRESS
    email_message.set_content(f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(email_message)
    except Exception as e:
        print(f"Error sending email: {e}")
        # Return a clear error response
        return "Failed to send message, please try again later.", 500

    # If everything went fine, redirect to thank you page
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return "Thanks for your message! I'll get back to you soon."

if __name__ == "__main__":
    app.run(debug=True)

