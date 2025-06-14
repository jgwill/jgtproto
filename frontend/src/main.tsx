import React from 'react'
import ReactDOM from 'react-dom/client'
import IntentStackUI from './IntentStackUI'
import TrendDiagram from './TrendDiagram'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <div className="p-4">
      <IntentStackUI />
      <div className="mt-8">
        <TrendDiagram />
      </div>
    </div>
  </React.StrictMode>
)
