import { type LottoResult } from '../services/lotto';

function LottoResultCard(data: LottoResult) {
    return(
        <div className="border border-mist-500 rounded-lg">
            <div className="bg-sky-300 border border-b-mist-500">
                <h2 className="font-bold text-mist-900">{data.game_name}</h2>
                <p className="font-regular text-mist-500">{data.id} | {data.draw_date}</p>
            </div>
            <div className="bg-white">
                <h3 className="font-semibold text-mist-900">{data.combination}</h3>
                <h3 className="font-semibold text-mist-900">{data.prize_pool}</h3>
                <h3 className="font-semibold text-mist-900">{data.amount_of_winners}</h3>
            </div>
        </div>
    );
}

export default LottoResultCard;