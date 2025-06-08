import Image from "next/image";
import ProductPlaceholder from "@/assets/placeholders/product.jpg";

interface ProductImageProps extends React.HtmlHTMLAttributes<HTMLElement> {
  imageUrl: string | null;
  imageContainerClassname: string;
  altText?: string;
}

export function ProductImage({
  imageUrl,
  imageContainerClassname,
  altText = "Product Image",
}: ProductImageProps) {
  return (
    <div className={`relative ${imageContainerClassname}`}>
      <Image
        className="object-contain rounded-md"
        src={imageUrl || ProductPlaceholder}
        alt={altText}
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        fill={true}
      />
    </div>
  );
}
