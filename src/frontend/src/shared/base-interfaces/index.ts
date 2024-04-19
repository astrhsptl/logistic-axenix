export type EntityId = number | string;

export interface BaseEntity {
  id: EntityId;
}

export interface TokenResponse {
  access: string;
  refresh: string;
}

export interface RefreshResponse {
  access: string;
}

export interface PaginatedResponse {
  count: number;
  next: string;
  previous: string;
}
