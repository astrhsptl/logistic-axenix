import { QueryParam } from '@/shared';
import { EntityId } from '@/shared/base-interfaces';
import { AxiosRequestConfig } from 'axios';
import { APITemplate } from './api-template';

export class APIFactory {
  private url: string;

  constructor(baseUrl: string, urlPrefix: string) {
    this.url = baseUrl + urlPrefix;
  }

  getRequests<FetchType, FetchTypeRequest>() {
    const { fetchAll, fetchByID, create, update, remove } = new APITemplate(
      this.url,
    );

    return {
      fetchAll: async (
        queryParams?: QueryParam,
        RequestConfig?: AxiosRequestConfig,
      ) => fetchAll<FetchType>(queryParams, RequestConfig),

      fetchById: async (id: EntityId, RequestConfig?: AxiosRequestConfig) =>
        fetchByID<FetchType>(id, RequestConfig),

      create: async (
        data: FetchTypeRequest,
        RequestConfig?: AxiosRequestConfig,
      ) => create<FetchType, FetchTypeRequest>(data, RequestConfig),

      update: async (
        id: EntityId,
        data: FetchTypeRequest,
        RequestConfig?: AxiosRequestConfig,
      ) => update<FetchType, FetchTypeRequest>(id, data, RequestConfig),

      remove: async (id: EntityId, RequestConfig?: AxiosRequestConfig) =>
        remove<FetchType>(id, RequestConfig),
    };
  }
}
