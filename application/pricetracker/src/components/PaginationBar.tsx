import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";

interface PaginationBarProps extends React.HtmlHTMLAttributes<HTMLElement> {
  currentPage: number;
}

function buildPaginationUrl(pageNum: number) {
  return `http://localhost:3000?page=${pageNum}`;
}

const MAX_PAGINATION_BUTTONS = 3;
const totalPages = 100;

function PaginationBar({ className, currentPage }: PaginationBarProps) {
  // check if there is a previous and a next page
  const hasPrev = currentPage > 1;
  const hasNext = currentPage < totalPages;

  // calculate how many pages there are before and after the current page
  const pagesBefore = currentPage - 1;
  const pagesAfter = totalPages - currentPage;

  // prepare up to MAX_PAGINATION_BUTTON pagination items for previous pages
  const previousPaginationItems = Array.from({
    length: Math.min(pagesBefore, MAX_PAGINATION_BUTTONS),
  })
    .map((val, index) => {
      const pageNum = currentPage - 1 * (index + 1);

      return (
        <PaginationItem key={`prev-pagination-item-${index}`}>
          <PaginationLink href={buildPaginationUrl(pageNum)}>
            {pageNum}
          </PaginationLink>
        </PaginationItem>
      );
    })
    .reverse();

  // prepare up to MAX_PAGINATION_BUTTON pagination items for next pages
  const nextPaginationItems = Array.from({
    length: Math.min(pagesAfter, MAX_PAGINATION_BUTTONS),
  }).map((val, index) => {
    const pageNum = currentPage + 1 * (index + 1);
    return (
      <PaginationItem key={`next-pagination-item-${index}`}>
        <PaginationLink href={buildPaginationUrl(pageNum)}>
          {pageNum}
        </PaginationLink>
      </PaginationItem>
    );
  });

  return (
    <Pagination className={className}>
      <PaginationContent>
        {/* Previous Pagination Button*/}
        <PaginationItem>
          <PaginationPrevious
            aria-disabled={!hasPrev}
            tabIndex={!hasPrev ? -1 : undefined}
            className={!hasPrev ? "pointer-events-none opacity-50" : undefined}
            href={buildPaginationUrl(currentPage - 1)}
          />
        </PaginationItem>

        {/* Ellipsis if needed */}
        {pagesBefore > 3 && (
          <PaginationItem>
            <PaginationEllipsis />
          </PaginationItem>
        )}

        {/* Pagination links for previous pages */}
        {previousPaginationItems}

        {/* Pagination button for current page */}
        <PaginationItem>
          <PaginationLink
            aria-disabled={true}
            className={"pointer-events-none opacity-50"}
            href="#"
          >
            {currentPage}
          </PaginationLink>
        </PaginationItem>

        {/* Pagination links for next pages */}
        {nextPaginationItems}

        {/* Ellipsis if needed */}
        {pagesAfter > 3 && (
          <PaginationItem>
            <PaginationEllipsis />
          </PaginationItem>
        )}

        {/* Pagination button for next page */}
        <PaginationItem>
          <PaginationNext
            aria-disabled={!hasNext}
            tabIndex={!hasNext ? -1 : undefined}
            className={!hasNext ? "pointer-events-none opacity-50" : undefined}
            href={buildPaginationUrl(currentPage + 1)}
          />
        </PaginationItem>
      </PaginationContent>
    </Pagination>
  );
}

export default PaginationBar;
