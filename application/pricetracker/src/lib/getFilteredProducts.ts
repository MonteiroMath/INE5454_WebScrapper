import productData from "@/data/products.json";
import { ProductDataList } from "@/types/types";

export default function getFilteredProducts() {
  return (productData as ProductDataList).filter((product) => {
    return product.prices.some((priceObj) => priceObj.price !== null);
  });
}
