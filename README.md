# 🚗 Car Price Estimator App

A modern, full-stack web application that helps you estimate fair selling prices for your car based on multiple factors including brand, model, year, condition, mileage, and maintenance history.

## Features

✨ **Modern UI with Smooth Animations**
- Beautiful gradient background design
- Smooth transitions and animations
- Responsive design for all devices
- Interactive price cards with hover effects

🎯 **Smart Price Estimation**
- Brand-specific base valuations
- Age depreciation calculation
- Mileage impact assessment
- Condition factor analysis
- Maintenance history consideration
- Accident history penalty
- Model premium adjustment

📊 **Comprehensive Car Analysis**
- Brand selection from popular manufacturers
- Model customization
- Year of purchase
- Condition levels (Excellent to Poor)
- Mileage tracking
- Maintenance history
- Accident history flag

🔐 **Reliable Backend**
- Python Flask REST API
- CORS enabled for frontend integration
- Real-time price calculations
- Fair price range generation

## Project Structure

```
car-price-estimator/
├── backend/
│   ├── app.py                 # Flask backend with estimation logic
│   └── requirements.txt        # Python dependencies
├── frontend/
│   └── index.html            # React frontend with UI
└── README.md                 # This file
```

## Installation & Setup

### Backend Setup

1. **Install Python dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Run the Flask server:**
   ```bash
   python app.py
   ```
   The backend will be available at `http://localhost:5000`

### Frontend Setup

1. **Open the frontend:**
   Simply open `frontend/index.html` in your web browser or serve it with a local server:
   ```bash
   # Using Python 3
   cd frontend
   python -m http.server 8000
   ```
   Then visit `http://localhost:8000`

## How to Use

1. **Select a Car Brand** - Choose from Toyota, Honda, BMW, Mercedes, Audi, Ford, Chevrolet, or Volkswagen
2. **Enter Model** - Type the specific model name (e.g., Civic, Camry, 3 Series)
3. **Set Purchase Year** - Select when you purchased the car
4. **Input Mileage** - Enter the current mileage in kilometers
5. **Choose Condition** - Select from Excellent, Very Good, Good, Fair, or Poor
6. **Maintenance History** - Indicate how well maintained the car is
7. **Accident History** - Check if the car has been in accidents
8. **Click "Estimate Price"** - Get your fair selling price!

## Price Calculation Logic

The app uses a sophisticated multi-factor algorithm:

1. **Base Value**: Brand-specific starting price
2. **Age Depreciation**: Yearly depreciation rate based on brand
3. **Condition Factor**: Reduces value based on car condition
4. **Mileage Adjustment**: Accounts for wear and tear
5. **Maintenance Factor**: Increases/decreases value based on history
6. **Accident Penalty**: 20% reduction if accident history exists
7. **Model Premium**: Adds premium for sports/SUV models

## API Endpoints

### Get Available Brands
```
GET /api/brands
Response: { "brands": ["Toyota", "Honda", ...] }
```

### Get Car Conditions
```
GET /api/conditions
Response: { "conditions": ["Excellent", "Very Good", ...] }
```

### Estimate Car Price
```
POST /api/estimate
Body: {
  "brand": "Toyota",
  "model": "Camry",
  "year": 2018,
  "condition": "Good",
  "mileage": 75000,
  "maintenance_history": "Average",
  "accident_history": false
}

Response: {
  "estimated_price": 12500.50,
  "fair_min": 11250.45,
  "fair_max": 13750.55,
  "confidence": 0.85
}
```

## Browser Compatibility

- Chrome (Latest)
- Firefox (Latest)
- Safari (Latest)
- Edge (Latest)

## Technologies Used

### Backend
- Python 3.8+
- Flask 2.3.0
- Flask-CORS 4.0.0

### Frontend
- React 18
- Babel (for JSX transpilation)
- HTML5/CSS3
- Modern CSS animations

## Customization

You can customize the app by:

1. **Adding More Brands** - Edit `CAR_BRANDS` dictionary in `backend/app.py`
2. **Adjusting Depreciation** - Modify depreciation rates for each brand
3. **Changing Conditions** - Update `CONDITION_FACTORS` dictionary
4. **Styling** - Edit CSS in `frontend/index.html`
5. **Color Scheme** - Modify gradient colors in the CSS section

## Future Enhancements

- 📈 Historical price trends analysis
- 🗺️ Location-based pricing adjustments
- 🔄 Market comparison feature
- 💾 Save estimates history
- 📱 Mobile app version
- 🤖 ML-based price prediction
- 🔐 User authentication
- 💬 Chat support integration

## Performance Notes

- Average estimation time: < 100ms
- Frontend animations: 60 FPS
- Responsive design optimized for mobile

## Troubleshooting

**CORS Error?**
- Make sure the Flask backend is running on port 5000
- Ensure frontend is accessing `http://localhost:5000/api`

**No Brands Showing?**
- Check that the backend is running
- Open browser console for error messages
- Verify network requests in DevTools

**Animations Not Smooth?**
- Update your browser to the latest version
- Check GPU acceleration is enabled
- Disable browser extensions that might interfere

## License

This project is open source and available for educational and commercial use.

## Support

For issues, questions, or suggestions, please create an issue in the repository.

---

**Built with ❤️ for car enthusiasts**
