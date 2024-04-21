import { QueryParam } from '@/shared';

export const compileUrlPath = (
  url: string,
  queryParams?: QueryParam,
): string => {
  if (!queryParams) return url;

  if (Object.keys(queryParams).length > 0) {
    url += '?';
  }

  Object.entries(queryParams).forEach(([qn, qv]) => {
    url += `${qn}=${qv}&`;
  });
  return url;
};
