import { PaginatedResponse } from '..';

export interface DriverRouteCreate {
  driver_id: string;
}

export interface DriverRouteUpdate {
  driver_id: string;
}

export interface DriverRoute extends DriverRouteCreate {
  id: string;
}

export interface DriverRoutePaginated extends PaginatedResponse {
  results: DriverRoute[];
}
