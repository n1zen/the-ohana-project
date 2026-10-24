import { type LottoResult } from "../services/lotto";

type InfoProps = {
  name: string;
  value: string;
};
function Info(props: InfoProps) {
  return (
    <div>
      {props.name === "winners" && <span className="text-md">Winners: </span>}
      <span className="text-md font-semibold">
        {props.name === "prize" && "Php"} {props.value}
      </span>
    </div>
  );
}

function LottoResultCard(data: LottoResult) {
  return (
    <div className="border border-mist-500 rounded-lg min-w-64 flex-col">
      <div className="bg-sky-300 border-b rounded-t-lg border-mist-500 flex-col text-center p-2">
        <h2 className="text-lg font-bold text-mist-900">{data.game_name}</h2>
        <p className="text-sm font-regular text-mist-700">{data.draw_date}</p>
      </div>
      <div className="bg-white rounded-b-lg text-center p-2">
        <Info name="" value={data.combination} />
        <Info name="prize" value={data.prize_pool} />
        <Info name="winners" value={data.amount_of_winners} />
      </div>
    </div>
  );
}

export default LottoResultCard;
