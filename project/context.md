# System Architecture Analysis
<!-- generated in 0.00s -->

## Overview

- **Project**: /home/tom/github/semcod/sllm
- **Primary Language**: python
- **Languages**: python: 7, shell: 2, yaml: 1, toml: 1
- **Analysis Mode**: static
- **Total Functions**: 45
- **Total Classes**: 9
- **Modules**: 11
- **Entry Points**: 19

## Architecture by Module

### src.sllm.controller
- **Functions**: 11
- **Classes**: 6
- **File**: `controller.py`

### src.sllm.compat
- **Functions**: 11
- **File**: `compat.py`

### src.sllm.cli
- **Functions**: 6
- **File**: `cli.py`

### src.sllm.registry
- **Functions**: 6
- **Classes**: 1
- **File**: `registry.py`

### src.sllm.validation
- **Functions**: 6
- **Classes**: 1
- **File**: `validation.py`

### src.sllm.nlp
- **Functions**: 5
- **Classes**: 1
- **File**: `nlp.py`

## Key Entry Points

Main execution flows into the system:

### src.sllm.compat.launch_koru_agent
> Launch a Koru agent through SLLM while preserving TTY behavior.

Clients with a file/arg prompt contract receive the prompt directly.
Stdin-only clien
- **Calls**: src.sllm.registry.normalize_client_id, src.sllm.registry.get_client_spec, src.sllm.controller.save_prompt, print, print, print, ShellDriveRequest, src.sllm.controller.build_drive_plan

### src.sllm.cli.main
- **Calls**: None.parse_args, AssertionError, src.sllm.cli._print, src.sllm.cli._drive, src.sllm.cli._nlp, src.sllm.cli._print, src.sllm.cli._build_parser, src.sllm.registry.detect_clients

### src.sllm.compat.detect_koru_agent_rows
> Return SLLM clients in Koru ``AgentOption.to_dict`` shape.
- **Calls**: src.sllm.registry.detect_clients, row.get, str, bool, rows.append, row.get, bool, bool

### src.sllm.controller.ShellDrivePlan.to_dict
- **Calls**: list, self.shell_preview, str, str

### src.sllm.registry.ShellClientSpec.to_dict
- **Calls**: self.command_path, list, list, list

### src.sllm.compat.tool_registry_entries
- **Calls**: src.sllm.registry.iter_client_specs, tuple, entries.append, list

### src.sllm.compat.is_client_available
- **Calls**: src.sllm.registry.get_client_spec, bool, spec.command_path

### src.sllm.compat.drive_koru_chat
- **Calls**: src.sllm.controller.drive_shell_llm, result.to_dict, ShellDriveRequest

### src.sllm.controller.ShellDrivePlan.shell_preview
- **Calls**: None.join, shlex.quote

### src.sllm.controller.ShellDriveResult.to_dict
- **Calls**: list, str

### src.sllm.compat.shell_client_ids
- **Calls**: tuple, src.sllm.registry.iter_client_specs

### src.sllm.compat.shell_process_patterns
- **Calls**: tuple, src.sllm.registry.iter_client_specs

### src.sllm.registry.ShellClientSpec.command_path
- **Calls**: resolver

### src.sllm.validation.ValidationResult.to_dict
- **Calls**: list

### src.sllm.compat.autopilot_backend_for_client
- **Calls**: src.sllm.compat.is_shell_llm_client

### src.sllm.validation.intent_contracts

### src.sllm.nlp.ShellIntent.to_dsl

### src.sllm.compat.agent_backend_profiles
> Return Koru-compatible backend profile metadata for shell LLM control.

### src.sllm.compat.agent_backend_aliases
> Return Koru backend aliases owned by SLLM.

## Process Flows

Key execution flows identified:

### Flow 1: launch_koru_agent
```
launch_koru_agent [src.sllm.compat]
  └─ →> normalize_client_id
  └─ →> get_client_spec
      └─> normalize_client_id
  └─ →> save_prompt
      └─> _prompt_root
```

### Flow 2: main
```
main [src.sllm.cli]
  └─> _print
  └─> _drive
      └─> _print
      └─ →> drive_shell_llm
          └─> build_drive_plan
```

### Flow 3: detect_koru_agent_rows
```
detect_koru_agent_rows [src.sllm.compat]
  └─ →> detect_clients
      └─> normalize_client_id
```

### Flow 4: to_dict
```
to_dict [src.sllm.controller.ShellDrivePlan]
```

### Flow 5: tool_registry_entries
```
tool_registry_entries [src.sllm.compat]
  └─ →> iter_client_specs
```

### Flow 6: is_client_available
```
is_client_available [src.sllm.compat]
  └─ →> get_client_spec
      └─> normalize_client_id
```

### Flow 7: drive_koru_chat
```
drive_koru_chat [src.sllm.compat]
  └─ →> drive_shell_llm
      └─> build_drive_plan
          └─> _resolve_spec
          └─> _resolve_command
```

### Flow 8: shell_preview
```
shell_preview [src.sllm.controller.ShellDrivePlan]
```

### Flow 9: shell_client_ids
```
shell_client_ids [src.sllm.compat]
  └─ →> iter_client_specs
```

### Flow 10: shell_process_patterns
```
shell_process_patterns [src.sllm.compat]
  └─ →> iter_client_specs
```

## Key Classes

### src.sllm.controller.ShellDrivePlan
- **Methods**: 2
- **Key Methods**: src.sllm.controller.ShellDrivePlan.shell_preview, src.sllm.controller.ShellDrivePlan.to_dict

### src.sllm.registry.ShellClientSpec
- **Methods**: 2
- **Key Methods**: src.sllm.registry.ShellClientSpec.command_path, src.sllm.registry.ShellClientSpec.to_dict

### src.sllm.controller.ShellDriveResult
- **Methods**: 1
- **Key Methods**: src.sllm.controller.ShellDriveResult.to_dict

### src.sllm.validation.ValidationResult
- **Methods**: 1
- **Key Methods**: src.sllm.validation.ValidationResult.to_dict

### src.sllm.nlp.ShellIntent
- **Methods**: 1
- **Key Methods**: src.sllm.nlp.ShellIntent.to_dsl

### src.sllm.controller.SllmError
> Base error for SLLM control failures.
- **Methods**: 0
- **Inherits**: RuntimeError

### src.sllm.controller.UnknownClientError
> Requested client is not registered.
- **Methods**: 0
- **Inherits**: SllmError

### src.sllm.controller.ClientUnavailableError
> Registered client command is not available in PATH.
- **Methods**: 0
- **Inherits**: SllmError

### src.sllm.controller.ShellDriveRequest
- **Methods**: 0

## Data Transformation Functions

Key functions that process and transform data:

### src.sllm.cli._build_parser
- **Output to**: argparse.ArgumentParser, parser.add_subparsers, sub.add_parser, clients.add_argument, sub.add_parser

### src.sllm.validation.validate_intent
- **Output to**: ValidationResult, src.sllm.registry.get_client_spec, errors.append, intent.prompt.strip, errors.append

### src.sllm.validation._validate_raw_dsl
- **Output to**: raw_dsl.get, isinstance, str, str, isinstance

### src.sllm.validation.validate_intent_contracts
- **Output to**: parse_contract_line, list, errors.append, parsed.append, list

### src.sllm.compat.shell_process_patterns
- **Output to**: tuple, src.sllm.registry.iter_client_specs

## Public API Surface

Functions exposed as public API (no underscore prefix):

- `src.sllm.compat.launch_koru_agent` - 17 calls
- `src.sllm.controller.build_drive_plan` - 11 calls
- `src.sllm.controller.drive_shell_llm` - 10 calls
- `src.sllm.cli.main` - 9 calls
- `src.sllm.compat.detect_koru_agent_rows` - 9 calls
- `src.sllm.validation.validate_intent` - 8 calls
- `src.sllm.controller.save_prompt` - 7 calls
- `src.sllm.validation.validate_intent_contracts` - 6 calls
- `src.sllm.nlp.intent_from_text` - 5 calls
- `src.sllm.controller.ShellDrivePlan.to_dict` - 4 calls
- `src.sllm.registry.ShellClientSpec.to_dict` - 4 calls
- `src.sllm.registry.normalize_client_id` - 4 calls
- `src.sllm.validation.ecosystem_status` - 4 calls
- `src.sllm.compat.tool_registry_entries` - 4 calls
- `src.sllm.registry.detect_clients` - 3 calls
- `src.sllm.compat.is_client_available` - 3 calls
- `src.sllm.compat.drive_koru_chat` - 3 calls
- `src.sllm.controller.ShellDrivePlan.shell_preview` - 2 calls
- `src.sllm.controller.ShellDriveResult.to_dict` - 2 calls
- `src.sllm.controller.result_from_error` - 2 calls
- `src.sllm.compat.shell_client_ids` - 2 calls
- `src.sllm.compat.shell_process_patterns` - 2 calls
- `src.sllm.registry.ShellClientSpec.command_path` - 1 calls
- `src.sllm.registry.get_client_spec` - 1 calls
- `src.sllm.validation.ValidationResult.to_dict` - 1 calls
- `src.sllm.compat.is_shell_llm_client` - 1 calls
- `src.sllm.compat.autopilot_backend_for_client` - 1 calls
- `src.sllm.registry.iter_client_specs` - 0 calls
- `src.sllm.validation.intent_contracts` - 0 calls
- `src.sllm.nlp.ShellIntent.to_dsl` - 0 calls
- `src.sllm.compat.agent_backend_profiles` - 0 calls
- `src.sllm.compat.agent_backend_aliases` - 0 calls

## System Interactions

How components interact:

```mermaid
graph TD
    launch_koru_agent --> normalize_client_id
    launch_koru_agent --> get_client_spec
    launch_koru_agent --> save_prompt
    launch_koru_agent --> print
    main --> parse_args
    main --> AssertionError
    main --> _print
    main --> _drive
    main --> _nlp
    detect_koru_agent_ro --> detect_clients
    detect_koru_agent_ro --> get
    detect_koru_agent_ro --> str
    detect_koru_agent_ro --> bool
    detect_koru_agent_ro --> append
    to_dict --> list
    to_dict --> shell_preview
    to_dict --> str
    to_dict --> command_path
    tool_registry_entrie --> iter_client_specs
    tool_registry_entrie --> tuple
    tool_registry_entrie --> append
    tool_registry_entrie --> list
    is_client_available --> get_client_spec
    is_client_available --> bool
    is_client_available --> command_path
    drive_koru_chat --> drive_shell_llm
    drive_koru_chat --> to_dict
    drive_koru_chat --> ShellDriveRequest
    shell_preview --> join
    shell_preview --> quote
```

## Reverse Engineering Guidelines

1. **Entry Points**: Start analysis from the entry points listed above
2. **Core Logic**: Focus on classes with many methods
3. **Data Flow**: Follow data transformation functions
4. **Process Flows**: Use the flow diagrams for execution paths
5. **API Surface**: Public API functions reveal the interface

## Context for LLM

Maintain the identified architectural patterns and public API surface when suggesting changes.