"""
Generate the bilingual STEAMxDREAM iGEM brochure PDF.

Requires:
- pyfpdf / fpdf installed (already available in this environment)
- A writable font path that supports zh-TW characters.

Font note:
- We point to the system font Arial Unicode via a local symlink at
  docs/fonts_ArialUnicode.ttf to avoid writing cache files to /System.
- Do not commit proprietary fonts; keep the symlink untracked if needed.
"""

from pathlib import Path
from fpdf import FPDF

FONT_ALIAS = "ArialUnicode"
FONT_PATH = Path("docs/fonts_ArialUnicode.ttf")
PDF_PATH = Path("docs/igem-training-brochure.pdf")


def add_title(pdf: FPDF, text: str):
    pdf.set_font(FONT_ALIAS, size=18)
    pdf.multi_cell(0, 10, text)
    pdf.ln(2)


def add_h2(pdf: FPDF, text: str):
    pdf.set_font(FONT_ALIAS, size=15)
    pdf.multi_cell(0, 9, text)
    pdf.ln(1)


def add_h3(pdf: FPDF, text: str):
    pdf.set_font(FONT_ALIAS, size=13)
    pdf.multi_cell(0, 8, text)


def add_paragraph(pdf: FPDF, text: str, size: int = 12):
    pdf.set_font(FONT_ALIAS, size=size)
    pdf.multi_cell(0, 7, text)
    pdf.ln(1)


def add_bullets(pdf: FPDF, items, size: int = 12):
    pdf.set_font(FONT_ALIAS, size=size)
    for item in items:
        pdf.multi_cell(0, 7, f"• {item}")
    pdf.ln(2)


def new_section(pdf: FPDF):
    pdf.ln(3)


def build_pdf():
    if not FONT_PATH.exists():
        raise SystemExit(
            f"Missing font file at {FONT_PATH}. Create a symlink to a Unicode TTF (e.g., Arial Unicode) or swap in an open-source CJK font."
        )

    pdf = FPDF(format="A4")
    pdf.add_page()
    pdf.add_font(FONT_ALIAS, fname=str(FONT_PATH), uni=True)
    pdf.set_auto_page_break(auto=True, margin=15)

    # Cover
    add_title(pdf, "STEAMxDREAM 未來生物探索｜iGEM 國際基因工程機器大賽訓練營")
    add_title(pdf, "STEAMxD iGEM Navigator Program 2025–2026")
    add_paragraph(
        pdf,
        "對象：國三～高三學生（約 9–12 年級）｜授課方式：線上課程＋實體實驗室操作｜主辦單位：STEAMxDREAM｜訂位／諮詢專線：0909-009-985",
    )
    add_paragraph(pdf, "官方網站：【放上你的網址】")
    new_section(pdf)

    # 中文版
    add_h2(pdf, "一、課程與競賽介紹")
    add_h3(pdf, "什麼是 iGEM？")
    add_paragraph(
        pdf,
        "iGEM（International Genetically Engineered Machine）為由 MIT 起源、目前由 iGEM Foundation 主辦的國際合成生物學競賽。每年吸引來自全球數十個國家、數百支隊伍參與，包含 Harvard、MIT、Stanford 等世界級名校學生，是目前最具影響力的學生生物科技競賽之一。",
    )
    add_h3(pdf, "STEAMxDREAM iGEM 訓練營是什麼？")
    add_paragraph(pdf, "本訓練營專為國三至高三學生設計，從合成生物學基礎概念出發，一路帶領學生：")
    add_bullets(
        pdf,
        [
            "發想與設計屬於自己的 iGEM 專題",
            "學習實驗設計與實驗室操作",
            "建立數學建模與程式分析能力",
            "完成 Human Practices、商業與社會影響分析",
            "製作英文網站（wiki）、海報與簡報",
            "為參加 iGEM 國際總決賽做好準備",
        ],
    )

    add_h2(pdf, "二、適合對象與學習成果")
    add_h3(pdf, "適合誰參加？")
    add_bullets(
        pdf,
        [
            "對生命科學、生醫、藥學、生物科技有興趣的學生",
            "喜歡數學、統計、程式設計、AI 或資料科學的學生",
            "對品牌企劃、商業模式、永續與 ESG、社會議題有熱情的學生",
            "擅長設計、插畫、動畫、網頁或影像創作的學生",
            "有志未來申請生科、生醫、醫學、資工、商學、設計相關科系者",
        ],
    )
    add_h3(pdf, "完成課程後，你可以獲得：")
    add_bullets(
        pdf,
        [
            "了解合成生物學與基因工程的核心概念",
            "具備閱讀學術論文與查找資料的基本能力",
            "完整參與一個跨國研究型專題的經驗",
            "建立實驗設計、數據分析與建模的初步能力",
            "完成一套可放入作品集的英文專題成果（網站＋海報＋簡報）",
            "為未來申請海外大學與研究計畫累積具有說服力的實戰資歷",
        ],
    )

    add_h2(pdf, "三、課程架構與時程概覽")
    add_paragraph(pdf, "實際時數可依你之後的開課計畫微調，下面給的是結構模板。")
    add_bullets(
        pdf,
        [
            "課程期間：2025 年 11 月 ～ 2026 年 10 月（依 iGEM 官方時程調整）",
            "授課形式：線上課程（理論、建模與專題小組討論）；實體課程（實驗室操作、集訓營、模擬答辯）",
            "主要階段：基礎啟蒙與能力建立（約 8–10 週）；專題發想與實驗／建模設計（約 8–10 週）；專題執行與 Human Practices（約 10–16 週）；成果整理、wiki 建置與答辯準備（約 6–8 週）",
        ],
    )

    add_h2(pdf, "四、課程大綱（模組設計）– 中文版")
    modules_zh = [
        (
            "模組一｜合成生物學與 iGEM 入門",
            [
                "了解合成生物學的基本概念與應用範例",
                "認識 iGEM 的歷史、規則與評分架構",
                "拆解歷屆金牌隊伍的專題與成功關鍵",
                "介紹 BioBrick、標準化基因零件與設計思維",
            ],
        ),
        (
            "模組二｜實驗室安全與基礎技術（Wet Lab 基礎）",
            [
                "實驗室安全規範與個人防護",
                "移液、無菌操作、培養菌株等基本技術",
                "DNA 操作與簡單分子生物實驗示範",
                "如何整理實驗紀錄與撰寫 lab notebook",
            ],
        ),
        (
            "模組三｜數學建模與程式入門（Dry Lab 基礎）",
            [
                "建模在 iGEM 專題中的角色",
                "以 Python / R 進行簡單數據處理與視覺化",
                "常見動態系統與基因迴路的數學模型概念",
                "範例：如何用程式模擬簡單生物系統",
            ],
        ),
        (
            "模組四｜專題發想與問題定義",
            [
                "問題挖掘工作坊：從生活與世界議題中找題目",
                "如何閱讀文獻與整理背景資料",
                "定義專題目標、研究問題與假說",
                "建立初步實驗與建模架構",
            ],
        ),
        (
            "模組五｜Human Practices 與社會影響",
            [
                "什麼是 Human Practices？為什麼 iGEM 這麼重視？",
                "社會、倫理、政策與利害關係人分析",
                "訪談設計與問卷設計基礎",
                "將回饋與調查結果回饋到專題設計",
            ],
        ),
        (
            "模組六｜商業模式與永續策略（Business & Impact）",
            [
                "從商業角度看合成生物學與創新科技",
                "商業模式畫布（Business Model Canvas）入門",
                "ESG 與永續發展目標（SDGs）與專題連結",
                "撰寫簡易商業企畫與 Pitch Deck",
            ],
        ),
        (
            "模組七｜設計、品牌與數位內容",
            [
                "隊伍命名與品牌識別設計（Logo、色彩、風格）",
                "wiki 網站架構規劃與基本前端概念",
                "海報設計原則與視覺資訊呈現",
                "影片與社群內容企畫（選配）",
            ],
        ),
        (
            "模組八｜專題執行與進度管理",
            [
                "專題排程與里程碑設計",
                "每週進度檢視與問題排除討論",
                "實驗與建模結果的整合與迭代修正",
                "寫作與整理實驗結果（Figures / Tables / 敘述）",
            ],
        ),
        (
            "模組九｜英文簡報與 iGEM 答辯練習",
            [
                "英文科學簡報結構與說服力",
                "問答與臨場反應訓練",
                "模擬 iGEM 場景的 full rehearsal",
                "如何將 iGEM 經驗整理進 CV、Personal Statement 與作品集",
            ],
        ),
    ]
    for title, bullets in modules_zh:
        add_h3(pdf, title)
        add_bullets(pdf, bullets)

    add_h2(pdf, "五、指導團隊")
    add_paragraph(pdf, "建議 PDF 中每位老師配一張照片＋ 3–4 行簡短介紹。")
    add_bullets(
        pdf,
        [
            "Jeff｜合成生物學與空間轉錄體學；台灣大學 生化科技系、台大生醫電資所碩士（空間轉錄體學）；曾參與 NTU 2024 Graduate iGEM Team 並擔任 2025 年 iGEM 國際競賽評審；興趣含 LLM x 生醫、蛋白質序列分析、空間轉錄體數據。",
            "Peggy｜大型語言模型與數學建模；台灣大學 電機工程學系、台大電機所博士（研究主題：LLM）；ICML、NeurIPS 第一作者；專長數學建模、機器學習與 AI 生醫應用。",
            "Derrick｜臨床醫學與轉譯研究；成功大學醫學系、Harvard Medical School 博士後；代表成大參與 iGEM；擅長臨床需求評估、倫理考量與 Human Practices。",
            "Vivi｜國際政治、創投與 ESG 商業策略；紐約大學國際政治主修；創投與新創教練，擁有多張 ESG / 永續專業證照；專長 business plan、影響力敘事與 Pitch Deck。",
            "Will｜Bioinformatics 與資料科學；卡內基美隆大學碩士（Bioinformatics）；熟悉 NGS、單細胞、多組學與雲端運算，指導學生建立可重現的分析流程與模型驗證。",
            "Jason｜Biomedicine 與轉譯醫學；Johns Hopkins University 碩士（Biomedicine）；熟悉國際醫學研究流程與臨床前研究設計，協助學生將研究對齊生醫趨勢與倫理規範。",
        ],
    )

    add_h2(pdf, "六、報名資訊與流程")
    add_h3(pdf, "報名資格")
    add_bullets(
        pdf,
        [
            "國三～高三學生（含國際學校與雙語學校）",
            "具備基本英文閱讀能力（能看簡單英文文章與說明）",
            "無需有實驗或程式背景，但需願意投入與團隊合作",
        ],
    )
    add_h3(pdf, "費用說明")
    add_bullets(
        pdf,
        [
            "課程與指導費：NT$【自行填寫】",
            "實驗室操作與材料費：NT$【自行填寫】",
            "iGEM 官方註冊與報名費：約 NT$【自行填寫，依當年匯率與官方公告為準】",
            "Grand Jamboree 出國活動費用：NT$【自行填寫，依實際行程另行公告】",
        ],
    )
    add_h3(pdf, "報名流程")
    add_bullets(
        pdf,
        [
            "線上填寫報名表",
            "資料審查與線上／實體面試",
            "通過面試後，簽署科研指導協議並完成繳費",
            "發送錄取通知、課程時程表、預習教材與實驗室報到資訊",
        ],
    )
    add_h3(pdf, "聯絡方式")
    add_bullets(
        pdf,
        [
            "官方 Line / Email：［自行填寫］",
            "官方網站：［自行填寫］",
            "報名專線：0909-009-985",
        ],
    )

    # English version
    pdf.add_page()
    add_h2(pdf, "Program Overview")
    add_paragraph(pdf, "STEAMxDREAM iGEM Training Program 2025–2026｜International Genetically Engineered Machine (iGEM) Training Camp")
    add_paragraph(pdf, "The STEAMxDREAM iGEM Training Program is designed for motivated high school students (Grades 9–12) who are passionate about life sciences, engineering, computer science, design, or social impact.")
    add_paragraph(pdf, "Students will work in cross-disciplinary teams to:")
    add_bullets(
        pdf,
        [
            "Design and execute an original synthetic biology project",
            "Learn wet-lab and dry-lab skills required for iGEM",
            "Explore human practices, ethics, and business models",
            "Build a complete set of iGEM deliverables: wiki, poster, and presentation",
            "Prepare for the iGEM Grand Jamboree and for future university applications",
        ],
    )

    add_h2(pdf, "Target Students & Learning Outcomes")
    add_h3(pdf, "Who is this program for?")
    add_bullets(
        pdf,
        [
            "Students in Grades 9–12 (or equivalent)",
            "Interested in biology, biotechnology, medicine, chemistry, or life sciences",
            "OR interested in mathematics, statistics, computer science, data science, or AI",
            "OR interested in business, ESG, social innovation, or public policy",
            "OR interested in design, visual arts, animation, web design, or media production",
        ],
    )
    add_h3(pdf, "By the end of the program, students will:")
    add_bullets(
        pdf,
        [
            "Understand core concepts of synthetic biology and genetic engineering",
            "Gain hands-on experience with scientific projects and team-based research",
            "Learn basic lab skills, modeling techniques, and data analysis workflows",
            "Complete a full iGEM-style project with English deliverables",
            "Build strong materials for CVs, personal statements, and portfolios",
        ],
    )

    add_h2(pdf, "Program Structure & Timeline")
    add_paragraph(pdf, "Program Duration: approx. Nov 2025 – Oct 2026")
    add_paragraph(pdf, "Format: Online sessions (theory, modeling, project meetings) + On-site sessions (lab work, intensive bootcamps, mock presentations)")
    add_paragraph(pdf, "Main phases:")
    add_bullets(
        pdf,
        [
            "Foundations & Skill-building",
            "Project Ideation & Design",
            "Implementation & Human Practices",
            "Wiki, Documentation & Final Presentation",
        ],
    )

    add_h2(pdf, "Curriculum Outline (Modules)")
    modules_en = [
        (
            "Module 1｜Introduction to Synthetic Biology & iGEM",
            [
                "History and key concepts of synthetic biology",
                "What is iGEM? Tracks, rules, and judging criteria",
                "Case studies of award-winning iGEM teams",
                "Standard biological parts and genetic circuit design",
            ],
        ),
        (
            "Module 2｜Lab Safety & Wet-lab Fundamentals",
            [
                "Laboratory safety and personal protection",
                "Basic techniques: pipetting, sterile techniques, culture handling",
                "Introductory molecular biology experiments",
                "Lab notebooks and experimental documentation",
            ],
        ),
        (
            "Module 3｜Modeling & Programming for iGEM (Dry-lab Basics)",
            [
                "Role of mathematical modeling in iGEM projects",
                "Basic Python / R for data analysis and visualization",
                "Simple dynamical system models for genetic circuits",
                "Simulating biological systems with code",
            ],
        ),
        (
            "Module 4｜Project Ideation & Problem Definition",
            [
                "Problem-finding workshop: from real-world issues to project ideas",
                "Literature review and background research",
                "Defining project goals, research questions, and hypotheses",
                "Designing initial experimental and modeling plans",
            ],
        ),
        (
            "Module 5｜Human Practices & Societal Impact",
            [
                "What is Human Practices in iGEM?",
                "Ethics, policy, and stakeholder analysis",
                "Designing interviews and surveys",
                "Integrating feedback into project design",
            ],
        ),
        (
            "Module 6｜Business Models & Sustainability (Business & Impact)",
            [
                "Innovation and entrepreneurship in synthetic biology",
                "Introduction to Business Model Canvas",
                "ESG and SDGs in relation to the project",
                "Writing a simple business plan and pitch deck",
            ],
        ),
        (
            "Module 7｜Design, Branding & Digital Content",
            [
                "Team identity: naming, logo, and visual style",
                "Wiki structure design and basic front-end concepts",
                "Poster design and visual communication principles",
                "Optional: video and social media content planning",
            ],
        ),
        (
            "Module 8｜Project Execution & Management",
            [
                "Milestone planning and project management",
                "Weekly progress reviews and troubleshooting",
                "Integrating wet-lab and dry-lab results",
                "Writing figures, tables, and result summaries",
            ],
        ),
        (
            "Module 9｜English Presentation & iGEM Preparation",
            [
                "Structure of a scientific presentation",
                "Storytelling and persuasive communication",
                "Q&A practice and mock iGEM sessions",
                "Packaging iGEM experience into CVs, essays, and portfolios",
            ],
        ),
    ]
    for title, bullets in modules_en:
        add_h3(pdf, title)
        add_bullets(pdf, bullets)

    add_h2(pdf, "Mentors, Fees & Application")
    add_paragraph(pdf, "Pair each mentor with a photo and 3–4 line bio in the PDF or on the website.")
    add_bullets(
        pdf,
        [
            "Jeff｜Synthetic biology & spatial transcriptomics; B.S. Biochemical Science, NTU; M.S. Biomedical Electronics & Bioinformatics, NTU (spatial transcriptomics); NTU 2024 Graduate iGEM team; iGEM 2025 judge; interests in LLMs for biomed, protein sequence analysis, spatial transcriptomics data.",
            "Peggy｜Large language models & mathematical modeling; B.S. EE, NTU; Ph.D. EE, NTU (LLM research); first-author at ICML/NeurIPS; focuses on math modeling, ML, and AI for biomedical use cases.",
            "Derrick｜Clinical medicine & translational research; M.D., National Cheng Kung University; Postdoc, Harvard Medical School; former NCKU iGEM member; specializes in clinical needs, ethics, and Human Practices.",
            "Vivi｜Geopolitics, venture capital & ESG strategy; B.A. International Politics, NYU; VC/startup coach with multiple ESG certifications; mentors business plans, impact storytelling, and pitch decks.",
            "Will｜Bioinformatics & data science; M.S. Bioinformatics, Carnegie Mellon University; experienced with NGS, single-cell, multi-omics, and cloud pipelines; guides reproducible analytics and model validation.",
            "Jason｜Biomedicine & translational medicine; M.S. Biomedicine, Johns Hopkins University; familiar with international research workflows and preclinical study design; aligns projects with biomedical trends and ethics.",
        ],
    )
    add_paragraph(pdf, "Program Fee: TBD (to be announced by organizer)")
    add_paragraph(pdf, "iGEM Registration & Travel Costs: subject to official fees and travel plans")
    add_paragraph(pdf, "Application Steps:")
    add_bullets(
        pdf,
        [
            "Online application form",
            "Review & interview",
            "Admission result & enrollment",
            "Receive schedule, pre-reading package, and lab onboarding information",
        ],
    )

    pdf.output(str(PDF_PATH))
    print(f"Wrote {PDF_PATH}")


if __name__ == "__main__":
    build_pdf()
