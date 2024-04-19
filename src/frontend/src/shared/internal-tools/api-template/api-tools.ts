import { QueryParam } from '@/shared';

export const compileUrlPath = (
  url: string,
  queryParams?: QueryParam,
): string => {
  if (!queryParams) return url;

  if (Object.keys(queryParams).length > 0) {
    url += '?';
  }

  for (const [qn, qv] of Object.entries(queryParams)) url += `${qn}=${qv}`;

  return url;
};
