# Angelo翻译工具 V1.0

**Android 多语言本地化自动化翻译工具** —— 专为 Android 项目打造的 **Excel 驱动** 一键批量翻译神器
<img width="1626" height="1071" alt="image" src="https://github.com/user-attachments/assets/da5a3264-0ac4-4cc9-8ecb-56f42b21992d" />

<img width="1626" height="1071" alt="image" src="https://github.com/user-attachments/assets/1dc8ccea-42a7-4c1d-b951-04da8bc57309" />

<img width="1626" height="1071" alt="image" src="https://github.com/user-attachments/assets/0e4a5b96-4be1-4ddb-8b04-32a9ae7699b5" />


<img width="1626" height="1071" alt="image" src="https://github.com/user-attachments/assets/0bd9f911-e430-40c9-a8c3-bce38c1b4c45" />


---

### 📖 项目简介

**Angelo翻译工具** 是一款专为 Android 开发者、翻译团队和多语言维护人员设计的**本地化（i18n）自动化工具**。

它以 **Excel 翻译表格** 为数据源，自动解析 Android 项目中 `res/` 目录下的所有 `strings.xml` 文件，实现**原文 → 目标语言**的一键批量翻译。同时自动创建或更新对应的语言资源文件夹（如 `values-zh-rTW`、`values-es-rMX` 等），并生成三份专业报告 Excel，极大提升多语言维护效率。

**核心价值**：
- 彻底告别手动复制粘贴和逐文件修改
- 解决翻译重复、不一致、缺失等问题
- 支持 30+ 种语言及区域变体，完全符合 Android 官方资源目录规范
- 界面友好、日志实时、多线程高效、容错性强

---

### ✨ 核心功能（详细说明）

1. **一键批量翻译**
   - 支持同时处理整个 Android 项目中所有 `strings.xml`
   - 自动识别 `values/`、`values-zh/`、`values-en/` 等源文件夹
   - 自动创建目标语言变体文件夹（如果不存在）

2. **智能翻译映射**
   - 精准匹配 Excel 中的原文（支持简体中文/英文作为参照语言）
   - 自动处理换行（单行最长 45 字符，防止布局溢出）
   - 保留原有 XML 格式、命名空间和注释

3. **重复翻译检测**
   - 自动检测同一原文在 Excel 不同 Sheet 中出现**不同译文**的情况
   - 记录来源 Sheet 和行号，便于人工校对

4. **翻译差异记录**
   - 对比旧译文与新译文，清晰记录每一个被修改的 Key

5. **文言缺失检测**
   - 扫描项目中所有已使用的 Key，找出 Excel 中**未提供翻译**的字符串
   - 去重后生成缺失报告

6. **高级特性**
   - 多线程处理（最高 4 线程 + Excel 保存独立线程）
   - 支持合并单元格、隐藏 Sheet、BOM 编码
   - 幂等设计：重复运行不会覆盖已有正确译文
   - 实时日志 + 进度条 + 完成弹窗提示

---

### 🌐 支持的语言（完整列表，共 30+ 种）

工具支持以下**所有语言及区域变体**，每个语言均对应 Android 标准资源文件夹：

| 语言代码     | 显示名称               | 资源文件夹变体                          |
|--------------|------------------------|-----------------------------------------|
| zh-cn        | 中文(简体)             | values-zh-rCN, values-zh                |
| en           | 英文                   | values-en-rUS, values-en, values-en-rGB |
| zh-tw        | 中文(繁体-台湾)        | values-zh-rTW                           |
| zh-hk        | 中文(繁体-香港)        | values-zh-rHK                           |
| th           | 泰语                   | values-th-rTH                           |
| de           | 德语                   | values-de-rDE, values-de                |
| fr           | 法语                   | values-fr-rFR                           |
| es           | 西班牙语               | values-es-rES, values-es                |
| es-MX        | 西班牙语(墨西哥)       | values-es-rMX                           |
| es-CL        | 西班牙语(智利)         | values-es-rCL                           |
| nl           | 荷兰语                 | values-nl-rNL                           |
| no           | 挪威语                 | values-no-rNO                           |
| da           | 丹麦语                 | values-da-rDK                           |
| sv           | 瑞典语                 | values-sv-rSE                           |
| it           | 意大利语               | values-it                               |
| pt           | 葡萄牙语               | values-pt-rPT                           |
| pt-BR        | 葡萄牙语(巴西)         | values-pt-rBR                           |
| el           | 希腊语                 | values-el-rGR                           |
| ar           | 阿拉伯语               | values-ar-rAE, values-ar, values-ar-rSA |
| tr           | 土耳其语               | values-tr-rTR                           |
| fi           | 芬兰语                 | values-fi-rFI                           |
| pl           | 波兰语                 | values-pl-rPL                           |
| uk           | 乌克兰语               | values-uk-rUA                           |
| ro           | 罗马尼亚语             | values-ro-rRO                           |
| cs           | 捷克语                 | values-cs-rCZ                           |
| hu           | 匈牙利语               | values-hu-rHU                           |
| sk           | 斯洛伐克语             | values-sk-rSK                           |
| sl           | 斯洛文尼亚语           | values-sl-rSI                           |
| hr           | 克罗地亚语             | values-hr-rHR                           |
| he           | 希伯来语               | values-he-rIL                           |
| vi           | 越南语                 | values-vi-rVN                           |
| ru           | 俄语                   | values-ru-rRU, values-ru                |
| sr           | 塞尔维亚语             | values-sr-rRS                           |
| bg           | 保加利亚语             | values-bg-rBG                           |
| et           | 爱沙尼亚语             | values-et-rEE                           |
| lv           | 拉脱维亚语             | values-lv-rLV                           |
| lt           | 立陶宛语               | values-lt-rLT                           |
| kk           | 哈萨克语               | values-kk-rKZ                           |
| ja           | 日语                   | values-ja-rJP                           |
| fa           | 波斯语                 | values-fa, values-fa-rIR                |
| tl           | 菲律宾语               | values-tl-rPH                           |

**参照语言**（Excel 原文列）：仅支持 **中文** 或 **英文**（可在界面切换）。

---

### 📋 Excel 翻译表格式要求

- 支持**多个 Sheet**（每个 Sheet 独立处理）
- 表头必须包含参照语言列（如“中文”或“英文”）和目标语言列（如“中文(繁体-台湾)”）
- 支持**语言别名**识别（例如“台繁”“繁中”“Taiwan Traditional”“繁体中文(台湾)”均可被识别）
- 支持**合并单元格**
- 推荐第一行为表头，后续行为原文 + 译文

---

### 📊 翻译完成后自动生成的报告

1. **翻译差异表**（Translate Diff）
   - 记录每个被修改的 Key
   - 包含：原文、旧译文、新译文、来源 App、Excel 来源页面

2. **翻译重复表**（Translate Same）
   - 同一原文在 Excel 中出现**不同译文**时触发
   - 详细记录所有冲突译文及来源 Sheet:行号

3. **文言缺失表**（Translate Loss）
   - 项目中存在但 Excel 未提供翻译的 Key
   - 包含：Key、原文、来源 App

---

### 🚀 快速开始（详细步骤）

1. 下载最新 Release（或克隆仓库）
2. 准备翻译 Excel 文件
3. 打开 `Angelo翻译工具.exe`
4. 点击 **选择工程目录**（Android 项目根目录）
5. 点击 **选择翻译文件**（你的 Excel）
6. 选择 **参照语言**（中文/英文）
7. 选择 **翻译语言**（目标语言）
8. 点击 **一键翻译**
9. 完成后查看生成的三个报告 Excel 并进行人工校对

---

### 欢迎商务洽谈

<img width="1206" height="2622" alt="f1f1a5ba8d34fe1cf9dbe8be2ec9c191" src="https://github.com/user-attachments/assets/98afae67-6c49-4456-afc2-49b3952f4aae" />

电话： 15342561548
邮箱 hk_wanghw@126.com

