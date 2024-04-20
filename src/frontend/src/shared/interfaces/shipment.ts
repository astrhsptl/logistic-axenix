import { PaginatedResponse } from '..';

export interface ShipmentCreate {
  name: string;
}

export interface ShipmentUpdate {
  name: string;
}

export interface Shipment extends ShipmentCreate {
  id: string;
}

export interface ShipmentPaginated extends PaginatedResponse {
  results: Shipment[];
}
