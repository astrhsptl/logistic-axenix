import { PaginatedResponse } from '..';

export interface CategoryCreate {
  name: string;
  description: string;
}

export interface CategoryUpdate {
  name?: string;
  description?: string;
}

export interface Category extends CategoryCreate {
  id: string;
}

export interface CategoryPaginated extends PaginatedResponse {
  results: Category[];
}
