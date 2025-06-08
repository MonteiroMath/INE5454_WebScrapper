import { ProductDataList } from "@/types/types";
import kabumData from "@/data/kabum.json";
import ProductCard from "@/components/ProductCard";
import PaginationBar from "@/components/PaginationBar";

interface SearchParams {
  searchParams: Promise<{ page?: string }>;
}

const PAGE_SIZE = 20;

export default async function Home({ searchParams }: SearchParams) {
  const { page: rawPage } = await searchParams;
  let page = rawPage ? parseInt(rawPage) : 1;
  page = isNaN(page) || page < 1 ? 1 : page;

  const startIndex = (page - 1) * PAGE_SIZE;

  const displayData = (kabumData as ProductDataList).slice(
    startIndex,
    startIndex + PAGE_SIZE
  );

  return (
    <div className="container mx-auto px-8">
      <main className="w-full sm:w-7/12 md:w-9/12 mx-auto">
        <div
          className="w-full flex flex-col items-center gap-y-8
          sm:grid  sm:justify-items-center md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4"
        >
          {displayData.map((product, index) => (
            <ProductCard
              key={`product-${product.loja}=${index}`}
              productId={index + startIndex}
              product={product}
            />
          ))}
          <PaginationBar className="mt-6" currentPage={page} />
        </div>
      </main>
    </div>
  );
}
