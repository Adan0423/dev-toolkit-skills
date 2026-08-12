---
name: qoder-wiki
description: Qoder official documentation knowledge base, containing product introduction, user guide, feature configuration, extension capabilities, account pricing, and troubleshooting. Use this skill when the user asks questions related to Qoder (e.g., installation, usage, features, pricing, shortcuts, MCP, Skills, Quest Mode, Repo Wiki, etc.).
---

# Qoder Wiki

Qoder official documentation knowledge base, providing product usage guides and technical references. Synced on 2026-04-12 against `https://docs.qoder.com/zh` left navigation.

## Usage

1. First check [INDEX.md](INDEX.md) to get the document index and content overview.
2. Locate the relevant documents based on the user's question.
3. Use the Read tool to read the corresponding document under the `docs/` directory.
4. If the document information is insufficient, consider searching the web to supplement.

## Document Structure

```
docs/
├── QuickStart/          # Product overview, installation & login, quick start
├── UserGuide/           # Models, Ask/Agent/Experts, Tools, Quest, NEXT, Repo Wiki
├── Context/             # Codebase index, @ Mention, rules, memory
├── Extensions/          # Skills, Commands, Custom Agents, MCP, Hooks, Deeplinks
├── Configuration/       # Shortcuts, network proxy
├── Account/             # Pricing, Credits, billing, Teams
├── Events/              # Referral program, referral terms, model campaigns, limited-time offers
├── Support/             # FAQ, troubleshooting, MCP FAQ
└── OtherProducts/       # JetBrains plugin, CLI, QoderWork overview
```

## Common Question Categories

| Question Type | Reference Document |
|---------|---------|
| What is Qoder | docs/QuickStart/Product-Overview.md |
| How to install and use | docs/QuickStart/Quick-Start.md |
| Smart chat/Agent mode | docs/UserGuide/Smart-Chat-Overview.md |
| Ask / Agent / Experts | docs/UserGuide/Ask-Mode.md, docs/UserGuide/Agent-Mode.md, docs/UserGuide/Experts-Mode.md |
| Model selection/Custom model | docs/UserGuide/Model-Selector.md, docs/UserGuide/Custom-Models.md |
| Quest Mode | docs/UserGuide/Quest-Mode.md |
| Code completion NEXT | docs/UserGuide/Inline-Suggestions-NEXT.md |
| Inline chat / Diff / Tools | docs/UserGuide/Inline-Chat.md, docs/UserGuide/Diff-View.md, docs/UserGuide/Tools.md |
| MCP Configuration | docs/Extensions/MCP.md |
| Skills Usage | docs/Extensions/Skills.md |
| Hooks Configuration | docs/Extensions/Hooks.md |
| Custom Rules | docs/Context/Rules.md |
| Shortcuts | docs/Configuration/Shortcuts.md |
| Pricing plans | docs/Account/Pricing.md, docs/Account/Pricing-Alternative.md (Check both!) |
| Teams organization edition | docs/Account/Teams-Pricing.md, docs/Account/Getting-Started-with-Teams.md, docs/Account/Members-and-Roles.md |
| CLI / JetBrains / QoderWork | docs/OtherProducts/CLI-Quick-Start.md, docs/OtherProducts/JetBrains-Plugin-Overview.md, docs/OtherProducts/QoderWork-Overview.md |
| Troubleshooting | docs/Support/FAQ.md, docs/Support/Troubleshooting-Guide.md |
