import { CSI } from '..';
import { fetchUserByToken, refreshAccessToken } from './api';

export const useRefreshToken = async () => {
  const refreshToken = CSI.getCredential('refresh');

  if (!refreshToken) {
    return;
  }

  refreshAccessToken(refreshToken)
    .then((data) => {
      if (data && data.data) {
        CSI.setCredential('access', data?.data?.access);
      }
      return;
    })
    .catch(() => {
      return;
    });
};

export const useAuthentication = async () => {
  const accessToken = CSI.getCredential('access');
  console.log(accessToken);

  if (!accessToken) {
    return;
  }

  const data = fetchUserByToken(accessToken)
    .then((user) => {
      return user;
    })
    .catch(async () => {
      return await useRefreshToken();
    });

  return data;
};
