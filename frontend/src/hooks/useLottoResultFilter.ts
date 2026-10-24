import { useQuery } from "@tanstack/react-query";
import {
  getLottoResultByGameAndDateRange,
  type GetLottoResultByGameAndDateRangeParams,
} from "../services/lotto";

export function useLottoResultFilter(params?: GetLottoResultByGameAndDateRangeParams) {
  return useQuery({
    queryKey: ["lottoResults", params],
    queryFn: ({ signal }) => getLottoResultByGameAndDateRange(params, signal),
  });
}
