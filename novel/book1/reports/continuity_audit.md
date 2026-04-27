# 正文连续性审计

## 本次复核范围
- 范围：CH001-CH130 全部正本批次。
- 文件：CH001-CH012、CH013-CH020、CH021-CH025、CH026-CH030、CH031-CH080、CH081-CH130。
- 结果：已修复并通过全量校验。
- 全量校验：130 章，624,111 个 CJK 汉字，全部章节不低于 4000 个 CJK 汉字。
- 校验命令：python C:\Users\taotao\.codex\skills\shengtu-novel-production\scripts\validate_novel_batch.py E:\python_learn\shengtu\novel\book1\chapters\CH001-CH012.md E:\python_learn\shengtu\novel\book1\chapters\CH013-CH020.md E:\python_learn\shengtu\novel\book1\chapters\CH021-CH025.md E:\python_learn\shengtu\novel\book1\chapters\CH026-CH030.md E:\python_learn\shengtu\novel\book1\chapters\CH031-CH080.md E:\python_learn\shengtu\novel\book1\chapters\CH081-CH130.md --min-chapters 130 --min-chars 4000 --expect-start 1 --expect-end 130

## 查明的问题
1. CH001-CH030：多数章节低于当前 4000 汉字底线，需要扩写。
2. CH031-CH080：存在严重固定段落重复，旧文件中同类 filler 段大量重复，导致正文像换标题的模板。
3. CH081-CH130：存在断引、回声渠、路债旧契阶段错位与重复段落，宁折羽缺席/在场也曾有冲突风险。
4. 未跟踪 CH031-CH040.md：该文件是乱码残片，非正本，未纳入本次提交范围。
5. 根因：旧生产脚本使用固定段落模板与 filler 循环；旧 validator 只验字数和章号，没有检查重复长段落、重复段落前缀和剧情模板化。

## 修复措施
- 升级 shengtu-novel-production skill validator：新增重复长段落和重复段落前缀检查。
- CH001-CH030：扩写到合格字数，补足具体行动、可见代价、旧账翻动和下一章后果。
- CH031-CH130：重写修复，删除模板化重复段，按每章标题绑定本章行动、证物、代价、旧账和下一章后果。
- 全程未修改 worldbible 核心设定文件。

## 六项检查
1. 有没有违反仓库正典：未发现。本次只修正文产物与生产状态/审计，不改 worldbible 核心设定。
2. 有没有新增未确认核心设定：未发现新增宇宙级或世界级规则；新增内容限于正文层证物、行动、代价、旧账呈现。
3. 有没有把正文写成设定说明：未发现禁用说明词；validator 已检查相关术语。
4. 有没有章节低于 4000 汉字：无。CH001-CH130 全部通过。
5. 有没有角色开挂或阵营脸谱化：修复后继续保留沈行策受限、白鹿半句、守衡司与灰缄线复杂性、各角色功能代价。
6. 下一批必须承接的具体后果：CH131《卖路市》必须承接“旧师父”、米船渡旧契、第二页账、临约铜钉、祁渡川个人旧债、宁折羽失约线和共保会治理压力。

## 后续风险
- 这次修复解决了硬性字数、重复段落和明显连续性冲突，但仍建议在下一轮正文生产前抽样精修关键章，尤其 CH001、CH013、CH031、CH081、CH121 这些阶段入口章。
- 之后每批必须先跑新版 validator，不能再只看字数通过。
