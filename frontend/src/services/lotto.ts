import { api } from "../lib/api";

export type LottoResult = {
  id: number;
  game_name: string;
  draw_date: string;
  combination: string;
  prize_pool: string;
  amount_of_winners: string;
};

export type GetLottoResultByGameAndDateRangeParams = {
  game_name?: string;
  start_date?: string;
  end_date?: string;
};

export async function getAllLottoResults(): Promise<LottoResult[]> {
  const res = await api.get<LottoResult[]>("/lotto/lotto-results");
  return res.data;
}

export async function getLottoResultByGameAndDateRange(
  params?: GetLottoResultByGameAndDateRangeParams,
  signal?: AbortSignal,
): Promise<LottoResult[]> {
  const res = await api.get<LottoResult[]>("/lotto/lotto-results/filter", { params, signal });
  return res.data;
}
