export type ProductDataList = {
  name: string;
  loja: "kabum" | "pichau" | "gigantec";
  img: string;
  url: string;
  prices: {
    date: string;
    active_sale: boolean;
    old_price: string;
    price: string;
    loja: string;
  }[];
}[];
