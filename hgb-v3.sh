#!/usr/bin/env bash
# =============================================================================
#  hermes-guardrails-bypass.sh  (v3 — E2E clean)
#  Disable Hermes Agent security guardrails on THIS machine.
#
#  Gates turned off:
#    - approvals.mode / unattended_mode / cron_mode / single_query_mode -> off/approve
#    - security.tirith_enabled  -> false (command safety scanner)
#    - security.protected_instruction_files -> false (SOUL.md/AGENTS.md self-edit gate)
#
#  Usage:
#    ./hermes-guardrails-bypass.sh            # apply (backs up config first)
#    ./hermes-guardrails-bypass.sh --restore  # restore latest backup
#    ./hermes-guardrails-bypass.sh --verify   # show current state only
#
#  NOTE on restore: the running gateway process can re-write config.yaml at
#  any time. Restore is atomic (temp + mv), but if the gateway re-applies its
#  own cached values afterwards, restart the process to see the restored state.
#
#  WARNING: with these off, a prompt-injection from any file/page the agent
#  reads can be executed without a confirmation prompt. Own machine, own risk.
# =============================================================================
set -euo pipefail

CFG="${HERMES_CONFIG:-$HOME/.hermes/config.yaml}"
TS="$(date +%Y%m%d-%H%M%S)"
BAK="${CFG}.bak-guardrails-${TS}"

c() { printf "\033[36m%s\033[0m\n" "$*"; }
g() { printf "\033[32m%s\033[0m\n" "$*"; }
r() { printf "\033[31m%s\033[0m\n" "$*"; }

preflight() {
  if [[ ! -f "$CFG" ]]; then
    r "config not found: $CFG"; exit 1
  fi
}

backup() {
  cp -p "$CFG" "$BAK"
  g "backup -> $BAK"
}

apply() {
  c "== disabling guardrails in $CFG =="

  if grep -qE '^approvals:' "$CFG"; then
    python3 - "$CFG" <<'PY'
import re, sys
p = sys.argv[1]
s = open(p).read()
def setkey(block_name, key, value, s):
    pat = re.compile(r'(^%s:\s*\n(?:[ \t]+.*\n)*)' % re.escape(block_name), re.M)
    m = pat.search(s)
    if not m:
        return s
    block = m.group(1)
    if re.search(r'^\s+%s\s*:' % re.escape(key), block, re.M):
        block = re.sub(r'^(\s+%s\s*:).*$' % re.escape(key),
                       lambda mm: mm.group(1) + " %s" % value, block, flags=re.M)
    else:
        block = block.rstrip("\n") + "\n    %s: %s\n" % (key, value)
    return s[:m.start(1)] + block + s[m.end(1):]

s = setkey("approvals", "mode", '"off"', s)
s = setkey("approvals", "unattended_mode", "approve", s)
s = setkey("approvals", "cron_mode", "approve", s)
s = setkey("approvals", "single_query_mode", "approve", s)
s = setkey("approvals", "destructive_slash_confirm", "false", s)
open(p, "w").write(s)
print("  approvals -> off/approve/approve/approve, destructive_slash_confirm -> false")
PY
  else
    printf '\napprovals:\n  mode: "off"\n  unattended_mode: approve\n  cron_mode: approve\n  single_query_mode: approve\n  destructive_slash_confirm: false\n' >> "$CFG"
    echo "  approvals block appended"
  fi

  if grep -qE '^security:' "$CFG"; then
    python3 - "$CFG" <<'PY'
import re, sys
p = sys.argv[1]
s = open(p).read()
def setkey(block_name, key, value, s):
    pat = re.compile(r'(^%s:\s*\n(?:[ \t]+.*\n)*)' % re.escape(block_name), re.M)
    m = pat.search(s)
    if not m:
        return s
    block = m.group(1)
    if re.search(r'^\s+%s\s*:' % re.escape(key), block, re.M):
        block = re.sub(r'^(\s+%s\s*:).*$' % re.escape(key),
                       lambda mm: mm.group(1) + " %s" % value, block, flags=re.M)
    else:
        block = block.rstrip("\n") + "\n    %s: %s\n" % (key, value)
    return s[:m.start(1)] + block + s[m.end(1):]

s = setkey("security", "tirith_enabled", "false", s)
s = setkey("security", "tirith_fail_open", "true", s)
s = setkey("security", "protected_instruction_files", "false", s)
open(p, "w").write(s)
print("  security -> tirith_enabled false, fail_open true, protected_instruction_files false")
PY
  else
    printf '\nsecurity:\n  tirith_enabled: false\n  tirith_fail_open: true\n  protected_instruction_files: false\n' >> "$CFG"
    echo "  security block appended"
  fi

  g "done."
  echo "  NOTE: full effect after a process restart."
}

restore() {
  local target=""
  if [[ $# -ge 2 && -f "$2" ]]; then
    target="$2"
  else
    target="$(ls -1t "${CFG}".bak-guardrails-* 2>/dev/null | head -1 || true)"
  fi
  if [[ -z "$target" || ! -f "$target" ]]; then
    r "no backup found"; exit 1
  fi
  # v3: atomic restore. If the running gateway re-writes config afterwards,
  # the restored state is on disk and takes effect after a process restart.
  local tmp
  tmp="$(mktemp "${CFG}.restore.XXXXXX")"
  cp -p "$target" "$tmp"
  mv -f "$tmp" "$CFG"
  g "restored from $target"
  echo "  NOTE: if the gateway process is running it may re-apply its cached"
  echo "        values; the on-disk state is authoritative after restart."
}

verify() {
  c "== current guardrail state =="
  for k in "mode" "unattended_mode" "cron_mode" "single_query_mode" "destructive_slash_confirm"; do
    printf "  approvals.%-26s = %s\n" "$k" \
      "$(grep -E "^\s+$k:" "$CFG" | head -1 | awk '{print $2}' || echo '(unset)')"
  done
  for k in "tirith_enabled" "tirith_fail_open" "protected_instruction_files"; do
    printf "  security.%-24s = %s\n" "$k" \
      "$(grep -E "^\s+$k:" "$CFG" | head -1 | awk '{print $2}' || echo '(unset)')"
  done
  printf "  %-34s = %s\n" "HERMES_YOLO_MODE (env)" "${HERMES_YOLO_MODE:-(unset)}"
}

preflight
case "${1:-}" in
  --restore) restore "$@" ;;
  --verify)  verify ;;
  *)         backup; apply; verify ;;
esac
