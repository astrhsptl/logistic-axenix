import { PaginatedResponse } from '..';

export interface ProductCreate {
  name: string;
  cost: number;
  volume: number;
  weight: number;
  expiration_date: string;
  product_quantity: number;
  id_category: string;
  id_shipment: string;
  id_sale_point: string;
  id_warehouse: string;
}

export interface ProductUpdate {
  name?: string;
  cost?: number;
  volume?: number;
  weight?: number;
  expiration_date?: string;
  product_quantity?: number;
  id_category?: string;
  id_shipment?: string;
  id_sale_point?: string;
  id_warehouse?: string;
}

export interface Product extends ProductCreate {
  id: string;
}

export interface ProductPaginated extends PaginatedResponse {
  results: Product[];
}
