import { useState } from "react";

import { useLottoResultFilter } from "../hooks/useLottoResultFilter";
import Header from "../components/Header";

function HomePage() {
  const [date, setDate] = useState<string>("2026-10-24");
  const { data, isPending, error } = useLottoResultFilter({ start_date: date, end_date: date });

  if (isPending) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <section>
      <Header title="Home" />
      <ul>
        {data.map((lottoResult) => (
          <li key={lottoResult.id}>{lottoResult.game_name}</li>
        ))}
      </ul>
      <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
    </section>
  );
}

export default HomePage;
