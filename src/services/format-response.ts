import ApiResponse from '../types/api-response';

export default function buildApiResponse(msg: string, payload?: any): ApiResponse {
  return {
    payload,
    msg,
  };
}
