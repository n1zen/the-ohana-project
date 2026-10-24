import { useState } from "react";

import { useLottoResultFilter } from "../hooks/useLottoResultFilter";
import Header from "../components/Header";

function HomePage() {
  const [startDate, setStartDate] = useState<string>("2026-10-23");
  const { data, isPending, error } = useLottoResultFilter({ start_date: startDate });

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
    </section>
  );
}

export default HomePage;
