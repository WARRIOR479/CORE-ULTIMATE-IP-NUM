from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

IPINFO_API = os.getenv("IPINFO_API")
VERIPHONE_API = os.getenv("VERIPHONE_API")


@app.route('/', methods=['GET', 'POST'])
def home():
    ip_data = None
    phone_data = None

    if request.method == 'POST':

        ip = request.form.get('ip')
        phone = request.form.get('phone')

        if ip:
            try:
                ip_url = f"https://ipinfo.io/{ip}?token={IPINFO_API}"
                response = requests.get(ip_url)
                ip_data = response.json()
            except:
                ip_data = {
                    'error': 'Failed to fetch IP data'
                }

        if phone:
            try:
                phone_url = f"https://api.veriphone.io/v2/verify?phone={phone}&key={VERIPHONE_API}"
                response = requests.get(phone_url)
                phone_data = response.json()
            except:
                phone_data = {
                    'error': 'Failed to fetch phone data'
                }

    return render_template(
        'index.html',
        ip_data=ip_data,
        phone_data=phone_data
    )


if __name__ == '__main__':
    app.run(debug=True)