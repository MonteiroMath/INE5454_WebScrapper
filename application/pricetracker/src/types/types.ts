export type ProductDataList = ProductData[];

export type ProductData = {
  name: string;
  loja: string;
  img: string;
  url: string;
  prices: {
    date: string;
    active_sale: boolean;
    old_price: string | null;
    price: string;
    loja: string;
  }[];
};
