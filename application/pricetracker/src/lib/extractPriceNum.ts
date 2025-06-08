export default function parseBRLToFloat(priceString: string): number {
  let cleanedString = priceString.replace("R$", "").trim();
  cleanedString = cleanedString.replace(",", ".");

  return parseFloat(cleanedString);
}
