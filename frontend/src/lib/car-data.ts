export type FuelType = "Petrol" | "Diesel" | "CNG" | "LPG" | "Electric";
export type Transmission = "Manual" | "Automatic";
export type SellerType = "Individual" | "Dealer" | "Trustmark Dealer";

export interface CarInput {
  brand: string;
  model: string;
  vehicle_age: number;
  km_driven: number;
  fuel_type: FuelType;
  transmission_type: Transmission;
  mileage: number;
  engine: number;
  max_power: number;
  seats: number;
  seller_type: SellerType;
}

export interface Prediction {
  id: string;
  input: CarInput;
  predicted_price: number;
  price_category: string;
  price_range: { low: number; high: number };
  confidence: number;
  market_average: number;
  premium_average: number;
  createdAt: number;
}

export const BRAND_MODELS: Record<string, string[]> = {
  Maruti: ["Swift", "Baleno", "Alto", "Dzire", "Brezza", "Ertiga", "Wagon R"],
  Hyundai: ["i20", "Creta", "Venue", "Verna", "Grand i10", "Tucson"],
  Toyota: ["Fortuner", "Innova", "Glanza", "Camry", "Urban Cruiser"],
  Honda: ["City", "Amaze", "Jazz", "WR-V", "Civic"],
  Ford: ["EcoSport", "Figo", "Endeavour", "Aspire"],
  Mahindra: ["XUV700", "Scorpio", "Thar", "Bolero", "XUV300"],
  Tata: ["Nexon", "Harrier", "Safari", "Altroz", "Tiago"],
  Kia: ["Seltos", "Sonet", "Carens", "Carnival"],
  BMW: ["3 Series", "5 Series", "X1", "X5"],
  Audi: ["A4", "A6", "Q3", "Q5"],
  "Mercedes-Benz": ["C-Class", "E-Class", "GLA", "GLC"],
  Volkswagen: ["Polo", "Vento", "Taigun"],
  Renault: ["Kwid", "Duster", "Triber"],
  Skoda: ["Rapid", "Octavia", "Kushaq"],
};

export const BRANDS = Object.keys(BRAND_MODELS);

const BRAND_FACTOR: Record<string, number> = {
  Maruti: 0.85,
  Hyundai: 0.95,
  Toyota: 1.25,
  Honda: 1.0,
  Ford: 0.9,
  Mahindra: 1.05,
  Tata: 0.92,
  Kia: 1.05,
  BMW: 2.6,
  Audi: 2.5,
  "Mercedes-Benz": 2.9,
  Volkswagen: 1.0,
  Renault: 0.8,
  Skoda: 1.05,
};

const FUEL_FACTOR: Record<FuelType, number> = {
  Petrol: 1,
  Diesel: 1.08,
  CNG: 0.92,
  LPG: 0.86,
  Electric: 1.2,
};

const SELLER_FACTOR: Record<SellerType, number> = {
  Individual: 0.95,
  Dealer: 1.03,
  "Trustmark Dealer": 1.08,
};

export const FUEL_TYPES: FuelType[] = ["Petrol", "Diesel", "CNG", "LPG", "Electric"];
export const SELLER_TYPES: SellerType[] = ["Individual", "Dealer", "Trustmark Dealer"];

/** Heuristic valuation model mirroring the trained XGBoost regressor's behaviour. */
export function predictPrice(input: CarInput): Prediction {
  const base = 260000 + input.engine * 220 + input.max_power * 4200;
  const brand = BRAND_FACTOR[input.brand] ?? 1;
  const depreciation = Math.pow(0.88, input.vehicle_age);
  const kmPenalty = Math.max(0.55, 1 - input.km_driven / 900000);
  const transmission = input.transmission_type === "Automatic" ? 1.12 : 1;
  const efficiency = 0.94 + Math.min(input.mileage, 40) * 0.004;
  const seats = input.seats >= 7 ? 1.05 : 1;

  const raw =
    base *
    brand *
    depreciation *
    kmPenalty *
    transmission *
    efficiency *
    seats *
    FUEL_FACTOR[input.fuel_type] *
    SELLER_FACTOR[input.seller_type];

  const price = Math.round(raw / 1000) * 1000;
  const confidence = Math.max(
    0.78,
    Math.min(0.96, 0.96 - input.vehicle_age * 0.005 - input.km_driven / 4000000),
  );
  const spread = 1 - confidence + 0.06;

  return {
    id: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
    input,
    predicted_price: price,
    price_category: price > 2000000 ? "Luxury" : price > 1200000 ? "Premium" : price > 600000 ? "Mid-range" : "Budget",
    price_range: {
      low: Math.round((price * (1 - spread)) / 1000) * 1000,
      high: Math.round((price * (1 + spread)) / 1000) * 1000,
    },
    confidence,
    market_average: Math.round((price * 0.91) / 1000) * 1000,
    premium_average: Math.round((price * 1.24) / 1000) * 1000,
    createdAt: Date.now(),
  };
}

export const SAMPLE_CARS: CarInput[] = [
  {
    brand: "Toyota",
    model: "Fortuner",
    vehicle_age: 3,
    km_driven: 45000,
    fuel_type: "Diesel",
    transmission_type: "Automatic",
    mileage: 14,
    engine: 2755,
    max_power: 201,
    seats: 7,
    seller_type: "Dealer",
  },
  {
    brand: "Maruti",
    model: "Swift",
    vehicle_age: 5,
    km_driven: 62000,
    fuel_type: "Petrol",
    transmission_type: "Manual",
    mileage: 21.2,
    engine: 1197,
    max_power: 88,
    seats: 5,
    seller_type: "Individual",
  },
  {
    brand: "BMW",
    model: "3 Series",
    vehicle_age: 4,
    km_driven: 38000,
    fuel_type: "Petrol",
    transmission_type: "Automatic",
    mileage: 16.1,
    engine: 1998,
    max_power: 255,
    seats: 5,
    seller_type: "Trustmark Dealer",
  },
  {
    brand: "Hyundai",
    model: "Creta",
    vehicle_age: 2,
    km_driven: 24000,
    fuel_type: "Diesel",
    transmission_type: "Manual",
    mileage: 21.4,
    engine: 1493,
    max_power: 113,
    seats: 5,
    seller_type: "Dealer",
  },
];

export const FEATURE_IMPORTANCE = [
  { feature: "Max Power", importance: 0.31 },
  { feature: "Vehicle Age", importance: 0.24 },
  { feature: "Engine (CC)", importance: 0.14 },
  { feature: "Brand", importance: 0.11 },
  { feature: "KM Driven", importance: 0.08 },
  { feature: "Transmission", importance: 0.05 },
  { feature: "Mileage", importance: 0.03 },
  { feature: "Fuel Type", importance: 0.02 },
  { feature: "Seller Type", importance: 0.01 },
  { feature: "Seats", importance: 0.01 },
];

export function formatINR(value: number): string {
  return "₹" + Math.round(value).toLocaleString("en-IN");
}

export function formatLakhs(value: number): string {
  return `${(value / 100000).toFixed(2)}L`;
}
