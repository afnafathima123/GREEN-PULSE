from flask import Flask, render_template, request, redirect, url_for, jsonify
import json, os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = os.path.join(os.environ.get("DATA_DIR", "."), "plants.json")

# --- Seed data if file doesn't exist ---
def load_plants():
    if not os.path.exists(DATA_FILE):
        default = [
            {"id": 1, "name": "Monstera Deliciosa", "type": "Tropical", "watered": "2025-03-28", "health": 92, "notes": "New leaf sprouting!", "emoji": "🌿"},
            {"id": 2, "name": "Snake Plant",        "type": "Succulent", "watered": "2025-03-25", "health": 78, "notes": "Thriving in low light.", "emoji": "🪴"},
            {"id": 3, "name": "Cherry Tomatoes",    "type": "Vegetable", "watered": "2025-03-29", "health": 85, "notes": "First flowers appearing!", "emoji": "🍅"},
        ]
        save_plants(default)
        return default
    with open(DATA_FILE) as f:
        return json.load(f)

def save_plants(plants):
    with open(DATA_FILE, "w") as f:
        json.dump(plants, f, indent=2)

@app.route("/")
def home():
    plants = load_plants()
    total = len(plants)
    avg_health = round(sum(p["health"] for p in plants) / total) if total else 0
    return render_template("index.html", plants=plants, total=total, avg_health=avg_health)

@app.route("/plant/<int:plant_id>")
def plant_detail(plant_id):
    plants = load_plants()
    plant = next((p for p in plants if p["id"] == plant_id), None)
    if not plant:
        return "Plant not found", 404
    return render_template("detail.html", plant=plant)

@app.route("/add", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        plants = load_plants()
        new_id = max((p["id"] for p in plants), default=0) + 1
        new_plant = {
            "id": new_id,
            "name": request.form.get("name", "My Plant"),
            "type": request.form.get("type", "Unknown"),
            "watered": datetime.today().strftime("%Y-%m-%d"),
            "health": int(request.form.get("health", 80)),
            "notes": request.form.get("notes", ""),
            "emoji": request.form.get("emoji", "🌱"),
        }
        plants.append(new_plant)
        save_plants(plants)
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/water/<int:plant_id>")
def water_plant(plant_id):
    plants = load_plants()
    for p in plants:
        if p["id"] == plant_id:
            p["watered"] = datetime.today().strftime("%Y-%m-%d")
            p["health"] = min(100, p["health"] + 5)
    save_plants(plants)
    return redirect(url_for("home"))

@app.route("/health")
def health_check():
    return jsonify({"status": "ok", "app": "GreenPulse", "version": "1.0.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
