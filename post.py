import smtplib
import email.mime.text as emt

def send_email(to_email, code):
    sender = '2008illyak@gmail.com' # якщо будeте використовувати мою пошту для поганих справ, наколдую маленький пісюн!
    password = "hkmw basj xxio wtbw" # А це можете, це не важливо... Чи важливо?

    message = f"Ваш код підтвердження: \n{code}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender, password)
        msg = emt.MIMEText(message)
        msg["Subject"] = "Код підтвердження"
        server.sendmail(sender, to_email, msg.as_string() )

        print(f"Код підтвердження було надіслано на пошту {to_email}!")
    except Exception:
        print("Ну, сьогодні ти короч не регеструєшся( Вийди, почепай траву, там, ще щось зроби")

def main():
    to_email = '2008illyak@gmail.com'
    print(send_email(to_email, 1111))

if __name__ == "__main__":
    main()







