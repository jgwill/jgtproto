# Intent Flow Integration

## Purpose
Outline how trader intents are transformed into executable strategies through a chain of components: LLM translation, specification parsing, JGTML execution, script generation, and memory recording.

## Expected Deliverables
- `LLMTranslationEngine` translating natural language to `.jgtml-spec` files
- `IntentSpecParser` converting specs to signal packages
- `JGTMLExecutionCore` running strategies against market data
- `EntryScriptGen` producing runnable scripts for automation
- `EchoLattice` storing execution results and feedback
- React components such as `IntentStackUI` visualizing this flow

## Integration Steps
1. Implement Python modules under `fts/intent_flow/` for each component.
2. Connect these modules in the enhanced pipeline or CLI bridge as they mature.
3. Extend the frontend with components to visualize intents and execution status.
4. Document usage patterns in the README and examples.

## Affected Areas
- `fts/intent_flow/`
- `frontend/` UI modules
- Pipeline orchestration code
- Documentation and specs
