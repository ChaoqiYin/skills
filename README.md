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

- [architect](./skills/engineering/architect/SKILL.md)：在实现前设计类型、接口和模块边界。
- [arena](./skills/engineering/arena/SKILL.md)：比较独立子代理的候选产物，整合并验证结果。
- [blast-radius](./skills/engineering/blast-radius/SKILL.md)：检查变更在差异之外的影响，并用实际运行验证风险。
- [bot-help](./skills/engineering/bot-help/SKILL.md)：介绍技能用法、推荐工作流，并排查技能发现问题。
- [bot-mode](./skills/engineering/bot-mode/SKILL.md)：按任务编排执行流程、原则、子代理协作和验证。
- [bro](./skills/engineering/bro/SKILL.md)：用简明语言重述上一条回复。
- [correct](./skills/engineering/correct/SKILL.md)：识别代理反复犯的错误，并用架构、类型、检查和测试防止复发。
- [create-formal-verification-skill](./skills/engineering/create-formal-verification-skill/SKILL.md)：创建项目内形式化验证技能，检查关键性质并记录验证范围。
- [create-verification-skill](./skills/engineering/create-verification-skill/SKILL.md)：创建能启动、驱动和验证实际应用的项目技能。
- [figure-it-out](./skills/engineering/figure-it-out/SKILL.md)：为复杂任务设计可审阅的执行流程，逐步验证并记录决策。
- [how](./skills/engineering/how/SKILL.md)：解释代码的运行方式、模块职责和架构关系。
- [in-your-own-words](./skills/engineering/in-your-own-words/SKILL.md)：用自己的话复述用户目标与待解决的问题。
- [interrogate](./skills/engineering/interrogate/SKILL.md)：通过独立子代理开展对抗评审，只报告可复现的问题。
- [ketchup](./skills/engineering/ketchup/SKILL.md)：概述本次对话中的工作进展和等待用户处理的事项。
- [lark-issue-tracker](./skills/engineering/lark-issue-tracker/SKILL.md)：用飞书多维表格管理需求、任务状态、依赖和评论协作。
- [maintain-formal-verification-skill](./skills/engineering/maintain-formal-verification-skill/SKILL.md)：让形式化验证与代码保持一致，区分验证漂移和实际缺陷。
- [maintain-verification-skill](./skills/engineering/maintain-verification-skill/SKILL.md)：检查并维护项目验证技能、功能地图和实际应用验证流程。
- [principle-attack-the-premise](./skills/engineering/principle-attack-the-premise/SKILL.md)：当多次修复失败时，先检验它们共同依赖的假设。
- [principle-boundary-discipline](./skills/engineering/principle-boundary-discipline/SKILL.md)：在系统边界集中校验输入，并保持业务逻辑纯粹。
- [principle-build-the-lever](./skills/engineering/principle-build-the-lever/SKILL.md)：为非简单工作构建可重复运行的工具或验证流程。
- [principle-encode-lessons-in-structure](./skills/engineering/principle-encode-lessons-in-structure/SKILL.md)：把反复出现的经验落实为类型、检查、元数据或脚本。
- [principle-exhaust-the-design-space](./skills/engineering/principle-exhaust-the-design-space/SKILL.md)：为新交互或架构设计制作多个原型并比较结果。
- [principle-experience-first](./skills/engineering/principle-experience-first/SKILL.md)：根据用户体验权衡产品范围和实现方案。
- [principle-fix-root-causes](./skills/engineering/principle-fix-root-causes/SKILL.md)：追溯并修复问题根因，避免用防御逻辑掩盖错误。
- [principle-foundational-thinking](./skills/engineering/principle-foundational-thinking/SKILL.md)：先确定核心数据结构、状态归属和实现顺序。
- [principle-guard-the-context-window](./skills/engineering/principle-guard-the-context-window/SKILL.md)：限制上下文开销，按需分派工作并保留摘要。
- [principle-laziness-protocol](./skills/engineering/principle-laziness-protocol/SKILL.md)：减少抽象和改动规模，用最小变更解决问题。
- [principle-make-operations-idempotent](./skills/engineering/principle-make-operations-idempotent/SKILL.md)：让命令和生命周期操作在重试或中断后仍能收敛。
- [principle-migrate-callers-then-delete-legacy-apis](./skills/engineering/principle-migrate-callers-then-delete-legacy-apis/SKILL.md)：迁移内部接口的调用方，再删除旧接口及兼容代码。
- [principle-minimize-reader-load](./skills/engineering/principle-minimize-reader-load/SKILL.md)：减少间接层和隐含状态，降低代码理解成本。
- [principle-model-the-domain](./skills/engineering/principle-model-the-domain/SKILL.md)：用清晰的数据结构表达领域规则和状态。
- [principle-never-block-on-the-human](./skills/engineering/principle-never-block-on-the-human/SKILL.md)：自主推进已授权的可逆工作，减少不必要的确认。
- [principle-outcome-oriented-execution](./skills/engineering/principle-outcome-oriented-execution/SKILL.md)：按明确验证边界推进迁移，保证最终结果完整。
- [principle-prove-it-works](./skills/engineering/principle-prove-it-works/SKILL.md)：通过实际产物和运行证据验证任务结果。
- [principle-redesign-from-first-principles](./skills/engineering/principle-redesign-from-first-principles/SKILL.md)：把新需求纳入整体设计，并同步相关引用。
- [principle-separate-before-serializing-shared-state](./skills/engineering/principle-separate-before-serializing-shared-state/SKILL.md)：优先隔离并发写入目标，再考虑串行化共享状态。
- [principle-sequence-verifiable-units](./skills/engineering/principle-sequence-verifiable-units/SKILL.md)：把多步工作拆成可验证单元，逐个检查后推进。
- [principle-subtract-before-you-add](./skills/engineering/principle-subtract-before-you-add/SKILL.md)：先删除过时和重复部分，再增加新实现。
- [principle-test-behavior-not-implementation](./skills/engineering/principle-test-behavior-not-implementation/SKILL.md)：验证可观察行为，避免测试依赖实现细节。
- [principle-type-system-discipline](./skills/engineering/principle-type-system-discipline/SKILL.md)：用类型和边界解析排除非法状态与参数混用。
- [recall](./skills/engineering/recall/SKILL.md)：结合会话历史和共享记录恢复近期工作上下文。
- [setup-bot](./skills/engineering/setup-bot/SKILL.md)：生成领域文档约定和必要配置，记录并验证飞书任务表链接。
- [sharpen](./skills/engineering/sharpen/SKILL.md)：深化任务要求并重写提示词，保持原有范围。
- [show-me-your-work](./skills/engineering/show-me-your-work/SKILL.md)：记录可审阅的决策轨迹，核验证据并开展独立评审。
- [statechart](./skills/engineering/statechart/SKILL.md)：检查 TLA+ 模型并生成状态图，展示违反规则的最短路径。
- [swarm](./skills/engineering/swarm/SKILL.md)：向独立子代理分派任务并汇总覆盖、竞速或探索结果。
- [tdd](./skills/engineering/tdd/SKILL.md)：用实际失败的行为测试或可执行复现驱动缺陷修复。
- [teach](./skills/engineering/teach/SKILL.md)：结合运行机制与历史原因，用易懂的方式讲解代码或变更。
- [technical-writing](./skills/engineering/technical-writing/SKILL.md)：用分层技术写作规范改进文档、方案、提交信息和评审说明。
- [typescript-best-practices](./skills/engineering/typescript-best-practices/SKILL.md)：在 TypeScript 代码中应用类型建模、边界校验和测试规范。
- [unslop](./skills/engineering/unslop/SKILL.md)：删除写作中的套话、冗余和常见 AI 表达模式。
- [why](./skills/engineering/why/SKILL.md)：从提交、评审和决策记录中解释设计原因与取舍。

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
