import fs from "node:fs";
import products from "./scrapper/data/products.js";

const productMap = {};



const shuffledProducts = products
  .map((value) => ({ value, sort: Math.random() }))
  .sort((a, b) => a.sort - b.sort)
  .map(({ value }) => value);

shuffledProducts.forEach((product) => {
  if (Object.hasOwn(productMap, product.name)) {
    productMap[product.name].prices.push({
      date: product.date,
      active_sale: product.active_sale,
      old_price: product.old_price,
      price: product.price,
      loja: product.loja,
    });
  } else {
    productMap[product.name] = {
      name: product.name,
      loja: product.loja,
      img: product.img,
      url: product.url,
      prices: [
        {
          date: product.date,
          active_sale: product.active_sale,
          old_price: product.old_price,
          price: product.price,
          loja: product.loja,
        },
      ],
    };
  }
});

try {
  fs.writeFileSync(
    "./data/products.json",
    JSON.stringify(Object.values(productMap))
  );
} catch (err) {
  console.error(err);
}
