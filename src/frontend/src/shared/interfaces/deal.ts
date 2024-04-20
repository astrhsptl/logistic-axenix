import { PaginatedResponse } from '..';

export interface DealCreate {
  quantity: number;
  id_sale_point: string;
  id_product: string;
}

export interface DealUpdate {
  quantity?: number;
  id_sale_point?: string;
  id_product?: string;
}

export interface Deal extends DealCreate {
  id: string;
}

export interface DealPaginated extends PaginatedResponse {
  results: Deal[];
}
