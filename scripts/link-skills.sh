#!/usr/bin/env bash
set -euo pipefail

# 开发用脚本：把本仓库的技能软链到本机 agent 的技能目录。
#
# 每个条目都是指向本仓库的软链，所以在仓库里改文件立刻生效，
# git pull 就等于升级全部技能。新增、删除、重命名技能后重跑一次。
#
# 目标目录默认 ~/.claude/skills，可用环境变量覆盖：
#   CLAUDE_SKILLS_DIR=~/.agents/skills bash scripts/link-skills.sh

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

# 如果目标目录本身是指向本仓库的软链，写进去就会把逐技能的软链塞回
# 仓库自己的 skills/ 里，污染工作区。检测到就退出，而不是照写不误。
if [ -L "$DEST" ]; then
  resolved="$(readlink -f "$DEST")"
  case "$resolved" in
    "$REPO"|"$REPO"/*)
      echo "error: $DEST 是指向本仓库的软链（$resolved）。" >&2
      echo "先删掉它（rm \"$DEST\"）再重跑，脚本会重建为真实目录。" >&2
      exit 1
      ;;
  esac
fi

mkdir -p "$DEST"

count=0
while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  name="$(basename "$src")"
  target="$DEST/$name"

  # 目标已存在且不是软链（真实目录或文件）时先删掉，
  # 否则 ln -sfn 会把它塞进那个目录里，而不是替换它。
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    rm -rf "$target"
  fi

  ln -sfn "$src" "$target"
  echo "linked $name -> $src"
  count=$((count + 1))
done < <(find "$REPO/skills" -name SKILL.md -not -path '*/node_modules/*' -print0 | sort -z)

echo "共 $count 个技能 -> $DEST"
