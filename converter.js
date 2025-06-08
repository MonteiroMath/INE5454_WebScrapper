import { formatWithOptions } from "node:util";
import kabum from "./scrapper/data/kabum.js";
import fs from "node:fs";
// import pichau as data from "./scrapper/data/pichau"
// import gigantec as data from "./scrapper/data/gigantec"

const kabumMap = {};

kabum.forEach((product) => {
  if (Object.hasOwn(kabumMap, product.name)) {
    kabumMap[product.name].prices.push({
      date: product.date,
      active_sale: product.active_sale,
      old_price: product.old_price,
      price: product.price,
      loja: product.loja,
    });
  } else {
    kabumMap[product.name] = {
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
    "./data/kabum.json",
    JSON.stringify(Object.values(kabumMap))
  );
} catch (err) {
  console.error(err);
}
