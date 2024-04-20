import axios from 'axios';
import { RefreshResponse, SERVER_URL, User } from '..';

export const fetchUserByToken = async (access: string) => {
  return await axios
    .get<User | null>(`${SERVER_URL}/auth/user/`, {
      headers: { Authorization: `Bearer ${access}` },
    })
    .catch(() => {
      return null;
    });
};

export const refreshAccessToken = async (refresh: string) => {
  return await axios
    .post<RefreshResponse | null>(`${SERVER_URL}/auth/refresh/`, {
      refresh: refresh,
    })
    .catch(() => {
      return null;
    });
};
