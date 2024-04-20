import { PaginatedResponse } from '..';

export interface WareHouseCreate {
  name: string;
  address: string;
  volume: number;
  is_provider?: boolean;
  lon: number;
  lat: number;
}

export interface WareHouseUpdate {
  name?: string;
  address?: string;
  volume?: number;
  is_provider?: boolean;
  lon?: number;
  lat?: number;
}

export interface WareHouse extends WareHouseCreate {
  id: string;
}

export interface WareHousePaginated extends PaginatedResponse {
  results: WareHouse[];
}
