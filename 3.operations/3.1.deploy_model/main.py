# Standard Library Imports
import os
import ssl
import logging
import pickle

# Third-Party Imports
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_wtf import CSRFProtect
from flask_csp.csp import csp_header
from flask_limiter import Limiter # Rate limiter
from flask_limiter.util import get_remote_address # Rate limiter
from dotenv import load_dotenv

# Model Learning
import numpy as np

load_dotenv()

app = Flask(__name__)
app_log = logging.getLogger(__name__)
logging.basicConfig(
    filename="security_log.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
)

# CSRF
app.secret_key = b"f53oi3uriq9pifpff;apl" # os.getenv('secret_key')
csrf = CSRFProtect(app)

# Default rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "100 per hour", "1 per second"],
    storage_uri="memory://",
)

@app.errorhandler(429)
def ratelimit_handler(e):
    '''
    Rate limit
    '''
    flash("Rate limit exceeded. Please try again later.", "error")
    return redirect(url_for('index'))

# Redirect index.html to domain root for consistent UX
@app.route("/index", methods=["GET"])
@app.route("/index.htm", methods=["GET"])
@app.route("/index.asp", methods=["GET"])
@app.route("/index.php", methods=["GET"])
@app.route("/index.html", methods=["GET"])
def root():
    '''
    Redirect to the root URL
    '''
    return redirect("/", 302)


@app.route("/", methods=["POST", "GET"])
@csp_header(
    {
        # Server Side CSP is consistent with meta CSP in layout.html
        "base-uri": "'self'",
        "default-src": "'self'",
        "style-src": "'self'",
        "script-src": "'self'",
        "img-src": "'self' data:",
        "media-src": "'self'",
        "font-src": "'self'",
        "object-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "worker-src": "'self'",
        "report-uri": "/csp_report",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "frame-src": "'none'"
    }
)

def index():
    '''
    Landing page with ML prediction
    '''
    result = None
    if request.method == "POST":
        try:
            # Grab each form input directly
            temp = float(request.form.get("Temp"))
            humidity = float(request.form.get("Humidity"))
            dew_point_temp = float(request.form.get("DewPointTemp"))
            wind_speed = float(request.form.get("WindSpeed"))
            rainfall = float(request.form.get("Rainfall"))
            hour = int(request.form.get("Hour"))

            # Combine into feature list in the order your model expects
            features = [[temp, humidity, dew_point_temp, wind_speed, rainfall, hour]]

            # Load model
            model_path = os.path.join(app.root_path, 'models', 'model.pkl')
            if os.path.exists(model_path):
                with open(model_path, 'rb') as f:
                    model = pickle.load(f)

                # Make prediction
                prediction = model.predict(features)[0]
                result = int(round(prediction))
                app_log.info("ML prediction: %s", result)
            else:
                flash("Model not available", "error")

        except ValueError:
            flash("Please enter valid numbers", "error")
        except Exception as e:
            app_log.error("Prediction error: %s", str(e))
            flash(f"Error: {str(e)}", "error")
    return render_template("/index.html", result=result)


@app.route("/privacy.html", methods=["GET"])
def privacy():
    '''
    Privacy policy page
    '''
    return render_template("/privacy.html")

# Endpoint for logging CSP violations
@app.route("/csp_report", methods=["POST"])
@csrf.exempt
def csp_report():
    '''
    Report CSP violations
    '''
    app.logger.critical(request.data.decode())
    return "done"


## SSL Encryption
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('certs/certificate.pem', 'certs/privatekey.pem')


if __name__ == "__main__":
    debug_mode = os.getenv('FLASK_DEBUG', 'True').lower() in ['true', '1', 't']
    app.run(debug=True, host="127.0.0.1", port=5000, ssl_context=None) # 'context' for HTTPS, SSL
