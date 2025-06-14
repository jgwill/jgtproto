import React, { useEffect, useState } from 'react'
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

const MFIBox = ({ items }: { items: { timestamp: string; mfi: number; mfi_green: number; }[] }) => (
  <Card className="bg-white text-left rounded-2xl shadow-md w-60 ml-4 p-4">
    <div className="font-bold mb-1">MFI Alignment</div>
    <ul className="list-disc list-inside text-sm">
      {items.slice(0, 2).map((item, idx) => (
        <li key={idx}>{item.timestamp}: {item.mfi_green ? 'Bullish' : 'Neutral'}</li>
      ))}
    </ul>
  </Card>
)

export default function TrendDiagram() {
  const [trends, setTrends] = useState<{label: string; trend: string}[]>([])
  const [mfi, setMfi] = useState<any[]>([])

  useEffect(() => {
    fetch('/trends').then(r => r.json()).then(setTrends).catch(() => {})
    fetch('/mfi').then(r => r.json()).then(setMfi).catch(() => {})
  }, [])

  return (
    <div className="flex justify-center p-6">
      <div className="flex flex-col items-center">
        {trends.map((t, idx) => (
          <React.Fragment key={idx}>
            <TrendBox label={t.label} trend={t.trend} />
            {idx < trends.length - 1 && <Arrow />}
          </React.Fragment>
        ))}
      </div>
      <MFIBox items={mfi} />
    </div>
  )
}
