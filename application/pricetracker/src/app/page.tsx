import Image from "next/image";
import { ProductDataList } from "@/types/types";
import * as kabumData from "@/data/kabum.json";

export default function Home() {
  return <div>{(kabumData as ProductDataList)[0].name}</div>;
}
