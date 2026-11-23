# skills

我的 agent 技能集合，用 [`npx skills`](https://skills.sh) 安装。

## 安装

```bash
npx skills add ChaoqiYin/skills
```

安装器会让你挑选要装哪些技能、装到哪个 agent 上。

先看看有哪些：

```bash
npx skills add ChaoqiYin/skills --list
```

只装某一个：

```bash
npx skills add ChaoqiYin/skills --skill=<技能名>
```

更新：

```bash
npx skills update <技能名>
```

## 技能列表

### engineering

- [lark-issue-tracker](./skills/engineering/lark-issue-tracker/SKILL.md)：用飞书多维表格管理需求、任务状态、依赖和评论协作。

## 仓库结构

```
skills/                     技能本体，按桶分类，每个技能一个目录
  engineering/<名字>/SKILL.md
README.md                   本文件，同时充当技能索引
CLAUDE.md                   仓库约定，供 agent 读取
scripts/link-skills.sh      把技能软链到本机，用于本地编辑
```

## 本地开发

技能在本仓库里编辑、在本机立刻生效：

```bash
bash scripts/link-skills.sh
```

它把 `skills/` 下每个技能软链到 `~/.claude/skills/<名字>`。因为是软链，改完文件 Claude Code 立刻读到，不需要重新安装。新增、删除、重命名技能后重跑一次即可。

## 加新技能

手动三步：

1. 建目录 `skills/<桶>/<技能名>/SKILL.md`
2. frontmatter 里写 `name` 和 `description`
3. 在上面那份技能列表里登记
