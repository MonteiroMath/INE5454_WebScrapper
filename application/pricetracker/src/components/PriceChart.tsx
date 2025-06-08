"use client";

import { CartesianGrid, Line, LineChart, XAxis } from "recharts";

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart";
import parseBRLToFloat from "@/lib/extractPriceNum";

const chartConfig = {
  price: {
    label: "price",
    color: "var(--chart-1)",
  },
} satisfies ChartConfig;

type priceList = (
  | {
      date: string;
      active_sale: boolean;
      old_price: string;
      price: string;
      loja: string;
    }
  | {
      date: string;
      active_sale: boolean;
      old_price: null;
      price: string;
      loja: string;
    }
)[];

interface ProductPriceChartProps extends React.HtmlHTMLAttributes<HTMLElement> {
  prices: priceList;
}

export function ProductPriceChart({
  className,
  prices,
}: ProductPriceChartProps) {
  const chartData = prices.map((priceObj) => ({
    date: new Date(priceObj.date),
    price: parseBRLToFloat(priceObj.price),
  }));
  return (
    <Card className={className}>
      <CardHeader>
        <CardTitle>Histórico de Preços</CardTitle>
        <CardDescription>Variação de preços na última semana</CardDescription>
      </CardHeader>
      <CardContent>
        <ChartContainer config={chartConfig}>
          <LineChart
            accessibilityLayer
            data={chartData}
            margin={{
              top: 24,
              left: 12,
              right: 12,
            }}
          >
            <CartesianGrid vertical={false} />
            <XAxis
              dataKey="date"
              tickLine={false}
              axisLine={false}
              tickMargin={8}
              tickFormatter={(value) => value.toString().slice(0, 3)}
            />
            <ChartTooltip
              cursor={false}
              content={<ChartTooltipContent indicator="dot" />}
            />
            <Line
              dataKey="price"
              type="linear"
              stroke="var(--color-price)"
              strokeWidth={2}
              dot={{
                fill: "var(--color-price)",
              }}
              activeDot={{
                r: 6,
              }}
            />
          </LineChart>
        </ChartContainer>
      </CardContent>
    </Card>
  );
}
