import React from 'react'
import { Card, CardContent } from '@/components/ui/card'
import { ArrowDown } from 'lucide-react'

const TrendBox = ({ label, trend }: { label: string; trend: string }) => {
  const color =
    trend === 'Bullish'
      ? 'bg-green-200'
      : trend === 'Bearish'
      ? 'bg-red-200'
      : 'bg-gray-200'

  return (
    <Card className={`${color} text-center rounded-2xl shadow-md w-40`}>
      <CardContent className="p-4">
        <div className="font-bold text-xl mb-2">{label}</div>
        <div className="text-base">Trend: {trend}</div>
      </CardContent>
    </Card>
  )
}

const Arrow = () => (
  <div className="flex justify-center my-2">
    <ArrowDown className="h-6 w-6" />
  </div>
)

const MFIBox = () => (
  <Card className="bg-white text-left rounded-2xl shadow-md w-60 ml-4 p-4">
    <div className="font-bold mb-1">MFI Alignment</div>
    <ul className="list-disc list-inside text-sm">
      <li>M1: Bullish</li>
      <li>D1: Bullish</li>
    </ul>
  </Card>
)

export default function TrendDiagram() {
  return (
    <div className="flex justify-center p-6">
      <div className="flex flex-col items-center">
        <TrendBox label="M1" trend="Bullish" />
        <Arrow />
        <TrendBox label="W1" trend="Bullish" />
        <Arrow />
        <TrendBox label="D1" trend="Bearish" />
        <Arrow />
        <TrendBox label="H1" trend="Bearish" />
        <Arrow />
        <TrendBox label="m15" trend="Bearish" />
        <Arrow />
        <TrendBox label="m1" trend="Bearish" />
      </div>
      <MFIBox />
    </div>
  )
}
