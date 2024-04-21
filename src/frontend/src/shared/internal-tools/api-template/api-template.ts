import { QueryParam } from '@/shared';
import { EntityId } from '@/shared/base-interfaces';
import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';
import { compileUrlPath } from './api-tools';

export class APITemplate {
  private url;

  constructor(url: string) {
    this.url = `https://api.labofdev.ru/api/v1/${url}/`;
  }

  async fetchAll<FetchType>(
    queryParams?: QueryParam,
    RequestConfig?: AxiosRequestConfig,
  ): Promise<FetchType> {
    const url = compileUrlPath(this.url, queryParams);
    const data: AxiosResponse<FetchType> = await axios
      .get(url, RequestConfig)
      .catch(() => []);

    return data.data;
  }

  async fetchByID<FetchType>(id: EntityId, RequestConfig?: AxiosRequestConfig) {
    const url = `${this.url}${id}`;
    return await axios.get<FetchType>(url, RequestConfig);
  }

  async create<FetchType, FetchTypeRequest>(
    data: FetchTypeRequest,
    RequestConfig?: AxiosRequestConfig,
  ) {
    return await axios.post<FetchType>(this.url, data, RequestConfig);
  }

  async update<FetchType, FetchTypeRequest>(
    id: EntityId,
    data: FetchTypeRequest,
    RequestConfig?: AxiosRequestConfig,
  ) {
    const url = `${this.url}${id}`;
    return await axios.patch<FetchType>(url, data, RequestConfig);
  }

  async remove<FetchType>(id: EntityId, RequestConfig?: AxiosRequestConfig) {
    const url = `${this.url}${id}`;
    return await axios.delete<FetchType>(url, RequestConfig);
  }
}
