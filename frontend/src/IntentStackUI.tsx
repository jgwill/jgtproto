import { Card, CardContent } from '@/components/ui/card'

export default function IntentStackUI() {
  return (
    <div className="grid grid-cols-1 gap-4 p-4">
      <Card>
        <CardContent>
          🎤 Trader Intent
          <div className="text-sm text-gray-600 mt-1">
            Natural language: market structure, waves, levels
          </div>
        </CardContent>
      </Card>
      <Card>
        <CardContent>
          🧠 LLM Translation Engine
          <div className="text-sm text-gray-600 mt-1">
            Parses narrative → <code>.jgtml-spec</code> using pattern rules
          </div>
        </CardContent>
      </Card>
      <Card>
        <CardContent>
          🟩 IntentSpecParser (Interpreter)
          <div className="text-sm text-gray-600 mt-1">
            Reads <code>.jgtml-spec</code> → constructs signal package
          </div>
        </CardContent>
      </Card>
      <Card>
        <CardContent>
          🟦 JGTML Execution Core
          <div className="pl-4 mt-2 space-y-1">
            <div>• run_spec() executor</div>
            <div>• Indicator loader (AO, Alligator)</div>
            <div>• Signal validator engine</div>
            <div>• Decision node: ENTER / WAIT / EXIT</div>
          </div>
          <div className="text-sm text-gray-600 mt-2">
            Core logic to interpret and execute strategy commands from spec
          </div>
        </CardContent>
      </Card>
      <Card>
        <CardContent>
          📜 EntryScriptGen
          <div className="text-sm text-gray-600 mt-1">
            Generates runnable bash/python script from signal
          </div>
        </CardContent>
      </Card>
      <Card>
        <CardContent>
          🟫 Echo Lattice (Memory Crystallization)
          <div className="text-sm text-gray-600 mt-1">
            Records outcome + feedback to memory crystal
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
