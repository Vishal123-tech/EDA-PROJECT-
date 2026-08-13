# -*- coding: utf-8 -*-
"""Generates 'Semiconductor-EDA-Code-Guide.pdf' — a full walkthrough of the
notebook's code with plain-English explanations of every block."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Preformatted, Spacer,
                                PageBreak, ListFlowable, ListItem, HRFlowable, Table, TableStyle)

OUT = r"C:\Users\vy355\OneDrive\Desktop\archive\Semiconductor-EDA-Code-Guide.pdf"

# ---- palette (matches the notebook's house style) ----
INK   = HexColor("#0b0b0b"); SOFT = HexColor("#52514e"); MUTED = HexColor("#898781")
BLUE  = HexColor("#2a78d6"); VIOLET = HexColor("#4a3aa7"); AQUA = HexColor("#1baf7a")
CODEBG = HexColor("#f4f4f2"); RULE = HexColor("#e1e0d9")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="Helvetica-Bold",
                    fontSize=17, textColor=BLUE, spaceBefore=6, spaceAfter=8, leading=21)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName="Helvetica-Bold",
                    fontSize=12.5, textColor=VIOLET, spaceBefore=12, spaceAfter=5, leading=16)
BODY = ParagraphStyle("Body", parent=ss["BodyText"], fontName="Helvetica",
                      fontSize=9.8, textColor=INK, leading=14.5, spaceAfter=6, alignment=TA_LEFT)
BULLET = ParagraphStyle("Bullet", parent=BODY, leftIndent=6, spaceAfter=2.5, leading=13.5)
CODE = ParagraphStyle("Code", parent=ss["Code"], fontName="Courier", fontSize=7.2,
                      textColor=HexColor("#14324f"), leading=9.4, backColor=CODEBG,
                      borderPadding=(6, 6, 6, 6), spaceBefore=2, spaceAfter=8, leftIndent=2)
CAP = ParagraphStyle("Cap", parent=BODY, fontSize=8.6, textColor=MUTED, spaceAfter=10)

flow = []


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def h1(t): flow.append(Paragraph(esc(t), H1))
def h2(t): flow.append(Paragraph(esc(t), H2))
def body(t): flow.append(Paragraph(t, BODY))
def cap(t): flow.append(Paragraph(esc(t), CAP))
def code(t): flow.append(Preformatted(esc(t.strip("\n")), CODE))
def gap(h=6): flow.append(Spacer(1, h))
def rule(): flow.append(HRFlowable(width="100%", thickness=0.6, color=RULE,
                                   spaceBefore=4, spaceAfter=8))


def bullets(items):
    lis = [ListItem(Paragraph(t, BULLET), value="•", leftIndent=10) for t in items]
    flow.append(ListFlowable(lis, bulletType="bullet", start="•",
                             leftIndent=8, bulletFontSize=8))


# ============================================================ COVER
flow.append(Spacer(1, 1.5 * inch))
flow.append(Paragraph("Global Semiconductor Industry", ParagraphStyle(
    "T", parent=H1, fontSize=26, textColor=INK, alignment=TA_CENTER, leading=30)))
flow.append(Paragraph("Exploratory Data Analysis (2010&ndash;2026)", ParagraphStyle(
    "T2", parent=H1, fontSize=16, textColor=BLUE, alignment=TA_CENTER, leading=20, spaceAfter=24)))
flow.append(Paragraph("Complete Code Guide", ParagraphStyle(
    "T3", parent=H2, fontSize=15, textColor=VIOLET, alignment=TA_CENTER, spaceAfter=40)))
flow.append(Paragraph(
    "A block-by-block walkthrough of the Python code behind the notebook &mdash; "
    "what every line does, why it is written that way, and the data-visualisation "
    "principles it follows.",
    ParagraphStyle("sub", parent=BODY, alignment=TA_CENTER, fontSize=11,
                   textColor=SOFT, leading=16)))
flow.append(Spacer(1, 0.5 * inch))
flow.append(Paragraph("Notebook: global-semiconductor-eda.ipynb  &bull;  Library stack: "
                      "pandas, numpy, matplotlib",
                      ParagraphStyle("sub2", parent=CAP, alignment=TA_CENTER)))
flow.append(PageBreak())

# ============================================================ 0. OVERVIEW
h1("1.  What this notebook does")
body("The notebook is an <b>exploratory data analysis (EDA)</b> of five linked CSV files that "
     "together describe the global semiconductor industry from 2010 to 2026. The goal is to turn "
     "raw tables into a visual story in five acts:")
bullets([
    "<b>Industry scale &amp; leaders</b> &mdash; total revenue, split by business model, and the top companies.",
    "<b>The AI-chip boom</b> &mdash; accelerator revenue by vendor, market concentration, and compute growth.",
    "<b>Price dynamics</b> &mdash; memory price cycles vs. data-centre GPU prices.",
    "<b>The fab-capacity race</b> &mdash; wafer capacity by country and the leading-edge share.",
    "<b>Geopolitics</b> &mdash; export-control actions over time and by imposing country.",
])
body("Every chart is produced with <b>matplotlib</b>; the data wrangling is done with "
     "<b>pandas</b>. The code is organised as one <i>setup</i> cell followed by one code cell per "
     "chart. The rest of this guide explains each of those cells in order.")

h2("The five datasets")
data = [
    ["File", "Rows", "What it holds"],
    ["chip_companies_financials.csv", "617", "Revenue, margins, R&D, capex by company/segment/country"],
    ["fab_capacity.csv", "313", "Monthly wafer capacity by company, country, process node"],
    ["chip_prices.csv", "405", "Monthly prices: DRAM, NAND, HBM3, NVIDIA H100/B200"],
    ["ai_chip_market.csv", "120", "AI-chip shipments, ASP, revenue, TFLOPS, TDP"],
    ["export_controls.csv", "34", "Export-control actions with a 1-10 severity score"],
]
t = Table(data, colWidths=[2.15 * inch, 0.5 * inch, 3.75 * inch])
t.setStyle(TableStyle([
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 8.5),
    ("FONT", (0, 1), (-1, -1), "Helvetica", 8.3),
    ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
    ("BACKGROUND", (0, 0), (-1, 0), BLUE),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), CODEBG]),
    ("GRID", (0, 0), (-1, -1), 0.4, RULE),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 5), ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
]))
flow.append(t)
flow.append(PageBreak())

# ============================================================ SETUP CELL
h1("2.  The setup cell &mdash; imports, style system, data loading")
body("This first code cell runs once and prepares everything the charts need: libraries, a small "
     "reusable colour/style system, a portable data loader, and the five DataFrames.")

h2("2.1  Imports")
code(
"import os, glob, warnings\n"
"import numpy as np\n"
"import pandas as pd\n"
"import matplotlib.pyplot as plt\n"
"import matplotlib.ticker as mticker\n"
"from matplotlib.lines import Line2D\n"
"warnings.filterwarnings(\"ignore\")")
bullets([
    "<b>os, glob</b> &mdash; build file paths and <i>discover</i> where the data lives (used by the loader).",
    "<b>numpy (np)</b> &mdash; fast numeric arrays; used for the stacked-bar baseline accumulator.",
    "<b>pandas (pd)</b> &mdash; the workhorse: reads CSVs and does all grouping/reshaping.",
    "<b>matplotlib.pyplot (plt)</b> &mdash; draws every figure.",
    "<b>matplotlib.ticker (mticker)</b> &mdash; formats axis numbers (e.g. adds the &lsquo;$&rsquo; and &lsquo;B&rsquo;).",
    "<b>warnings.filterwarnings(\"ignore\")</b> &mdash; hides harmless library warnings so the output stays clean.",
])

h2("2.2  A tiny design system (colours)")
body("Rather than pick colours ad-hoc per chart, the notebook defines them <i>once</i>. This keeps "
     "every figure visually consistent and colourblind-safe.")
code(
"INK      = \"#0b0b0b\"   # primary text\n"
"INK_SOFT = \"#52514e\"   # secondary text\n"
"MUTED    = \"#898781\"   # axis / tick labels\n"
"GRID     = \"#e1e0d9\"   # hairline gridlines\n"
"SURFACE  = \"#fcfcfb\"   # chart background\n"
"CAT = [\"#2a78d6\", \"#1baf7a\", \"#eda100\", \"#008300\",\n"
"       \"#4a3aa7\", \"#e34948\", \"#e87ba4\", \"#eb6834\"]\n"
"BLUE, AQUA, YELLOW, GREEN, VIOLET, RED, MAGENTA, ORANGE = CAT\n"
"BLUE_RAMP = [\"#cde2fb\",\"#9ec5f4\",\"#6da7ec\",\"#3987e5\",\"#2a78d6\",\"#1c5cab\",\"#104281\"]")
bullets([
    "<b>INK / INK_SOFT / MUTED / GRID / SURFACE</b> &mdash; the neutral &lsquo;ink &amp; paper&rsquo; tones for text, axes and background.",
    "<b>CAT</b> &mdash; eight categorical hues in a <i>fixed order</i>. The order is chosen so neighbouring colours stay distinguishable for colour-blind readers.",
    "The unpacking line gives each hue a readable name (BLUE, AQUA, &hellip;) so the plotting code reads clearly.",
    "<b>BLUE_RAMP</b> &mdash; a single-hue light&rarr;dark ramp used when a colour must encode <i>magnitude</i> rather than identity.",
])

h2("2.3  Global chart defaults")
code(
"plt.rcParams.update({\n"
"    \"figure.facecolor\": SURFACE, \"axes.facecolor\": SURFACE,\n"
"    \"font.family\": [\"Segoe UI\", \"DejaVu Sans\", \"sans-serif\"], \"font.size\": 11,\n"
"    \"text.color\": INK, \"axes.labelcolor\": INK_SOFT, \"axes.edgecolor\": \"#c3c2b7\",\n"
"    \"xtick.color\": MUTED, \"ytick.color\": MUTED, \"axes.linewidth\": 0.8,\n"
"    \"figure.dpi\": 110, \"axes.titlesize\": 14, \"axes.titleweight\": \"bold\",\n"
"})")
body("<b>rcParams</b> is matplotlib&rsquo;s global settings dictionary. Setting it once means every "
     "chart automatically shares the same background, font, colours, and resolution &mdash; no need to "
     "repeat styling in each cell.")

h2("2.4  The style() helper")
body("Every chart calls this one function to apply consistent &lsquo;chrome&rsquo; (the frame, grid, "
     "title and labels), so the styling logic lives in a single place.")
code(
"def style(ax, title=None, sub=None, ylab=None, xlab=None):\n"
"    for s in (\"top\", \"right\"):\n"
"        ax.spines[s].set_visible(False)        # remove box top/right\n"
"    for s in (\"left\", \"bottom\"):\n"
"        ax.spines[s].set_color(\"#c3c2b7\")       # soften remaining axes\n"
"    ax.grid(axis=\"y\", color=GRID, linewidth=0.8, zorder=0)\n"
"    ax.set_axisbelow(True)                      # grid sits BEHIND the data\n"
"    if title:\n"
"        ax.set_title(title, loc=\"left\", color=INK, pad=14 if sub else 8)\n"
"    if sub:                                     # small grey subtitle\n"
"        ax.text(0, 1.015, sub, transform=ax.transAxes, ha=\"left\",\n"
"                va=\"bottom\", color=MUTED, fontsize=10.5)\n"
"    if ylab: ax.set_ylabel(ylab, color=INK_SOFT)\n"
"    if xlab: ax.set_xlabel(xlab, color=INK_SOFT)\n"
"    ax.tick_params(length=0)                    # hide tick marks\n"
"    return ax")
bullets([
    "Removes the top and right <b>spines</b> (the box lines) for a lighter, modern look.",
    "Draws a faint horizontal <b>grid</b> and pushes it <i>behind</i> the data with set_axisbelow(True).",
    "Left-aligns the <b>title</b> and adds an optional grey <b>subtitle</b> just above the plot using axes-fraction coordinates (transform=ax.transAxes).",
    "Optionally sets the y/x axis labels and hides the little tick marks. Returns the axis so calls can be chained.",
])

h2("2.5  Portable data loading")
body("The same notebook must run both on your machine and on Kaggle, where the data appears under "
     "<font face='Courier'>/kaggle/input/&hellip;</font>. This helper probes several likely locations "
     "and returns the first that contains a known file.")
code(
"def find_data_dir():\n"
"    candidates = glob.glob(\"/kaggle/input/*/\") + [\n"
"        \"/kaggle/input/global-semiconductor-industry-2010-2026\", \".\",\n"
"    ]\n"
"    for c in candidates:\n"
"        if os.path.exists(os.path.join(c, \"chip_companies_financials.csv\")):\n"
"            return c\n"
"    return \".\"\n"
"\n"
"DATA = find_data_dir()\n"
"fin    = pd.read_csv(os.path.join(DATA, \"chip_companies_financials.csv\"))\n"
"ai     = pd.read_csv(os.path.join(DATA, \"ai_chip_market.csv\"))\n"
"prices = pd.read_csv(os.path.join(DATA, \"chip_prices.csv\"))\n"
"fab    = pd.read_csv(os.path.join(DATA, \"fab_capacity.csv\"))\n"
"ctrl   = pd.read_csv(os.path.join(DATA, \"export_controls.csv\"))")
bullets([
    "<b>glob.glob(\"/kaggle/input/*/\")</b> lists every mounted dataset folder on Kaggle.",
    "The loop returns the first folder that actually contains the financials CSV; locally that resolves to \".\" (the current folder).",
    "<b>pd.read_csv</b> loads each file into a DataFrame &mdash; a table you can group, filter and reshape. The five variables (fin, ai, prices, fab, ctrl) are reused by every later cell.",
])
flow.append(PageBreak())

# ============================================================ SECTION 1
h1("3.  Section 1 &mdash; industry scale &amp; leaders")

h2("3.1  Total revenue over time (area + line)")
code(
"by_year = fin.groupby(\"year\")[\"revenue_usd_bn\"].sum()\n"
"\n"
"fig, ax = plt.subplots(figsize=(10, 4.6))\n"
"ax.fill_between(by_year.index, by_year.values, color=BLUE, alpha=0.12)   # soft area\n"
"ax.plot(by_year.index, by_year.values, color=BLUE, lw=2.4)              # the line\n"
"ax.scatter([by_year.index[-1]], [by_year.values[-1]], color=BLUE, s=36) # end dot\n"
"ax.yaxis.set_major_formatter(\n"
"    mticker.FuncFormatter(lambda v, _: f\"${v:,.0f}B\"))                  # $1,151B\n"
"style(ax, \"Total tracked semiconductor revenue\", \"2010-2026\", ylab=\"Revenue\")\n"
"\n"
"cagr = (by_year.values[-1] / by_year.values[0]) ** (1/(len(by_year)-1)) - 1")
bullets([
    "<b>groupby(\"year\").sum()</b> collapses 617 company-rows into one revenue total per year.",
    "<b>fill_between</b> paints a translucent area under the line; <b>plot</b> draws the line; <b>scatter</b> marks the final point. Together they give a clean &lsquo;area chart with emphasis&rsquo;.",
    "<b>FuncFormatter</b> with a lambda rewrites raw axis numbers as currency (the <font face='Courier'>:,.0f</font> adds thousands separators, no decimals).",
    "<b>CAGR</b> = compound annual growth rate: the constant yearly rate that turns the first value into the last over N-1 steps.",
])

h2("3.2  Revenue by business model (stacked area)")
code(
"def family(seg):\n"
"    if seg == \"foundry\":            return \"Foundry\"\n"
"    if seg == \"eda_software\":       return \"EDA tools\"\n"
"    if seg.startswith(\"fabless\"):   return \"Fabless\"\n"
"    if seg.startswith(\"idm\"):       return \"IDM\"\n"
"    if seg.startswith(\"equipment\"): return \"Equipment\"\n"
"    return \"Other\"\n"
"fin[\"family\"] = fin[\"segment\"].map(family)\n"
"\n"
"fam_year = (fin.groupby([\"year\", \"family\"])[\"revenue_usd_bn\"].sum()\n"
"              .unstack(\"family\").fillna(0))\n"
"ax.stackplot(fam_year.index, [fam_year[c].values for c in order],\n"
"             labels=order, colors=[colors[c] for c in order])")
bullets([
    "The raw data has 20 fine-grained segments. <b>family()</b> collapses them into five readable groups; <b>.map()</b> applies it to every row.",
    "<b>groupby([...]).sum().unstack(\"family\")</b> pivots the data into a year &times; family grid; <b>fillna(0)</b> replaces missing combinations with zero.",
    "<b>stackplot</b> stacks the five families so the top edge equals total revenue and each band shows one group&rsquo;s contribution. Colours come from the fixed categorical palette.",
])

h2("3.3  Top 15 companies (horizontal bars)")
code(
"latest = fin[fin.year == fin.year.max()].nlargest(15, \"revenue_usd_bn\")[::-1]\n"
"bars = ax.barh(latest[\"company_name\"], latest[\"revenue_usd_bn\"], color=BLUE)\n"
"bars[-1].set_color(VIOLET)                       # highlight the leader\n"
"for b, v in zip(bars, latest[\"revenue_usd_bn\"]):\n"
"    ax.text(b.get_width() + 1.5, b.get_y() + b.get_height()/2,\n"
"            f\"${v:,.0f}B\", va=\"center\")           # value label at bar end")
bullets([
    "<b>fin.year == fin.year.max()</b> keeps only the latest year; <b>nlargest(15, ...)</b> selects the 15 biggest companies.",
    "<b>[::-1]</b> reverses the order so the largest bar ends up on top in a horizontal chart.",
    "Because bars encode a <i>ranking</i> (magnitude, not identity) they use one hue; the single leader is re-coloured to draw the eye. The loop writes each value at the end of its bar.",
])

h2("3.4  R&amp;D vs capex (two lines, one axis)")
code(
"inv = fin.groupby(\"year\")[[\"rd_spend_usd_bn\", \"capex_usd_bn\"]].sum()\n"
"ax.plot(inv.index, inv[\"capex_usd_bn\"],   color=AQUA, marker=\"o\", label=\"Capex\")\n"
"ax.plot(inv.index, inv[\"rd_spend_usd_bn\"], color=BLUE, marker=\"o\", label=\"R&D spend\")\n"
"ax.legend(loc=\"upper left\", frameon=False)")
bullets([
    "Both measures are summed per year and drawn as two lines on the <b>same y-axis</b>. They share the same unit ($B), so a second axis is deliberately avoided &mdash; dual-axis charts distort comparisons.",
    "Distinct palette colours plus a <b>legend</b> identify the two series without relying on colour alone.",
])
flow.append(PageBreak())

# ============================================================ SECTION 2
h1("4.  Section 2 &mdash; the AI-chip boom")

h2("4.1  Revenue by vendor (top 5 + Other)")
code(
"rev = ai.groupby([\"year\",\"vendor\"])[\"estimated_revenue_usd_m\"].sum()\\\n"
"        .unstack(\"vendor\").fillna(0)\n"
"totals = rev.sum().sort_values(ascending=False)\n"
"top = list(totals.head(5).index)               # 5 biggest vendors overall\n"
"rev_plot = rev[top].copy()\n"
"rev_plot[\"Other\"] = rev.drop(columns=top).sum(axis=1)   # rest -> 'Other'\n"
"pal = {name: CAT[i] for i, name in enumerate(top)}       # fixed entity->colour\n"
"pal[\"Other\"] = MUTED\n"
"ax.stackplot(rev_plot.index, [rev_plot[s].values/1000 for s in series], ...)")
bullets([
    "There are 11 vendors &mdash; too many for a readable stack. The code keeps the <b>top 5 by total revenue</b> and merges the rest into a grey <b>&lsquo;Other&rsquo;</b> band.",
    "<b>pal</b> maps each vendor to a fixed palette slot, so a vendor keeps the <i>same colour</i> in every chart (colour follows the entity, never its rank).",
    "Dividing by 1000 converts $millions to $billions for the axis.",
])

h2("4.2  Market concentration (leader&rsquo;s share)")
code(
"share = rev.div(rev.sum(axis=1), axis=0) * 100   # each vendor's % of the year\n"
"leader = totals.index[0]                          # biggest vendor overall\n"
"ax.plot(share.index, share[leader].values, color=BLUE, marker=\"o\")\n"
"ax.axhline(50, color=MUTED, ls=(0, (4, 4)))       # 50% reference line\n"
"ax.set_ylim(0, 100)")
bullets([
    "<b>rev.div(rev.sum(axis=1), axis=0)</b> divides every cell by its row total, converting revenue into each vendor&rsquo;s yearly market share.",
    "Only the leader&rsquo;s share is plotted; a dashed <b>axhline</b> at 50% gives a &lsquo;majority of the market&rsquo; reference. Fixing y to 0-100 keeps the scale honest.",
])

h2("4.3  Frontier compute (log scale)")
code(
"ai[\"launch_year\"] = pd.to_datetime(ai[\"launch_date\"]).dt.year\n"
"frontier = ai.groupby(\"launch_year\")[\"fp16_tflops\"].max()\n"
"ax.plot(frontier.index, frontier.values, color=VIOLET, marker=\"o\")\n"
"ax.set_yscale(\"log\")")
bullets([
    "<b>pd.to_datetime(...).dt.year</b> extracts the launch year from a date string.",
    "<b>groupby(...).max()</b> takes the single most powerful chip launched each year (the &lsquo;frontier&rsquo;).",
    "<b>set_yscale(\"log\")</b> uses a logarithmic axis so exponential growth (which spans several orders of magnitude) shows as a roughly straight line.",
])
flow.append(PageBreak())

# ============================================================ SECTION 3
h1("5.  Section 3 &mdash; price dynamics")
body("Product prices span five orders of magnitude (a $2 DRAM chip vs. a $30,000 GPU). Two "
     "techniques let us compare them fairly: <b>indexing to a common base</b>, and a <b>log scale</b>.")

h2("5.1  Indexed price trends (base = 100)")
code(
"prices[\"date\"] = pd.to_datetime(prices[\"year_month\"] + \"-01\")\n"
"for prod, g in prices.groupby(\"product\"):\n"
"    g = g.sort_values(\"date\")\n"
"    idx = g[\"price\"].values / g[\"price\"].values[0] * 100   # first month = 100\n"
"    ax.plot(g[\"date\"], idx, color=pcolor.get(name, MUTED), label=name)\n"
"    ax.annotate(name, (g[\"date\"].values[-1], idx[-1]), ...)  # label at line end")
bullets([
    "Each product&rsquo;s price is divided by its <i>first</i> value and &times;100, so every series starts at 100. Now the lines show <b>relative change</b>, letting cheap memory and pricey GPUs share one axis.",
    "The loop draws one line per product and writes the product name directly at the end of its line (<b>direct labelling</b> is easier to read than a legend for line charts).",
])

h2("5.2  Latest price on a log scale")
code(
"latest_px = (prices.sort_values(\"date\").groupby(\"product\").tail(1)\n"
"             .sort_values(\"price\"))\n"
"bars = ax.barh(latest_px[\"name\"], latest_px[\"price\"])\n"
"ax.set_xscale(\"log\")\n"
"ax.text(..., f\"${v:,.0f}\" if v >= 100 else f\"${v:,.2f}\")   # smart formatting")
bullets([
    "<b>groupby(\"product\").tail(1)</b> keeps each product&rsquo;s most recent price after sorting by date.",
    "A <b>log x-axis</b> compresses the huge range so a $2 chip and a $30,000 GPU both fit on one readable chart.",
    "The conditional f-string shows cents for cheap items and whole dollars for expensive ones.",
])
flow.append(PageBreak())

# ============================================================ SECTION 4
h1("6.  Section 4 &mdash; the fab-capacity race")

h2("6.1  Capacity by country (stacked area)")
code(
"iso = {\"TWN\":\"Taiwan\", \"KOR\":\"South Korea\", \"USA\":\"United States\", ...}\n"
"fab[\"country\"] = fab[\"country_iso3\"].map(iso).fillna(fab[\"country_iso3\"])\n"
"cap = fab.groupby([\"year\",\"country\"])[\"monthly_wafer_capacity\"].sum()\\\n"
"        .unstack(\"country\").fillna(0)\n"
"topc = list(cap.sum().sort_values(ascending=False).head(5).index)\n"
"capp = cap[topc].copy(); capp[\"Other\"] = cap.drop(columns=topc).sum(axis=1)")
bullets([
    "<b>iso</b> maps 3-letter country codes to full names; <b>.map(...).fillna(...)</b> keeps the code if a name is missing.",
    "Same &lsquo;top 5 + Other&rsquo; pattern as the vendor chart, so the stack stays legible.",
    "Values are later divided by 1,000,000 to show <i>millions</i> of wafers per month.",
])

h2("6.2  Leading-edge capacity and its share")
code(
"leading = fab[(fab[\"process_node_nm\"] <= 7) & (fab[\"year\"] == fab[\"year\"].max())]\n"
"le = leading.groupby(\"country\")[\"monthly_wafer_capacity\"].sum().sort_values()\n"
"\n"
"fab[\"is_leading\"] = fab[\"process_node_nm\"] <= 7        # boolean flag\n"
"node_year = fab.groupby([\"year\",\"is_leading\"])[\"monthly_wafer_capacity\"].sum()\\\n"
"              .unstack().fillna(0)\n"
"share_le = node_year[True] / node_year.sum(axis=1) * 100")
bullets([
    "A process node &le; 7 nm counts as <b>leading-edge</b> (the most advanced chips). The first block ranks countries by leading-edge capacity in the latest year.",
    "<b>is_leading</b> is a True/False column; grouping on it splits capacity into leading vs. mature, and the ratio gives the leading-edge <b>share</b> over time.",
])
flow.append(PageBreak())

# ============================================================ SECTION 5
h1("7.  Section 5 &mdash; geopolitics")

h2("7.1  Export-control timeline (stem plot)")
code(
"ctrl[\"date\"] = pd.to_datetime(ctrl[\"date\"])\n"
"imp_color = {\"USA\": BLUE, \"NLD\": ORANGE, \"CHN\": RED}\n"
"for country, g in ctrl.groupby(\"imposing_country\"):\n"
"    ax.vlines(g[\"date\"], 0, g[\"severity_score\"], color=imp_color[country])\n"
"    ax.scatter(g[\"date\"], g[\"severity_score\"], color=imp_color[country],\n"
"               label=imp_name[country])")
bullets([
    "Each action is drawn as a <b>stem</b>: <b>vlines</b> makes the vertical stalk from 0 up to the severity score, and <b>scatter</b> puts a dot on top.",
    "Grouping by imposing country and colouring by a fixed map (USA / Netherlands / China) shows at a glance who is driving the controls.",
])

h2("7.2  Actions per year (manual stacked bars)")
code(
"cnt = ctrl.groupby([\"year\",\"imposing_country\"]).size()\\\n"
"        .unstack(\"imposing_country\").fillna(0)\n"
"bottom = np.zeros(len(cnt))\n"
"for country in cnt.columns:\n"
"    ax.bar(cnt.index, cnt[country], bottom=bottom, color=imp_color[country])\n"
"    bottom += cnt[country].values          # raise the base for the next layer")
bullets([
    "<b>.size()</b> counts rows per (year, country) pair; unstacking makes a year &times; country grid of counts.",
    "Stacked bars are built by hand: each country is drawn starting at <b>bottom</b>, then <b>bottom</b> is raised by that country&rsquo;s counts so the next layer sits on top.",
])

# ============================================================ PRINCIPLES
flow.append(PageBreak())
h1("8.  The design principles behind every chart")
body("The styling is not decoration &mdash; it follows a small set of data-visualisation rules that "
     "make the charts accurate and accessible:")
bullets([
    "<b>Colour by job.</b> Identity &rarr; fixed categorical hues; magnitude &rarr; one-hue ramp or a single colour. Colours are never cycled by rank.",
    "<b>One axis, never two y-scales.</b> Series with different units are compared by <i>indexing to a common base</i> or shown as separate charts (see the price section).",
    "<b>Colour follows the entity.</b> NVIDIA is the same blue in every chart; a filter that changes the number of series never repaints the survivors.",
    "<b>Log scale for wide ranges.</b> Used for frontier compute and unit prices, which span several orders of magnitude.",
    "<b>Recessive chrome.</b> Thin, soft axes; a faint grid behind the data; no chart-junk. The data is the loudest thing on the page.",
    "<b>Direct labelling.</b> Line ends and bar ends are labelled in place, reducing reliance on legends and colour alone.",
    "<b>Top-N + &lsquo;Other&rsquo;.</b> When a category has too many values, keep the largest few and pool the rest, so stacks stay readable.",
])

h1("9.  Running and publishing the notebook")
h2("9.1  Run it locally")
code(
"python -m nbconvert --to notebook --execute --inplace \\\n"
"    global-semiconductor-eda.ipynb")
body("This executes every cell and saves the rendered charts back into the .ipynb file.")

h2("9.2  Publish to Kaggle")
code(
"python -m kaggle kernels push -p \\\n"
"    \"C:\\Users\\vy355\\OneDrive\\Desktop\\archive\\kernel\"")
body("The <font face='Courier'>kernel</font> folder holds the notebook plus a "
     "<font face='Courier'>kernel-metadata.json</font> file that tells Kaggle the title, that it is "
     "public, and that it draws on the source dataset. Kaggle then re-runs the notebook on its own "
     "servers and publishes it to your profile. (This step needs your Kaggle API token in "
     "<font face='Courier'>~/.kaggle/kaggle.json</font>.)")
rule()
cap("Generated as a companion to global-semiconductor-eda.ipynb. Code excerpts are lightly "
    "condensed for readability; the notebook holds the full, runnable source.")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.75 * inch, 0.5 * inch,
                      "Global Semiconductor Industry EDA — Code Guide")
    canvas.drawRightString(7.75 * inch, 0.5 * inch, "Page %d" % doc.page)
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=letter,
                        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                        topMargin=0.7 * inch, bottomMargin=0.8 * inch,
                        title="Semiconductor EDA - Code Guide", author="vishalinsightx")
doc.build(flow, onFirstPage=footer, onLaterPages=footer)
print("Wrote", OUT)
