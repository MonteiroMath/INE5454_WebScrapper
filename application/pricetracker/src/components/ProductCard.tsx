import Link from "next/link";
import Image from "next/image";

import { Card, CardContent, CardHeader } from "@/components/ui/card";

import { ProductData } from "@/types/types";

import ProductPlaceholder from "@/assets/placeholders/product.jpg";
import sortPricesByDate from "@/lib/orderByDate";

interface ProductCardProps extends React.HtmlHTMLAttributes<HTMLElement> {
  key: string;
  product: ProductData;
  productId: number;
}

export default function ProductCard({ product, productId }: ProductCardProps) {
  const sortedPrices = sortPricesByDate(product.prices);

  console.log(product.prices);
  return (
    <Card className="h-[400px] w-[250px]">
      <CardHeader>
        <Link href={`/products/${productId}`}>
          <div className="relative h-[150px] w-[200px]">
            <Image
              className="rounded-md"
              src={product.img || ProductPlaceholder}
              fill={true}
              sizes="200px"
              alt={`Image of product ${product.name}`}
            />
          </div>
        </Link>
      </CardHeader>
      <CardContent>
        <Link href={`/products/${productId}`}>
          <p className="h-14 typo-large overflow-hidden hover:text-muted-foreground">
            {product.name}
          </p>
        </Link>

        <p className="typo-p font-semibold">
          {sortedPrices.slice(-1)[0].price}
        </p>
      </CardContent>
    </Card>
  );
}
