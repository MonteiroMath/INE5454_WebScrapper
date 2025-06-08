import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  images: {
    remotePatterns: [
      new URL("https://images.kabum.com.br/**"),
      new URL("https://www.gigantec.com.br/**"),
      new URL("https://media.pichau.com.br/**"),
    ],
  },
};

export default nextConfig;
