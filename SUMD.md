# sllm

Shell LLM client control plane for semcod/coru automation.

## Contents

- [Metadata](#metadata)
- [Architecture](#architecture)
- [Interfaces](#interfaces)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Deployment](#deployment)
- [Environment Variables (`.env.example`)](#environment-variables-envexample)
- [Release Management (`goal.yaml`)](#release-management-goalyaml)
- [Code Analysis](#code-analysis)
- [Call Graph](#call-graph)
- [Test Contracts](#test-contracts)
- [Intent](#intent)

## Metadata

- **name**: `sllm`
- **version**: `0.1.8`
- **python_requires**: `>=3.11`
- **license**: Apache-2.0
- **ai_model**: `openrouter/qwen/qwen3-coder-next`
- **ecosystem**: SUMD + DOQL + testql + taskfile
- **generated_from**: pyproject.toml, testql(1), app.doql.less, goal.yaml, .env.example, project/(3 analysis files)

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

## Interfaces

### CLI Entry Points

- `sllm`

### testql Scenarios

#### `testql-scenarios/generated-cli-tests.testql.toon.yaml`

```toon markpact:testql path=testql-scenarios/generated-cli-tests.testql.toon.yaml
# SCENARIO: CLI Command Tests
# TYPE: cli
# GENERATED: true

CONFIG[2]{key, value}:
  cli_command, python -m sllm
  timeout_ms, 10000

# Test 1: CLI help command
SHELL "python -m sllm --help" 5000
ASSERT_EXIT_CODE 0
ASSERT_STDOUT_CONTAINS "usage"

# Test 2: CLI version command
SHELL "python -m sllm --version" 5000
ASSERT_EXIT_CODE 0

# Test 3: CLI main workflow (dry-run)
SHELL "python -m sllm --help" 10000
ASSERT_EXIT_CODE 0
```

## Configuration

```yaml
project:
  name: sllm
  version: 0.1.8
  env: local
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

## Deployment

```bash markpact:run
pip install sllm

# development install
pip install -e .[dev]
```

## Environment Variables (`.env.example`)

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENROUTER_API_KEY` | `*(not set)*` | Required: OpenRouter API key (https://openrouter.ai/keys) |
| `LLM_MODEL` | `openrouter/qwen/qwen3-coder-next` | Model (default: openrouter/qwen/qwen3-coder-next) |
| `PFIX_AUTO_APPLY` | `true` | true = apply fixes without asking |
| `PFIX_AUTO_INSTALL_DEPS` | `true` | true = auto pip/uv install |
| `PFIX_AUTO_RESTART` | `false` | true = os.execv restart after fix |
| `PFIX_MAX_RETRIES` | `3` |  |
| `PFIX_DRY_RUN` | `false` |  |
| `PFIX_ENABLED` | `true` |  |
| `PFIX_GIT_COMMIT` | `false` | true = auto-commit fixes |
| `PFIX_GIT_PREFIX` | `pfix:` | commit message prefix |
| `PFIX_CREATE_BACKUPS` | `false` | false = disable .pfix_backups/ directory |

## Release Management (`goal.yaml`)

- **versioning**: `semver`
- **commits**: `conventional` scope=`sllm`
- **changelog**: `keep-a-changelog`
- **build strategies**: `python`, `nodejs`, `rust`
- **version files**: `VERSION`, `pyproject.toml:version`, `venv/lib/python3.13/site-packages/markdown_it/__init__.py:__version__`

## Code Analysis

### `project/map.toon.yaml`

```toon markpact:analysis path=project/map.toon.yaml
# sllm | 11f 1220L | python:8,shell:2,less:1 | 2026-06-03
# stats: 45 func | 9 cls | 11 mod | CC̄=4.0 | critical:3 | cycles:0
# alerts[5]: CC test_compat_exports_koru_agent_rows=17; CC _intent_from_nlp2dsl=15; CC drive_shell_llm=10; CC _validate_raw_dsl=9; CC launch_koru_agent=8
# hotspots[5]: test_compat_exports_koru_agent_rows fan=11; launch_koru_agent fan=10; build_drive_plan fan=10; _intent_from_nlp2dsl fan=10; _drive fan=9
# evolution: baseline
# Keys: M=modules, D=details, i=imports, e=exports, c=classes, f=functions, m=methods
M[11]:
  app.doql.less,28
  project.sh,50
  src/sllm/__init__.py,37
  src/sllm/cli.py,140
  src/sllm/compat.py,206
  src/sllm/controller.py,245
  src/sllm/nlp.py,105
  src/sllm/registry.py,168
  src/sllm/validation.py,128
  tests/test_sllm.py,111
  tree.sh,2
D:
  src/sllm/__init__.py:
  src/sllm/cli.py:
    e: _print,_build_parser,_read_prompt,_drive,_nlp,main
    _print(payload;output_format)
    _build_parser()
    _read_prompt(args)
    _drive(args)
    _nlp(args)
    main(argv)
  src/sllm/compat.py:
    e: agent_backend_profiles,agent_backend_aliases,is_shell_llm_client,is_client_available,shell_client_ids,shell_process_patterns,tool_registry_entries,autopilot_backend_for_client,detect_koru_agent_rows,drive_koru_chat,launch_koru_agent
    agent_backend_profiles()
    agent_backend_aliases()
    is_shell_llm_client(agent_id)
    is_client_available(client_id)
    shell_client_ids()
    shell_process_patterns()
    tool_registry_entries()
    autopilot_backend_for_client(agent_id)
    detect_koru_agent_rows()
    drive_koru_chat()
    launch_koru_agent()
  src/sllm/controller.py:
    e: _prompt_root,save_prompt,_resolve_spec,_resolve_command,build_drive_plan,_timeout_value,drive_shell_llm,result_from_error,SllmError,UnknownClientError,ClientUnavailableError,ShellDriveRequest,ShellDrivePlan,ShellDriveResult
    SllmError:  # Base error for SLLM control failures.
    UnknownClientError:  # Requested client is not registered.
    ClientUnavailableError:  # Registered client command is not available in PATH.
    ShellDriveRequest:
    ShellDrivePlan: shell_preview(0),to_dict(0)
    ShellDriveResult: to_dict(0)
    _prompt_root(project;prompt_dir)
    save_prompt(prompt)
    _resolve_spec(client_id)
    _resolve_command(spec)
    build_drive_plan(request)
    _timeout_value(timeout_seconds)
    drive_shell_llm(request)
    result_from_error(client_id;exc)
  src/sllm/nlp.py:
    e: _client_from_text,_strip_drive_prefix,_intent_from_nlp2dsl,intent_from_text,ShellIntent
    ShellIntent: to_dsl(0)
    _client_from_text(text;default_client)
    _strip_drive_prefix(text)
    _intent_from_nlp2dsl(text;default_client)
    intent_from_text(text)
  src/sllm/registry.py:
    e: normalize_client_id,iter_client_specs,get_client_spec,detect_clients,ShellClientSpec
    ShellClientSpec: command_path(1),to_dict(0)
    normalize_client_id(raw)
    iter_client_specs()
    get_client_spec(client_id)
    detect_clients()
  src/sllm/validation.py:
    e: validate_intent,_validate_raw_dsl,intent_contracts,validate_intent_contracts,ecosystem_status,ValidationResult
    ValidationResult: to_dict(0)
    validate_intent(intent)
    _validate_raw_dsl(raw_dsl;client_id)
    intent_contracts()
    validate_intent_contracts()
    ecosystem_status()
  tests/test_sllm.py:
    e: test_registry_normalizes_common_aliases,test_detect_clients_marks_available_from_injected_which,test_compat_exports_koru_agent_rows,test_build_drive_plan_uses_message_file_for_aider,test_nlp_rules_select_client_and_prompt,test_validate_intent_rejects_raw_dsl_without_sllm_drive,test_intent_contracts_are_exposed_for_ecosystem_validation
    test_registry_normalizes_common_aliases()
    test_detect_clients_marks_available_from_injected_which()
    test_compat_exports_koru_agent_rows(monkeypatch)
    test_build_drive_plan_uses_message_file_for_aider(monkeypatch;tmp_path)
    test_nlp_rules_select_client_and_prompt()
    test_validate_intent_rejects_raw_dsl_without_sllm_drive()
    test_intent_contracts_are_exposed_for_ecosystem_validation()
```

### `project/logic.pl`

```prolog markpact:analysis path=project/logic.pl
% ── Project Metadata ─────────────────────────────────────
project_metadata('sllm', '0.1.8', 'python').

% ── Project Files ────────────────────────────────────────
project_file('app.doql.less', 28, 'less').
project_file('project.sh', 50, 'shell').
project_file('src/sllm/__init__.py', 37, 'python').
project_file('src/sllm/cli.py', 140, 'python').
project_file('src/sllm/compat.py', 206, 'python').
project_file('src/sllm/controller.py', 245, 'python').
project_file('src/sllm/nlp.py', 105, 'python').
project_file('src/sllm/registry.py', 168, 'python').
project_file('src/sllm/validation.py', 128, 'python').
project_file('tests/test_sllm.py', 111, 'python').
project_file('tree.sh', 2, 'shell').

% ── Python Functions ─────────────────────────────────────
python_function('src/sllm/cli.py', '_print', 2, 6, 5).
python_function('src/sllm/cli.py', '_build_parser', 0, 1, 5).
python_function('src/sllm/cli.py', '_read_prompt', 1, 4, 4).
python_function('src/sllm/cli.py', '_drive', 1, 5, 9).
python_function('src/sllm/cli.py', '_nlp', 1, 4, 8).
python_function('src/sllm/cli.py', 'main', 1, 5, 8).
python_function('src/sllm/compat.py', 'agent_backend_profiles', 0, 1, 0).
python_function('src/sllm/compat.py', 'agent_backend_aliases', 0, 1, 0).
python_function('src/sllm/compat.py', 'is_shell_llm_client', 1, 1, 1).
python_function('src/sllm/compat.py', 'is_client_available', 1, 2, 3).
python_function('src/sllm/compat.py', 'shell_client_ids', 0, 2, 2).
python_function('src/sllm/compat.py', 'shell_process_patterns', 0, 2, 2).
python_function('src/sllm/compat.py', 'tool_registry_entries', 0, 4, 4).
python_function('src/sllm/compat.py', 'autopilot_backend_for_client', 1, 2, 1).
python_function('src/sllm/compat.py', 'detect_koru_agent_rows', 0, 5, 6).
python_function('src/sllm/compat.py', 'drive_koru_chat', 0, 1, 3).
python_function('src/sllm/compat.py', 'launch_koru_agent', 0, 8, 10).
python_function('src/sllm/controller.py', '_prompt_root', 2, 2, 2).
python_function('src/sllm/controller.py', 'save_prompt', 1, 2, 7).
python_function('src/sllm/controller.py', '_resolve_spec', 1, 2, 2).
python_function('src/sllm/controller.py', '_resolve_command', 1, 2, 3).
python_function('src/sllm/controller.py', 'build_drive_plan', 1, 3, 10).
python_function('src/sllm/controller.py', '_timeout_value', 1, 3, 1).
python_function('src/sllm/controller.py', 'drive_shell_llm', 1, 10, 7).
python_function('src/sllm/controller.py', 'result_from_error', 2, 1, 2).
python_function('src/sllm/nlp.py', '_client_from_text', 2, 6, 5).
python_function('src/sllm/nlp.py', '_strip_drive_prefix', 1, 5, 4).
python_function('src/sllm/nlp.py', '_intent_from_nlp2dsl', 2, 15, 10).
python_function('src/sllm/nlp.py', 'intent_from_text', 1, 3, 5).
python_function('src/sllm/registry.py', 'normalize_client_id', 1, 1, 4).
python_function('src/sllm/registry.py', 'iter_client_specs', 0, 1, 0).
python_function('src/sllm/registry.py', 'get_client_spec', 1, 3, 1).
python_function('src/sllm/registry.py', 'detect_clients', 0, 4, 3).
python_function('src/sllm/validation.py', 'validate_intent', 1, 4, 7).
python_function('src/sllm/validation.py', '_validate_raw_dsl', 2, 9, 4).
python_function('src/sllm/validation.py', 'intent_contracts', 0, 1, 0).
python_function('src/sllm/validation.py', 'validate_intent_contracts', 0, 4, 3).
python_function('src/sllm/validation.py', 'ecosystem_status', 0, 2, 4).
python_function('tests/test_sllm.py', 'test_registry_normalizes_common_aliases', 0, 4, 2).
python_function('tests/test_sllm.py', 'test_detect_clients_marks_available_from_injected_which', 0, 8, 2).
python_function('tests/test_sllm.py', 'test_compat_exports_koru_agent_rows', 1, 17, 11).
python_function('tests/test_sllm.py', 'test_build_drive_plan_uses_message_file_for_aider', 2, 4, 4).
python_function('tests/test_sllm.py', 'test_nlp_rules_select_client_and_prompt', 0, 4, 2).
python_function('tests/test_sllm.py', 'test_validate_intent_rejects_raw_dsl_without_sllm_drive', 0, 3, 2).
python_function('tests/test_sllm.py', 'test_intent_contracts_are_exposed_for_ecosystem_validation', 0, 5, 3).

% ── Python Classes ───────────────────────────────────────
python_class('src/sllm/controller.py', 'SllmError').
python_class('src/sllm/controller.py', 'UnknownClientError').
python_class('src/sllm/controller.py', 'ClientUnavailableError').
python_class('src/sllm/controller.py', 'ShellDriveRequest').
python_class('src/sllm/controller.py', 'ShellDrivePlan').
python_method('ShellDrivePlan', 'shell_preview', 0, 2, 2).
python_method('ShellDrivePlan', 'to_dict', 0, 1, 3).
python_class('src/sllm/controller.py', 'ShellDriveResult').
python_method('ShellDriveResult', 'to_dict', 0, 1, 2).
python_class('src/sllm/nlp.py', 'ShellIntent').
python_method('ShellIntent', 'to_dsl', 0, 1, 0).
python_class('src/sllm/registry.py', 'ShellClientSpec').
python_method('ShellClientSpec', 'command_path', 1, 4, 1).
python_method('ShellClientSpec', 'to_dict', 0, 1, 2).
python_class('src/sllm/validation.py', 'ValidationResult').
python_method('ValidationResult', 'to_dict', 0, 1, 1).

% ── Dependencies ─────────────────────────────────────────

% ── Makefile Targets ─────────────────────────────────────

% ── Taskfile Tasks ───────────────────────────────────────

% ── Environment Variables ────────────────────────────────
env_variable('OPENROUTER_API_KEY', '*(not set)*', 'Required: OpenRouter API key (https://openrouter.ai/keys)').
env_variable('LLM_MODEL', 'openrouter/qwen/qwen3-coder-next', 'Model (default: openrouter/qwen/qwen3-coder-next)').
env_variable('PFIX_AUTO_APPLY', 'true', 'true = apply fixes without asking').
env_variable('PFIX_AUTO_INSTALL_DEPS', 'true', 'true = auto pip/uv install').
env_variable('PFIX_AUTO_RESTART', 'false', 'true = os.execv restart after fix').
env_variable('PFIX_MAX_RETRIES', '3', '').
env_variable('PFIX_DRY_RUN', 'false', '').
env_variable('PFIX_ENABLED', 'true', '').
env_variable('PFIX_GIT_COMMIT', 'false', 'true = auto-commit fixes').
env_variable('PFIX_GIT_PREFIX', 'pfix:', 'commit message prefix').
env_variable('PFIX_CREATE_BACKUPS', 'false', 'false = disable .pfix_backups/ directory').

% ── TestQL Scenarios ─────────────────────────────────────
testql_scenario('generated-cli-tests.testql.toon.yaml', 'cli').

% ── Semantic Facts from SUMD.md ──────────────────────────
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

## Intent

Shell LLM client control plane for semcod/coru automation.
