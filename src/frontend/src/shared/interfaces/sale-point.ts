import { PaginatedResponse } from '..';

export interface SalePointCreate {
  name: string;
  address: string;
  volume: number;
  lon: number;
  lat: number;
}

export interface SalePointUpdate {
  name?: string;
  address?: string;
  volume?: number;
  lon?: number;
  lat?: number;
}

export interface SalePoint extends SalePointCreate {
  id: string;
}

export interface SalePointPaginated extends PaginatedResponse {
  results: SalePoint[];
}
