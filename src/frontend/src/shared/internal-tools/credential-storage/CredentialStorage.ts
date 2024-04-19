import { CredentialOptions, CredentialStorageInterface } from '@/shared';

class CredentialStorage implements CredentialStorageInterface {
  getCredentials() {
    const cookies = document.cookie
      .split('; ')
      .map((cookString) => cookString.split('='));
    let data = {};

    cookies.forEach((cookie) => {
      data = { ...data, ...{ [cookie[0]]: cookie[1] } };
    });

    return data;
  }

  setCredential(
    key: string,
    value: string,
    options: CredentialOptions = {},
  ): void {
    if (options && options.expires instanceof Date) {
      options.expires = options.expires.toUTCString();
    }

    let updatedCookie = `${encodeURIComponent(key)}=${encodeURIComponent(value)}; path=/;`;

    for (let [optionKey, optionValue] of Object.entries(options)) {
      if (optionKey === 'maxAge') {
        optionKey = 'max-age';
      }

      updatedCookie += '; ' + optionKey;

      if (optionValue !== true) {
        updatedCookie += '=' + optionValue;
      }
    }

    document.cookie = updatedCookie;
  }

  getCredential(key: string): string | null | undefined {
    const matches = document.cookie.match(
      new RegExp(
        '(?:^|; )' +
          key.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') +
          '=([^;]*)',
      ),
    );
    return matches ? decodeURIComponent(matches[1]) : undefined;
  }

  removeCredential(key: string): void {
    this.setCredential(key, '', {
      maxAge: -1,
    });
  }

  invalidate(): void {
    const cookies = this.getCredentials();
    console.log(cookies);

    Object.keys(cookies).forEach((el) => {
      this.removeCredential(el);
    });
  }
}

export const CSI = new CredentialStorage();
