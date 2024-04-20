import { PaginatedResponse } from '..';

export interface DriverCreate {
  first_name: string;
  last_name: string;
  phone: number;
  experience?: number;
  user_id?: number;
}

export interface DriverUpdate {
  first_name?: string;
  last_name?: string;
  phone?: number;
  experience?: number;
  user_id?: number;
}

export interface Driver extends DriverCreate {
  id: string;
}

export interface DriverPaginated extends PaginatedResponse {
  results: Driver[];
}
