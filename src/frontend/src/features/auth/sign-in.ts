import { CSI, SERVER_URL, TokenResponse } from '@/shared';
import axios from 'axios';

interface LoginData {
  username: string;
  password: string;
}

interface SignUpData {
  email: string;
  username: string;
  password: string;
}

export const useSignIn = async (credentials: LoginData) => {
  const tokens = await axios
    .post<TokenResponse | null>(`${SERVER_URL}/auth/login/`, credentials)
    .then(({ data }) => data)
    .catch(() => null);

  if (!tokens) {
    return null;
  }

  CSI.setCredential('access', tokens.access);
  CSI.setCredential('refresh', tokens.refresh);

  return tokens;
};

export const useSignUp = async (credentials: SignUpData) => {
  const tokens = await axios
    .post<TokenResponse | null>(`${SERVER_URL}/auth/register/`, credentials)
    .then(({ data }) => data)
    .catch(() => null);

  if (!tokens) {
    return null;
  }

  console.log(tokens);

  CSI.setCredential('access', tokens.access);
  CSI.setCredential('refresh', tokens.refresh);

  return tokens;
};
