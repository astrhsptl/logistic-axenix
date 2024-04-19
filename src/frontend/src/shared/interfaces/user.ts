import { PaginatedResponse } from '..';

export interface User {
  id: string;
  last_login: string;
  username: string;
  email: string;
  avatar: string;
  create_time: string;
  update_time: string;
  is_active: boolean;
  is_staff: boolean;
  is_superuser: boolean;
}

export interface UserPaginated extends PaginatedResponse {
  results: User[];
}
