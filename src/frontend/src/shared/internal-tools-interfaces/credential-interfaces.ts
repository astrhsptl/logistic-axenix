export interface CredentialOptions {
  expires?: Date | string;
  maxAge?: number;
  secure?: boolean;
  samesite?: 'strict' | 'lax';

  httpOnly?: boolean;
}

export interface CredentialStorageInterface {
  setCredential(key: string, value: string, options: CredentialOptions): void;
  getCredential(key: string): string | null | undefined;
  removeCredential(key: string): void;
  invalidate(): void;
}
