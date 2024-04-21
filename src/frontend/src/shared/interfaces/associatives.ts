import { PaginatedResponse } from '..';

export interface AssociativesCreate {
  distance: number;
  duration: number;
  id_warehouse_from: string;
  id_warehouse_to: string;
  id_sale_point_from: string;
  id_sale_point_to: string;
}

export interface AssociativesUpdate {
  distance?: number;
  duration?: number;
  id_warehouse_from?: string;
  id_warehouse_to?: string;
  id_sale_point_from?: string;
  id_sale_point_to?: string;
}

export interface Associatives extends AssociativesCreate {
  id: string;
}

export interface AssociativesPaginated extends PaginatedResponse {
  results: Associatives[];
}
