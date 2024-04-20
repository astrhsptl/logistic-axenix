import { PaginatedResponse } from '..';

export interface RouteOrderCreate {
  order_position: number;
  complited: boolean;
  id_warehouse: string;
  id_salepoint: string;
  id_route: string;
}

export interface RouteOrderUpdate {
  order_position?: number;
  complited?: boolean;
  id_warehouse?: string;
  id_salepoint?: string;
  id_route?: string;
}

export interface RouteOrder extends RouteOrderCreate {
  id: string;
}

export interface RouteOrderPaginated extends PaginatedResponse {
  results: RouteOrder[];
}
