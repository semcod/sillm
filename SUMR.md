# sllm

SUMD - Structured Unified Markdown Descriptor for AI-aware project refactorization

## Contents

- [Metadata](#metadata)
- [Architecture](#architecture)
- [Dependencies](#dependencies)
- [Call Graph](#call-graph)
- [Test Contracts](#test-contracts)
- [Refactoring Analysis](#refactoring-analysis)
- [Intent](#intent)

## Metadata

- **name**: `sllm`
- **version**: `0.1.8`
- **python_requires**: `>=3.11`
- **license**: Apache-2.0
- **ai_model**: `openrouter/qwen/qwen3-coder-next`
- **ecosystem**: SUMD + DOQL + testql + taskfile
- **generated_from**: pyproject.toml, testql(1), app.doql.less, goal.yaml, .env.example, project/(5 analysis files)

## Architecture

```
SUMD (description) → DOQL/source (code) → taskfile (automation) → testql (verification)
```

### DOQL Application Declaration (`app.doql.less`)

```less markpact:doql path=app.doql.less
// LESS format — define @variables here as needed

app {
  name: sllm;
  version: 0.1.8;
}

dependencies {
  dev: "pytest>=8.0,<10.0, ruff>=0.11,<0.16, goal>=2.1.0, costs>=0.1.20, pfix>=0.1.60";
}

interface[type="cli"] {
  framework: argparse;
}
interface[type="cli"] page[name="sllm"] {

}

deploy {
  target: pip;
}

environment[name="local"] {
  runtime: python;
  env_file: .env;
  python_version: >=3.11;
}
```

## Dependencies

### Runtime

*(see pyproject.toml)*

### Development

```text markpact:deps python scope=dev
pytest>=8.0,<10.0
ruff>=0.11,<0.16
goal>=2.1.0
costs>=0.1.20
pfix>=0.1.60
```

## Call Graph

*35 nodes · 46 edges · 6 modules · CC̄=3.3*

### Hubs (by degree)

| Function | CC | in | out | total |
|----------|----|----|-----|-------|
| `_build_parser` *(in src.sllm.cli)* | 1 | 1 | 24 | **25** |
| `_intent_from_nlp2dsl` *(in src.sllm.nlp)* | 15 ⚠ | 1 | 24 | **25** |
| `launch_koru_agent` *(in src.sllm.compat)* | 8 | 0 | 17 | **17** |
| `_print` *(in src.sllm.cli)* | 6 | 7 | 10 | **17** |
| `_nlp` *(in src.sllm.cli)* | 4 | 1 | 12 | **13** |
| `drive_shell_llm` *(in src.sllm.controller)* | 10 ⚠ | 3 | 10 | **13** |
| `build_drive_plan` *(in src.sllm.controller)* | 3 | 2 | 11 | **13** |
| `_validate_raw_dsl` *(in src.sllm.validation)* | 9 | 1 | 11 | **12** |

```toon markpact:analysis path=project/calls.toon.yaml
# code2llm call graph | /home/tom/github/semcod/sllm
# generated in 0.07s
# nodes: 35 | edges: 46 | modules: 6
# CC̄=3.3

HUBS[20]:
  src.sllm.cli._build_parser
    CC=1  in:1  out:24  total:25
  src.sllm.nlp._intent_from_nlp2dsl
    CC=15  in:1  out:24  total:25
  src.sllm.compat.launch_koru_agent
    CC=8  in:0  out:17  total:17
  src.sllm.cli._print
    CC=6  in:7  out:10  total:17
  src.sllm.cli._nlp
    CC=4  in:1  out:12  total:13
  src.sllm.controller.drive_shell_llm
    CC=10  in:3  out:10  total:13
  src.sllm.controller.build_drive_plan
    CC=3  in:2  out:11  total:13
  src.sllm.validation._validate_raw_dsl
    CC=9  in:1  out:11  total:12
  src.sllm.cli._drive
    CC=5  in:1  out:11  total:12
  src.sllm.registry.normalize_client_id
    CC=1  in:6  out:4  total:10
  src.sllm.compat.detect_koru_agent_rows
    CC=5  in:0  out:9  total:9
  src.sllm.validation.validate_intent
    CC=4  in:1  out:8  total:9
  src.sllm.controller.save_prompt
    CC=2  in:2  out:7  total:9
  src.sllm.cli.main
    CC=5  in:0  out:9  total:9
  src.sllm.nlp._client_from_text
    CC=6  in:1  out:6  total:7
  src.sllm.validation.validate_intent_contracts
    CC=4  in:1  out:6  total:7
  src.sllm.registry.get_client_spec
    CC=3  in:6  out:1  total:7
  src.sllm.nlp._strip_drive_prefix
    CC=5  in:1  out:5  total:6
  src.sllm.nlp.intent_from_text
    CC=3  in:1  out:5  total:6
  src.sllm.registry.detect_clients
    CC=4  in:2  out:3  total:5

MODULES:
  src.sllm.cli  [6 funcs]
    _build_parser  CC=1  out:24
    _drive  CC=5  out:11
    _nlp  CC=4  out:12
    _print  CC=6  out:10
    _read_prompt  CC=4  out:4
    main  CC=5  out:9
  src.sllm.compat  [9 funcs]
    autopilot_backend_for_client  CC=2  out:1
    detect_koru_agent_rows  CC=5  out:9
    drive_koru_chat  CC=1  out:3
    is_client_available  CC=2  out:3
    is_shell_llm_client  CC=1  out:1
    launch_koru_agent  CC=8  out:17
    shell_client_ids  CC=2  out:2
    shell_process_patterns  CC=2  out:2
    tool_registry_entries  CC=4  out:4
  src.sllm.controller  [8 funcs]
    _prompt_root  CC=2  out:3
    _resolve_command  CC=2  out:3
    _resolve_spec  CC=2  out:2
    _timeout_value  CC=3  out:1
    build_drive_plan  CC=3  out:11
    drive_shell_llm  CC=10  out:10
    result_from_error  CC=1  out:2
    save_prompt  CC=2  out:7
  src.sllm.nlp  [4 funcs]
    _client_from_text  CC=6  out:6
    _intent_from_nlp2dsl  CC=15  out:24
    _strip_drive_prefix  CC=5  out:5
    intent_from_text  CC=3  out:5
  src.sllm.registry  [4 funcs]
    detect_clients  CC=4  out:3
    get_client_spec  CC=3  out:1
    iter_client_specs  CC=1  out:0
    normalize_client_id  CC=1  out:4
  src.sllm.validation  [4 funcs]
    _validate_raw_dsl  CC=9  out:11
    ecosystem_status  CC=2  out:4
    validate_intent  CC=4  out:8
    validate_intent_contracts  CC=4  out:6

EDGES:
  src.sllm.cli._drive → src.sllm.cli._print
  src.sllm.cli._drive → src.sllm.controller.drive_shell_llm
  src.sllm.cli._drive → src.sllm.controller.result_from_error
  src.sllm.cli._drive → src.sllm.cli._read_prompt
  src.sllm.cli._nlp → src.sllm.nlp.intent_from_text
  src.sllm.cli._nlp → src.sllm.validation.validate_intent
  src.sllm.cli._nlp → src.sllm.controller.drive_shell_llm
  src.sllm.cli._nlp → src.sllm.cli._print
  src.sllm.cli.main → src.sllm.cli._print
  src.sllm.cli.main → src.sllm.cli._drive
  src.sllm.cli.main → src.sllm.cli._nlp
  src.sllm.cli.main → src.sllm.cli._build_parser
  src.sllm.cli.main → src.sllm.registry.detect_clients
  src.sllm.cli.main → src.sllm.validation.ecosystem_status
  src.sllm.controller.save_prompt → src.sllm.controller._prompt_root
  src.sllm.controller._resolve_spec → src.sllm.registry.get_client_spec
  src.sllm.controller.build_drive_plan → src.sllm.controller._resolve_spec
  src.sllm.controller.build_drive_plan → src.sllm.controller._resolve_command
  src.sllm.controller.build_drive_plan → src.sllm.controller.save_prompt
  src.sllm.controller.drive_shell_llm → src.sllm.controller.build_drive_plan
  src.sllm.controller.drive_shell_llm → src.sllm.controller._timeout_value
  src.sllm.registry.get_client_spec → src.sllm.registry.normalize_client_id
  src.sllm.registry.detect_clients → src.sllm.registry.normalize_client_id
  src.sllm.validation.validate_intent → src.sllm.registry.get_client_spec
  src.sllm.validation.validate_intent → src.sllm.validation._validate_raw_dsl
  src.sllm.validation._validate_raw_dsl → src.sllm.registry.normalize_client_id
  src.sllm.validation.ecosystem_status → src.sllm.validation.validate_intent_contracts
  src.sllm.nlp._client_from_text → src.sllm.registry.iter_client_specs
  src.sllm.nlp._client_from_text → src.sllm.registry.normalize_client_id
  src.sllm.nlp._intent_from_nlp2dsl → src.sllm.registry.normalize_client_id
  src.sllm.nlp.intent_from_text → src.sllm.nlp._client_from_text
  src.sllm.nlp.intent_from_text → src.sllm.nlp._intent_from_nlp2dsl
  src.sllm.nlp.intent_from_text → src.sllm.registry.get_client_spec
  src.sllm.nlp.intent_from_text → src.sllm.nlp._strip_drive_prefix
  src.sllm.compat.is_shell_llm_client → src.sllm.registry.get_client_spec
  src.sllm.compat.is_client_available → src.sllm.registry.get_client_spec
  src.sllm.compat.shell_client_ids → src.sllm.registry.iter_client_specs
  src.sllm.compat.shell_process_patterns → src.sllm.registry.iter_client_specs
  src.sllm.compat.tool_registry_entries → src.sllm.registry.iter_client_specs
  src.sllm.compat.autopilot_backend_for_client → src.sllm.compat.is_shell_llm_client
  src.sllm.compat.detect_koru_agent_rows → src.sllm.registry.detect_clients
  src.sllm.compat.drive_koru_chat → src.sllm.controller.drive_shell_llm
  src.sllm.compat.launch_koru_agent → src.sllm.registry.normalize_client_id
  src.sllm.compat.launch_koru_agent → src.sllm.registry.get_client_spec
  src.sllm.compat.launch_koru_agent → src.sllm.controller.save_prompt
  src.sllm.compat.launch_koru_agent → src.sllm.controller.build_drive_plan
```

## Test Contracts

*Scenarios as contract signatures — what the system guarantees.*

### Cli (1)

**`CLI Command Tests`**

## Refactoring Analysis

*Pre-refactoring snapshot — use this section to identify targets. Generated from `project/` toon files.*

### Call Graph & Complexity (`project/calls.toon.yaml`)

```toon markpact:analysis path=project/calls.toon.yaml
# code2llm call graph | /home/tom/github/semcod/sllm
# generated in 0.07s
# nodes: 35 | edges: 46 | modules: 6
# CC̄=3.3

HUBS[20]:
  src.sllm.cli._build_parser
    CC=1  in:1  out:24  total:25
  src.sllm.nlp._intent_from_nlp2dsl
    CC=15  in:1  out:24  total:25
  src.sllm.compat.launch_koru_agent
    CC=8  in:0  out:17  total:17
  src.sllm.cli._print
    CC=6  in:7  out:10  total:17
  src.sllm.cli._nlp
    CC=4  in:1  out:12  total:13
  src.sllm.controller.drive_shell_llm
    CC=10  in:3  out:10  total:13
  src.sllm.controller.build_drive_plan
    CC=3  in:2  out:11  total:13
  src.sllm.validation._validate_raw_dsl
    CC=9  in:1  out:11  total:12
  src.sllm.cli._drive
    CC=5  in:1  out:11  total:12
  src.sllm.registry.normalize_client_id
    CC=1  in:6  out:4  total:10
  src.sllm.compat.detect_koru_agent_rows
    CC=5  in:0  out:9  total:9
  src.sllm.validation.validate_intent
    CC=4  in:1  out:8  total:9
  src.sllm.controller.save_prompt
    CC=2  in:2  out:7  total:9
  src.sllm.cli.main
    CC=5  in:0  out:9  total:9
  src.sllm.nlp._client_from_text
    CC=6  in:1  out:6  total:7
  src.sllm.validation.validate_intent_contracts
    CC=4  in:1  out:6  total:7
  src.sllm.registry.get_client_spec
    CC=3  in:6  out:1  total:7
  src.sllm.nlp._strip_drive_prefix
    CC=5  in:1  out:5  total:6
  src.sllm.nlp.intent_from_text
    CC=3  in:1  out:5  total:6
  src.sllm.registry.detect_clients
    CC=4  in:2  out:3  total:5

MODULES:
  src.sllm.cli  [6 funcs]
    _build_parser  CC=1  out:24
    _drive  CC=5  out:11
    _nlp  CC=4  out:12
    _print  CC=6  out:10
    _read_prompt  CC=4  out:4
    main  CC=5  out:9
  src.sllm.compat  [9 funcs]
    autopilot_backend_for_client  CC=2  out:1
    detect_koru_agent_rows  CC=5  out:9
    drive_koru_chat  CC=1  out:3
    is_client_available  CC=2  out:3
    is_shell_llm_client  CC=1  out:1
    launch_koru_agent  CC=8  out:17
    shell_client_ids  CC=2  out:2
    shell_process_patterns  CC=2  out:2
    tool_registry_entries  CC=4  out:4
  src.sllm.controller  [8 funcs]
    _prompt_root  CC=2  out:3
    _resolve_command  CC=2  out:3
    _resolve_spec  CC=2  out:2
    _timeout_value  CC=3  out:1
    build_drive_plan  CC=3  out:11
    drive_shell_llm  CC=10  out:10
    result_from_error  CC=1  out:2
    save_prompt  CC=2  out:7
  src.sllm.nlp  [4 funcs]
    _client_from_text  CC=6  out:6
    _intent_from_nlp2dsl  CC=15  out:24
    _strip_drive_prefix  CC=5  out:5
    intent_from_text  CC=3  out:5
  src.sllm.registry  [4 funcs]
    detect_clients  CC=4  out:3
    get_client_spec  CC=3  out:1
    iter_client_specs  CC=1  out:0
    normalize_client_id  CC=1  out:4
  src.sllm.validation  [4 funcs]
    _validate_raw_dsl  CC=9  out:11
    ecosystem_status  CC=2  out:4
    validate_intent  CC=4  out:8
    validate_intent_contracts  CC=4  out:6

EDGES:
  src.sllm.cli._drive → src.sllm.cli._print
  src.sllm.cli._drive → src.sllm.controller.drive_shell_llm
  src.sllm.cli._drive → src.sllm.controller.result_from_error
  src.sllm.cli._drive → src.sllm.cli._read_prompt
  src.sllm.cli._nlp → src.sllm.nlp.intent_from_text
  src.sllm.cli._nlp → src.sllm.validation.validate_intent
  src.sllm.cli._nlp → src.sllm.controller.drive_shell_llm
  src.sllm.cli._nlp → src.sllm.cli._print
  src.sllm.cli.main → src.sllm.cli._print
  src.sllm.cli.main → src.sllm.cli._drive
  src.sllm.cli.main → src.sllm.cli._nlp
  src.sllm.cli.main → src.sllm.cli._build_parser
  src.sllm.cli.main → src.sllm.registry.detect_clients
  src.sllm.cli.main → src.sllm.validation.ecosystem_status
  src.sllm.controller.save_prompt → src.sllm.controller._prompt_root
  src.sllm.controller._resolve_spec → src.sllm.registry.get_client_spec
  src.sllm.controller.build_drive_plan → src.sllm.controller._resolve_spec
  src.sllm.controller.build_drive_plan → src.sllm.controller._resolve_command
  src.sllm.controller.build_drive_plan → src.sllm.controller.save_prompt
  src.sllm.controller.drive_shell_llm → src.sllm.controller.build_drive_plan
  src.sllm.controller.drive_shell_llm → src.sllm.controller._timeout_value
  src.sllm.registry.get_client_spec → src.sllm.registry.normalize_client_id
  src.sllm.registry.detect_clients → src.sllm.registry.normalize_client_id
  src.sllm.validation.validate_intent → src.sllm.registry.get_client_spec
  src.sllm.validation.validate_intent → src.sllm.validation._validate_raw_dsl
  src.sllm.validation._validate_raw_dsl → src.sllm.registry.normalize_client_id
  src.sllm.validation.ecosystem_status → src.sllm.validation.validate_intent_contracts
  src.sllm.nlp._client_from_text → src.sllm.registry.iter_client_specs
  src.sllm.nlp._client_from_text → src.sllm.registry.normalize_client_id
  src.sllm.nlp._intent_from_nlp2dsl → src.sllm.registry.normalize_client_id
  src.sllm.nlp.intent_from_text → src.sllm.nlp._client_from_text
  src.sllm.nlp.intent_from_text → src.sllm.nlp._intent_from_nlp2dsl
  src.sllm.nlp.intent_from_text → src.sllm.registry.get_client_spec
  src.sllm.nlp.intent_from_text → src.sllm.nlp._strip_drive_prefix
  src.sllm.compat.is_shell_llm_client → src.sllm.registry.get_client_spec
  src.sllm.compat.is_client_available → src.sllm.registry.get_client_spec
  src.sllm.compat.shell_client_ids → src.sllm.registry.iter_client_specs
  src.sllm.compat.shell_process_patterns → src.sllm.registry.iter_client_specs
  src.sllm.compat.tool_registry_entries → src.sllm.registry.iter_client_specs
  src.sllm.compat.autopilot_backend_for_client → src.sllm.compat.is_shell_llm_client
  src.sllm.compat.detect_koru_agent_rows → src.sllm.registry.detect_clients
  src.sllm.compat.drive_koru_chat → src.sllm.controller.drive_shell_llm
  src.sllm.compat.launch_koru_agent → src.sllm.registry.normalize_client_id
  src.sllm.compat.launch_koru_agent → src.sllm.registry.get_client_spec
  src.sllm.compat.launch_koru_agent → src.sllm.controller.save_prompt
  src.sllm.compat.launch_koru_agent → src.sllm.controller.build_drive_plan
```

### Code Analysis (`project/analysis.toon.yaml`)

```toon markpact:analysis path=project/analysis.toon.yaml
# code2llm | 11f 1668L | python:7,shell:2,yaml:1,toml:1 | 2026-06-03
# generated in 0.00s
# CC̅=3.3 | critical:1/45 | dups:0 | cycles:0

HEALTH[1]:
  🟡 CC    _intent_from_nlp2dsl CC=15 (limit:15)

REFACTOR[1]:
  1. split 1 high-CC methods  (CC>15)

PIPELINES[15]:
  [1] Src [main]: main → _print
      PURITY: 100% pure
  [2] Src [shell_preview]: shell_preview
      PURITY: 100% pure
  [3] Src [to_dict]: to_dict
      PURITY: 100% pure
  [4] Src [to_dict]: to_dict
      PURITY: 100% pure
  [5] Src [command_path]: command_path
      PURITY: 100% pure
  [6] Src [to_dict]: to_dict
      PURITY: 100% pure
  [7] Src [to_dict]: to_dict
      PURITY: 100% pure
  [8] Src [is_client_available]: is_client_available → get_client_spec → normalize_client_id
      PURITY: 100% pure
  [9] Src [shell_client_ids]: shell_client_ids → iter_client_specs
      PURITY: 100% pure
  [10] Src [shell_process_patterns]: shell_process_patterns → iter_client_specs
      PURITY: 100% pure
  [11] Src [tool_registry_entries]: tool_registry_entries → iter_client_specs
      PURITY: 100% pure
  [12] Src [autopilot_backend_for_client]: autopilot_backend_for_client → is_shell_llm_client → get_client_spec → normalize_client_id
      PURITY: 100% pure
  [13] Src [detect_koru_agent_rows]: detect_koru_agent_rows → detect_clients → normalize_client_id
      PURITY: 100% pure
  [14] Src [drive_koru_chat]: drive_koru_chat → drive_shell_llm → build_drive_plan → _resolve_spec → ...(2 more)
      PURITY: 100% pure
  [15] Src [launch_koru_agent]: launch_koru_agent → normalize_client_id
      PURITY: 100% pure

LAYERS:
  src/                            CC̄=3.3    ←in:0  →out:0
  │ controller                 244L  6C   11m  CC=10     ←2
  │ compat                     205L  0C   11m  CC=8      ←0
  │ registry                   167L  1C    6m  CC=4      ←5
  │ cli                        139L  0C    6m  CC=6      ←0
  │ validation                 127L  1C    6m  CC=9      ←1
  │ !! nlp                        104L  1C    5m  CC=15     ←1
  │ __init__                    36L  0C    0m  CC=0.0    ←0
  │
  ./                              CC̄=0.0    ←in:0  →out:0
  │ !! goal.yaml                  511L  0C    0m  CC=0.0    ←0
  │ pyproject.toml              84L  0C    0m  CC=0.0    ←0
  │ project.sh                  50L  0C    0m  CC=0.0    ←0
  │ tree.sh                      1L  0C    0m  CC=0.0    ←0
  │

COUPLING: no cross-package imports detected

EXTERNAL:
  validation: run `vallm batch .` → validation.toon
  duplication: run `redup scan .` → duplication.toon
```

### Duplication (`project/duplication.toon.yaml`)

```toon markpact:analysis path=project/duplication.toon.yaml
# redup/duplication | 0 groups | 7f 1022L | 2026-06-03

SUMMARY:
  files_scanned: 7
  total_lines:   1022
  dup_groups:    0
  dup_fragments: 0
  saved_lines:   0
  scan_ms:       4218
```

### Evolution / Churn (`project/evolution.toon.yaml`)

```toon markpact:analysis path=project/evolution.toon.yaml
# code2llm/evolution | 45 func | 6f | 2026-06-03
# generated in 0.00s

NEXT[2] (ranked by impact):
  [1] !  SPLIT-FUNC      _intent_from_nlp2dsl  CC=15  fan=13
      WHY: CC=15 exceeds 15
      EFFORT: ~1h  IMPACT: 195

  [2] !! SPLIT           goal.yaml
      WHY: 511L, 0 classes, max CC=0
      EFFORT: ~4h  IMPACT: 0


RISKS[1]:
  ⚠ Splitting goal.yaml may break 0 import paths

METRICS-TARGET:
  CC̄:          3.3 → ≤2.3
  max-CC:      15 → ≤7
  god-modules: 1 → 0
  high-CC(≥15): 1 → ≤0
  hub-types:   0 → ≤0

PATTERNS (language parser shared logic):
  _extract_declarations() in base.py — unified extraction for:
    - TypeScript: interfaces, types, classes, functions, arrow funcs
    - PHP: namespaces, traits, classes, functions, includes
    - Ruby: modules, classes, methods, requires
    - C++: classes, structs, functions, #includes
    - C#: classes, interfaces, methods, usings
    - Java: classes, interfaces, methods, imports
    - Go: packages, functions, structs
    - Rust: modules, functions, traits, use statements

  Shared regex patterns per language:
    - import: language-specific import/require/using patterns
    - class: class/struct/trait declarations with inheritance
    - function: function/method signatures with visibility
    - brace_tracking: for C-family languages ({ })
    - end_keyword_tracking: for Ruby (module/class/def...end)

  Benefits:
    - Consistent extraction logic across all languages
    - Reduced code duplication (~70% reduction in parser LOC)
    - Easier maintenance: fix once, apply everywhere
    - Standardized FunctionInfo/ClassInfo models

HISTORY:
  (first run — no previous data)
```

## Intent

Shell LLM client control plane for semcod/coru automation.
