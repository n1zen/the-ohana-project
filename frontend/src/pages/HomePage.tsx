import { useState } from "react";

import { useLottoResultFilter } from "../hooks/useLottoResultFilter";
import Header from "../components/Header";
import LottoResultCard from "../components/LottoResultCard";

function HomePage() {
  const [date, setDate] = useState<string>("2026-10-24");
  const { data, isPending, error } = useLottoResultFilter({ start_date: date, end_date: date });

  if (isPending) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <section>
      <Header title="Home" />
      <div className="p-4">
        <section className="mb-3">
          <label>Date: </label>
          <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
        </section>
        <section className="flex flex-wrap gap-4">
          {data.map((lottoResult) => (
            <LottoResultCard
              key={lottoResult.id}
              id={lottoResult.id}
              game_name={lottoResult.game_name}
              draw_date={lottoResult.draw_date}
              combination={lottoResult.combination}
              prize_pool={lottoResult.prize_pool}
              amount_of_winners={lottoResult.amount_of_winners}
            />
          ))}
        </section>
      </div>
    </section>
  );
}

export default HomePage;
