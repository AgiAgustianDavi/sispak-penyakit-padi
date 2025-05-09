from flask import Flask, render_template, request
from rules import forward_chaining

app = Flask(__name__)

def validate_cf_value(value, field_name, errors):
    try:
        val = float(value)
        if val < 0 or val > 1:
            errors.append(f"Tingkat keyakinan untuk '{field_name}' harus antara 0 dan 1.")
    except (ValueError, TypeError):
        errors.append(f"Tingkat keyakinan untuk '{field_name}' harus berupa angka antara 0 dan 1.")

@app.route("/", methods=["GET", "POST"])
def index():
    diagnosis = None
    errors = []
    if request.method == "POST":
        data = {
            "ada_bercak": request.form.get("ada_bercak"),
            "cf_ada_bercak": request.form.get("cf_ada_bercak"),
            "kuning_kering": request.form.get("kuning_kering"),
            "cf_kuning_kering": request.form.get("cf_kuning_kering"),
            "kerdil": request.form.get("kerdil"),
            "cf_kerdil": request.form.get("cf_kerdil"),
            "busuk": request.form.get("busuk"),
            "cf_busuk": request.form.get("cf_busuk"),
            "ters_hama": request.form.get("ters_hama"),
            "cf_ters_hama": request.form.get("cf_ters_hama"),
            "biji": request.form.get("biji")
        }
        # Validate CF inputs
        validate_cf_value(data["cf_ada_bercak"], "ada bercak", errors)
        validate_cf_value(data["cf_kuning_kering"], "kuning kering", errors)
        validate_cf_value(data["cf_kerdil"], "kerdil", errors)
        validate_cf_value(data["cf_busuk"], "busuk", errors)
        validate_cf_value(data["cf_ters_hama"], "terserang hama", errors)

        # Only run diagnosis if no errors
        if not errors:
            diagnosis = forward_chaining(data)

    return render_template("index.html", diagnosis=diagnosis, errors=errors)

if __name__ == "__main__":
    app.run(debug=True)