export type ApiRootResponse = {
  name: string;
  version: string;
  description: string;
  docs: string;
  redoc: string;
  health: string;
  endpoints: Record<string, string>;
};

export type HealthResponse = {
  status: string;
  model_loaded: boolean;
  api_version: string;
  uptime: number | null;
};

export type ModelMetrics = {
  model_name: string;
  r2_score: number;
  mae: number;
  rmse: number;
  training_samples: number;
  test_samples: number;
  features_count: number;
  description: string;
};

export type ModelInfoResponse = {
  model_type: string;
  is_loaded: boolean;
  features_used: {
    categorical: string[];
    numerical: string[];
  };
  model_metrics: ModelMetrics;
};

export type BootstrapData = {
  apiInfo: ApiRootResponse;
  health: HealthResponse;
  modelInfo: ModelInfoResponse;
};

export type BrandModelsResponse = {
  models: string[];
};

export type PredictResponse = {
  predicted_price: number;
  predicted_price_lakhs: number;
  price_category: string;
  price_range: {
    low: number;
    high: number;
  };
  confidence_score: number;
  timestamp: string;
};

export type PredictWithAskingResponse = PredictResponse & {
  asking_price: number;
  price_difference: number;
  deal_status: string;
  deal_message: string;
  savings: number;
};

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8000").replace(
  /\/+$/,
  "",
);

async function fetchJson<T>(path: string, init?: RequestInit): Promise<T> {
  const normalizedPath = path.startsWith("/") ? path : `/${path}`;
  const response = await fetch(`${API_BASE_URL}${normalizedPath}`, init);

  if (!response.ok) {
    throw new Error(`Request to ${normalizedPath} failed with ${response.status} ${response.statusText}`);
  }

  return (await response.json()) as T;
}

export async function fetchBootstrapData(): Promise<BootstrapData> {
  const [apiInfo, health, modelInfo] = await Promise.all([
    fetchJson<ApiRootResponse>("/"),
    fetchJson<HealthResponse>("/health"),
    fetchJson<ModelInfoResponse>("/model-info"),
  ]);

  return { apiInfo, health, modelInfo };
}

export function isModelReady(health: HealthResponse): boolean {
  return health.status === "OK" && health.model_loaded;
}

export async function fetchBrands(): Promise<string[]> {
  return fetchJson<string[]>("/brands");
}

export async function fetchBrandModels(brand: string): Promise<string[]> {
  const encodedBrand = encodeURIComponent(brand);
  const response = await fetchJson<BrandModelsResponse>(`/brands/${encodedBrand}/models`);
  return response.models;
}

export async function predictCar(payload: {
  brand: string;
  model: string;
  vehicle_age: number;
  km_driven: number;
  fuel_type: string;
  transmission_type: string;
  mileage: number;
  engine: number;
  max_power: number;
  seats: number;
  seller_type: string;
}): Promise<PredictResponse> {
  return fetchJson<PredictResponse>("/predict", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(payload),
  });
}

export async function predictCarWithAsking(payload: {
  brand: string;
  model: string;
  vehicle_age: number;
  km_driven: number;
  fuel_type: string;
  transmission_type: string;
  mileage: number;
  engine: number;
  max_power: number;
  seats: number;
  seller_type: string;
  asking_price: number;
}): Promise<PredictWithAskingResponse> {
  return fetchJson<PredictWithAskingResponse>("/predict-with-asking", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(payload),
  });
}
