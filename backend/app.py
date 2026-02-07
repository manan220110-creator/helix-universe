from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Sample data for car valuation
CAR_BRANDS = {
    "Toyota": {"base_value": 15000, "depreciation_rate": 0.12},
    "Honda": {"base_value": 16000, "depreciation_rate": 0.11},
    "BMW": {"base_value": 40000, "depreciation_rate": 0.15},
    "Mercedes": {"base_value": 45000, "depreciation_rate": 0.16},
    "Audi": {"base_value": 38000, "depreciation_rate": 0.14},
    "Ford": {"base_value": 20000, "depreciation_rate": 0.13},
    "Chevrolet": {"base_value": 18000, "depreciation_rate": 0.12},
    "Volkswagen": {"base_value": 22000, "depreciation_rate": 0.12},
}

CONDITION_FACTORS = {
    "Excellent": 1.0,
    "Very Good": 0.85,
    "Good": 0.70,
    "Fair": 0.55,
    "Poor": 0.40,
}

def calculate_car_value(data):
    """Calculate estimated car value based on multiple factors"""
    brand = data.get("brand", "").strip()
    model = data.get("model", "")
    year = int(data.get("year", 2020))
    condition = data.get("condition", "Good")
    mileage = int(data.get("mileage", 0))
    maintenance_history = data.get("maintenance_history", "Average")
    accident_history = data.get("accident_history", False)
    
    # Get base value
    brand_data = CAR_BRANDS.get(brand, {"base_value": 15000, "depreciation_rate": 0.12})
    base_value = brand_data["base_value"]
    depreciation_rate = brand_data["depreciation_rate"]
    
    # Calculate age depreciation
    current_year = datetime.now().year
    age = current_year - year
    age_depreciation = 1 - (depreciation_rate * age)
    age_depreciation = max(0.1, age_depreciation)  # Minimum 10% of base value
    
    # Apply age depreciation
    current_value = base_value * age_depreciation
    
    # Apply condition factor
    condition_factor = CONDITION_FACTORS.get(condition, 0.70)
    current_value *= condition_factor
    
    # Mileage adjustment (0.15 per 10,000 km)
    mileage_adjustment = 1 - (mileage / 100000) * 0.15
    mileage_adjustment = max(0.2, mileage_adjustment)
    current_value *= mileage_adjustment
    
    # Maintenance history adjustment
    maintenance_factors = {
        "Excellent": 1.1,
        "Very Good": 1.05,
        "Average": 1.0,
        "Poor": 0.85,
    }
    maintenance_factor = maintenance_factors.get(maintenance_history, 1.0)
    current_value *= maintenance_factor
    
    # Accident history penalty
    if accident_history:
        current_value *= 0.8
    
    # Model premium (optional)
    model_premium = 1.0
    if "Sport" in model or "GT" in model:
        model_premium = 1.15
    elif "SUV" in model or "Truck" in model:
        model_premium = 1.05
    current_value *= model_premium
    
    return max(1000, round(current_value, 2))

@app.route("/api/brands", methods=["GET"])
def get_brands():
    """Get list of available car brands"""
    return jsonify({"brands": list(CAR_BRANDS.keys())})

@app.route("/api/conditions", methods=["GET"])
def get_conditions():
    """Get list of car conditions"""
    return jsonify({"conditions": list(CONDITION_FACTORS.keys())})

@app.route("/api/estimate", methods=["POST"])
def estimate_price():
    """Calculate estimated car price"""
    try:
        data = request.json
        
        # Validate required fields
        required_fields = ["brand", "model", "year", "condition", "mileage"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        estimated_value = calculate_car_value(data)
        
        # Calculate fair price range
        fair_min = estimated_value * 0.90
        fair_max = estimated_value * 1.10
        
        return jsonify({
            "estimated_price": estimated_value,
            "fair_min": round(fair_min, 2),
            "fair_max": round(fair_max, 2),
            "confidence": 0.85
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
