import { Badge } from "@/components/ui/badge";
import { ProductImage } from "@/components/ProductImage";
import getFilteredProducts from "@/lib/getFilteredProducts";
import { ProductPriceChart } from "@/components/PriceChart";
import sortPricesByDate from "@/lib/orderByDate";

interface ProductDetailsParams {
  id: string;
}

const productData = getFilteredProducts();

async function ProductDetailsPage({
  params,
}: {
  params: Promise<ProductDetailsParams>;
}) {
  const { id } = await params;

  const product = productData[parseInt(id)];
  const sortedPrices = sortPricesByDate(product.prices);

  return (
    <main className="container mx-auto px-5">
      <div className="mt-8 sm:flex sm:justify-center sm:gap-x-12 md:gap-x-10 xl:gap-x-10">
        <ProductImage
          imageUrl={product.img}
          imageContainerClassname="h-[300px] w-auto sm:w-1/2 sm:h-[250px] lg:h-[300px] xl:w-1/3"
        />

        <section className="mt-5 sm:mt-0 ">
          <h1 className="typo-h3">{product.name}</h1>
          <Badge className="mt-5" variant="secondary">
            {product.loja}
          </Badge>
          <div className="typo-p font-bold">
            {sortedPrices.slice(-1)[0].price}
          </div>

          <ProductPriceChart className="mt-5" prices={sortedPrices} />
        </section>
      </div>
    </main>
  );
}

export default ProductDetailsPage;
