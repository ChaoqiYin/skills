技能放在 `skills/` 下，按桶分类：

- `engineering/`：写代码时用的
- `productivity/`：非代码的工作流

每个技能是 `skills/<桶>/<技能名>/SKILL.md`。桶可以按需增加，也可以改名，改完记得同步本文件和两份 README 的索引。

## 约定

1. `SKILL.md` 的 frontmatter 必须有 `name`（小写加连字符）和 `description`。
2. `description` 要同时写清「做什么」和「什么时候触发」。它是别人在 `npx skills add --list` 里唯一能看到的一行，写得含糊就没人装。别写「一个有用的技能」这种。
3. 新增、重命名、删除技能后，必须同步更新 `README.md` 和 `skills/README.md` 的索引。索引里的技能名要链接到它自己的 `SKILL.md`。
4. **不要在分类目录里直接放 `SKILL.md`**（比如 `skills/engineering/SKILL.md`）。它比该分类下的技能更浅，会遮蔽掉它们全部。分类目录里放 `README.md` 是安全的，扫描只认 `SKILL.md`。
5. 半成品的技能加 `metadata.internal: true`，默认对其他人隐藏，只在本机设了 `INSTALL_INTERNAL_SKILLS=1` 时可见。

## 为什么没有 package.json

分发走 [skills.sh](https://skills.sh)。别人执行 `npx skills add <owner>/skills`，CLI 会把仓库 clone 下来、扫 `skills/` 里的 `SKILL.md`。整条链路只用 git，不经过 npm registry，所以本仓库不需要 `package.json`、不需要 `.claude-plugin/`、也没有版本号这回事：用户跑 `npx skills update` 直接拿到最新 commit。

## 本地编辑

`scripts/link-skills.sh` 把每个技能软链到 `~/.claude/skills`，改文件立刻生效。新增、删除、重命名技能后重跑一次。
