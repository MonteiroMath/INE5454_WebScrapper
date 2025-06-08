type PriceEntry = {
  date: string;
  active_sale: boolean;
  old_price: string | null;
  price: string;
  loja: string;
};

type PriceList = PriceEntry[];

export default function sortPricesByDate(prices: PriceList): PriceList {
  const sortedPrices = [...prices];

  sortedPrices.sort((a, b) => {
    const dateA = new Date(a.date);
    const dateB = new Date(b.date);

    if (dateA < dateB) {
      return -1;
    }
    if (dateA > dateB) {
      return 1;
    }
    return 0;
  });

  return sortedPrices;
}
