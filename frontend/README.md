# Frontend (React + TypeScript)

This frontend is the user interface for the CarCast used-car valuation app. It connects to the FastAPI backend and provides prediction, deal analysis, and prediction history in a clean single-page experience.

## Quick setup

```bash
cd frontend
npm install
npm run dev
```

## Environment variable

Set backend base URL in [.env](D:/Car-price-prediction-project.worktrees/car-price-prediction-documentation/frontend/.env):

```env
VITE_API_BASE_URL=http://localhost:8000
```

## Brief features

- Car price prediction from 11 user inputs
- Asking-price deal analysis
- Dynamic brand/model loading from backend APIs
- Basic API health/model readiness feedback
- Local prediction history for quick reuse
   - Searchable dropdown with icons

2. **Model** (Dropdown, filtered by brand)
   - Dynamic options based on selected brand
   - Searchable

3. **Vehicle Age** (Slider + Number Input)
   - Range: 0-30 years
   - Slider with tick marks
   - "New" vs "Used" indicator

4. **KM Driven** (Slider + Number Input)
   - Range: 0-1,000,000 km
   - Unit: "km"
   - Progress bar below slider

5. **Fuel Type** (Chip Selector)
   - Options: Petrol, Diesel, CNG, LPG, Electric
   - Visual icons for each

6. **Transmission** (Toggle/Chip Selector)
   - Options: Manual, Automatic
   - Animated toggle

7. **Mileage** (Number Input)
   - Unit: "km/l"
   - Min: 0, Max: 50

8. **Engine** (Number Input)
   - Unit: "CC"
   - Min: 0, Max: 8000

9. **Max Power** (Number Input)
   - Unit: "HP" or "bhp"
   - Min: 0, Max: 1000

10. **Seats** (Number Input)
    - Range: 1-10
    - +/- buttons for adjustment

11. **Seller Type** (Dropdown)
    - Options: Individual, Dealer, Trustmark Dealer

**Sample Data Button:**
- "Fill Sample Data" text with refresh icon
- On click: Populates all fields with realistic values
- Animated button with rotation

### 4. Results Section (Premium Design)

```jsx
// Appears with slide-up animation on prediction

// Price Card Design:
┌──────────────────────────────────────┐
│  💰 Estimated Fair Price             │
│                                      │
│        ₹18,75,000                    │  <- Large, animated counter
│                                      │
│        ₹16,80,000  -  ₹20,70,000     │  <- Price range
│                                      │
│        📊 Confidence: 95%            │  <- Confidence badge
│                                      │
│        ⏱️ Last updated: 2 min ago    │
└──────────────────────────────────────┘

// Price Breakdown Graph:
// Horizontal bar chart showing:
- Your Car's Price: $18.75L
- Average Market Price: $16.50L
- Premium Segment Average: $22.00L

// Deal Analyzer:
┌──────────────────────────────────────┐
│  💰 Deal Analyzer                    │
│                                      │
│  Asking Price: [________] (Input)    │
│                                      │
│  🟢 Good Deal!                       │
│  You could save ₹1,75,000            │
│  (Market price is ₹1,75,000 higher)  │
└──────────────────────────────────────┘
```

### 5. History Section

```jsx
// Horizontal scrollable cards or list

// Card Design:
┌────────────────────────────┐
│  🚗 Toyota Fortuner 2019   │
│  ₹18,75,000               │
│  📅 Jan 15, 2024           │
│  📊 View Details →         │
└────────────────────────────┘

// Features:
- Max 20 recent predictions
- Clear history button
- Click to re-run prediction
- Persist in localStorage
```

### 6. Data Science Behind Section

```jsx
// Two-column layout

// Left Column: Metrics Cards
┌─────────────┬─────────────┐
│  📊 R² Score │  📈 MAE     │
│  0.9459      │  ₹97,149   │
└─────────────┴─────────────┘
┌─────────────┐
│  🤖 Model   │
│  XGBoost    │
└─────────────┘

// Right Column: Feature Importance Graph
// Interactive bar chart showing top 10 features

// Section below:
// Jupyter Notebook Embed (iframe) or links to:
- GitHub Notebook Link
- Dataset Link
- Model Documentation
```

### 7. Chatbot Section

```jsx
// Floating chat bubble interface (bottom-right)

// Placeholder Design:
┌──────────────────────────────┐
│  💬 CarCast Assistant     │
│  "Coming Soon!"              │
│  Ask about car prices,      │
│  features, and more.         │
│                              │
│  [Quick Question 1]          │
│  [Quick Question 2]          │
│  [Quick Question 3]          │
└──────────────────────────────┘

// Quick Questions:
- "What factors affect car price?"
- "How accurate is the prediction?"
- "Tell me about the model"
```

---

## 🎬 Animations & Interactions

### Page Load Animations
- Fade-in for each section (staggered)
- Hero car floating animation (CSS)
- Counting numbers animation for stats

### Form Interactions
- Input focus: Gold border glow
- Dropdown: Smooth expand animation
- Slider: Smooth value change with live update
- Checkbox/Toggle: Spring animation
- Predict Button: Pulse animation on hover, loading state with dots

### Results Animations
- Price card: Slide-up from bottom
- Price number: Counting up animation
- Price range: Draw animation
- Confidence bar: Progress bar animation
- Graphs: Animate in from bottom

### Scroll Animations
- Elements fade in on scroll (Intersection Observer)
- Parallax effect on hero section
- Sticky navigation bar

### Micro-Interactions
- Hover effects on cards (slight lift + shadow)
- Button click ripple effect
- Input validation: Green/Red border with icon
- Success animation: Confetti or particles on first prediction

---

## 📱 Responsive Design

### Breakpoints
- Desktop: > 1024px
- Tablet: 768px - 1024px
- Mobile: < 768px

### Mobile Adaptations
- Single column layout
- Reduced font sizes
- Touch-optimized inputs
- Bottom navigation bar
- Collapsible sections

---

## 🔧 Tech Stack (Frontend)

```json
{
  "framework": "React 18+",
  "language": "TypeScript",
  "styling": "Tailwind CSS + CSS Modules",
  "animations": "Framer Motion",
  "state": "Zustand or Context API",
  "forms": "React Hook Form + Zod",
  "charts": "Chart.js or Recharts",
  "icons": "Lucide React or Font Awesome",
  "notifications": "React Toastify",
  "routing": "React Router v6",
  "http": "Axios",
  "ui": "Custom components (no UI library)",
  "deployment": "Vercel"
}
```

---

## 📁 Recommended File Structure

```
src/
├── components/
│   ├── layout/
│   │   ├── Navbar.jsx
│   │   ├── Footer.jsx
│   │   └── Layout.jsx
│   ├── sections/
│   │   ├── Hero.jsx
│   │   ├── Features.jsx
│   │   ├── PredictionForm.jsx
│   │   ├── Results.jsx
│   │   ├── DealAnalyzer.jsx
│   │   ├── History.jsx
│   │   ├── DataScience.jsx
│   │   └── Chatbot.jsx
│   ├── ui/
│   │   ├── Button.jsx
│   │   ├── Input.jsx
│   │   ├── Dropdown.jsx
│   │   ├── Slider.jsx
│   │   ├── Card.jsx
│   │   ├── Badge.jsx
│   │   └── Toggle.jsx
│   └── charts/
│       ├── PriceBreakdown.jsx
│       └── FeatureImportance.jsx
├── hooks/
│   ├── useScrollAnimation.js
│   ├── useLocalStorage.js
│   └── usePrediction.js
├── services/
│   └── api.js
├── utils/
│   ├── constants.js
│   ├── formatters.js
│   └── validators.js
├── contexts/
│   └── PredictionContext.jsx
├── styles/
│   └── globals.css
├── App.jsx
├── index.jsx
└── routes.jsx
```

---

## 🧩 Key Components Code Structure

### PredictionForm.jsx

```jsx
import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { motion } from 'framer-motion';
import { Slider, Dropdown, Toggle, Button } from '../ui';

const PredictionForm = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [brands, setBrands] = useState([]);
  const [models, setModels] = useState([]);

  const fillSampleData = () => {
    // Populate form with sample car data
  };

  const onSubmit = async (data) => {
    setIsLoading(true);
    // API call
    setIsLoading(false);
  };

  return (
    
      {/* Form fields */}
      

        {/* Brand */}
        
        {/* Model */}
        
        {/* ... rest of fields */}
      


      

        
          Fill Sample Data
        
        
          Predict Price
        
      

    
  );
};
```

### Results.jsx

```jsx
import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import CountUp from 'react-countup';

const Results = ({ prediction }) => {
  if (!prediction) return null;

  return (
    
      
        {/* Price Display */}
        

          

            Estimated Fair Price
          

          

            ₹
          

          

            ₹{prediction.minPrice} - ₹{prediction.maxPrice}
          

        


        {/* Price Range Bar */}
        

          {/* Range slider visualization */}
        


        {/* Deal Analyzer */}
        

          {/* Asking price input and analysis */}
        

      
    
  );
};
```

---

## 📊 Assets Required

### Images (PNG/SVG)
- Car silhouette (multiple angles)
- Logo (combined car + text)
- Hero background pattern
- Feature icons (car, graph, lightning, shield)
- Social share images
- Favicon

### Animations
- Lottie files for:
  - Loading state
  - Success state
  - Car driving animation
  - Confetti/celebration

### Fonts
- Playfair Display (Google Fonts)
- Inter (Google Fonts)
- DM Sans (Google Fonts)

---

## 🌟 Bonus Features (If Time Permits)

1. **Share Results**
   - Twitter/X share
   - WhatsApp share
   - Link copy

2. **Email Report**
   - Send prediction to email
   - PDF report generation

3. **Compare Cars**
   - Compare two cars side by side

4. **Market Trends**
   - Price trend graphs by brand/model

5. **Dark Mode**
   - Elegant dark version with warm tones

6. **Keyboard Shortcuts**
   - Tab navigation
   - Enter to submit

---

## 🔗 Links to Include

### Footer/Header
- GitHub: `https://github.com/yourusername/used-car-price-prediction`
- LinkedIn: `https://linkedin.com/in/yourprofile`
- Dataset: Link to Cardekho dataset
- Notebooks: Link to GitHub notebooks

### Data Science Section
- Jupyter Notebooks (GitHub links)
- Model Performance Report
- Feature Engineering Documentation

---

## 📝 Success Criteria

- [ ] No blue/violet colors used
- [ ] Responsive on all devices
- [ ] Smooth animations throughout
- [ ] Form validation with clear errors
- [ ] Sample data button works
- [ ] Prediction displays with animation
- [ ] Price range shows confidence interval
- [ ] Deal analyzer works
- [ ] History persists in localStorage
- [ ] Graphs render correctly
- [ ] All links functional
- [ ] Loading states present
- [ ] GitHub link visible
- [ ] Developer info visible
- [ ] Professional typography
- [ ] Premium visual design

---

## 🚀 Getting Started Command

```bash
# Create React app with TypeScript
npx create-react-app car-price-ai --template typescript

# Install dependencies
npm install framer-motion react-hook-form react-router-dom \
  axios chart.js react-chartjs-2 react-countup \
  lucide-react tailwindcss @tailwindcss/forms

# Start development server
npm start
```

---

## 📝 Notes for Developer

1. **API Integration:**
   - Base URL: `http://localhost:8000`
   - Endpoint: `/predict`
   - Method: POST
   - Content-Type: `application/json`

2. **Sample Request:**
```json
{
  "brand": "Toyota",
  "model": "Fortuner",
  "vehicle_age": 3,
  "km_driven": 45000,
  "fuel_type": "Diesel",
  "transmission_type": "Automatic",
  "mileage": 14.0,
  "engine": 2755,
  "max_power": 201.0,
  "seats": 7,
  "seller_type": "Dealer"
}
```

3. **Sample Response:**
```json
{
  "predicted_price": 1875000,
  "predicted_price_lakhs": 18.75,
  "price_category": "Premium",
  "price_range": {
    "low": 1687500,
    "high": 2062500
  },
  "confidence": 0.92
}
```

---

## 📌 Final Notes

1. Use **warm, earthy tones** throughout
2. **Animations should feel premium**, not cheap
3. **Typography is key** - use serif for headings
4. **Spacing should be generous** for readability
5. **Mobile-first design** approach
6. **Accessibility** is important (ARIA labels, keyboard navigation)
7. **Performance** should be optimized (lazy loading, code splitting)

This prompt should give any React developer everything they need to build the frontend. The key is the **premium, warm design** without blue/violet colors! 🎨✨

This project was built with [Lovable](https://lovable.dev).

## Build with Lovable

Continue developing this project in the [Lovable editor](https://lovable.dev/projects/c75490e0-3c81-4b68-b5b3-816fbed3a269).

- **Ship faster**: describe what you want to build and Lovable handles the code.
- **Stay in sync**: every change made in Lovable is committed straight to this repository.
- **Full ownership**: this code is yours. Push to `main` on GitHub and your changes sync back into Lovable, ready for your next prompt.

## Development

Prefer working locally? You need Node.js and npm — [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating).

```sh
git clone <this-repository-url>
cd <repository-name>
npm i
npm run dev
```
