import os
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import markdown
from xhtml2pdf import pisa

# Paths
base_dir = "/Users/manishbulchandani/D/Creative Upaay/Work/ef-polymers/Audit-using-skils"
individual_dir = os.path.join(base_dir, "individual-analysis")
output_dir = os.path.join(individual_dir, "viz_charts")
md_file_path = os.path.join(individual_dir, "overall-analysis.md")
html_file_path = os.path.join(individual_dir, "overall-analysis.html")
pdf_file_path = os.path.join(individual_dir, "overall-analysis.pdf")

# Create output dir for charts
os.makedirs(output_dir, exist_ok=True)

print("Starting visualization generation...")

# ----------------- Viz 1: Radar Chart -----------------
print("Generating Viz 1...")
categories = [
    'Process\nStandardization', 'Technology\nUtilization', 'Data\nGovernance', 
    'Sales & CRM', 'Financial\nAccuracy', 'Knowledge\nManagement', 
    'Automation\nMaturity', 'Scalability\nReadiness'
]
values = [1.5, 2.0, 1.0, 1.0, 1.5, 1.5, 1.5, 1.5]
benchmark = [3.0] * 8

N = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
values += values[:1]
benchmark += benchmark[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], categories, color='#334155', size=9, weight='bold')
ax.set_rlabel_position(0)
plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="#64748b", size=8)
plt.ylim(0, 5)

# Plot EFP Current
ax.plot(angles, values, linewidth=2, linestyle='solid', label="EFP Current (Avg: 1.5)", color='#16a34a')
ax.fill(angles, values, '#22c55e', alpha=0.25)

# Plot Benchmark
ax.plot(angles, benchmark, linewidth=1.5, linestyle='dashed', label="Industry Benchmark (3.0)", color='#dc2626')

plt.title("EF Polymers — Enterprise Overview", size=13, color='#1e3a8a', weight='bold', pad=15)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_1_radar.png'), dpi=300, bbox_inches='tight')
plt.close()

# ----------------- Viz 2: Grouped Horizontal Bar Chart -----------------
print("Generating Viz 2...")
data = {
    'Department': [
        'R&D', 'Production', 'Logistics', 'Finance & Accounts', 'Marketing/Retail', 
        'BD-Cocopeat', 'BD-NGO/CSR', 'BD-Seed', 'BD-B2B/RCM', 'MENA Int\'l', 
        'COO Office', 'CBDO Office'
    ],
    'Process': [2.0, 2.5, 2.0, 2.5, 1.5, 2.0, 1.5, 1.0, 2.0, 2.0, 2.0, 1.5],
    'Technology': [2.0, 2.0, 1.5, 3.0, 1.0, 1.5, 1.0, 1.0, 1.5, 1.5, 2.0, 1.0],
    'Data Quality': [1.5, 2.0, 1.5, 2.0, 1.0, 1.5, 1.0, 1.0, 1.5, 2.0, 1.5, 1.0],
    'Documentation': [2.5, 2.0, 1.5, 2.0, 1.5, 2.0, 1.5, 1.0, 1.5, 2.0, 2.0, 1.5],
    'Knowledge  ': [1.5, 2.0, 2.0, 2.5, 1.0, 1.5, 1.0, 1.0, 1.5, 1.5, 2.0, 1.0]
}
df = pd.DataFrame(data)
df = df.iloc[::-1]  # reverse order for horizontal plot

fig, ax = plt.subplots(figsize=(10, 7))
y = np.arange(len(df))
width = 0.15

colors = ['#3b82f6', '#22c55e', '#f59e0b', '#a855f7', '#ef4444']  # blue, green, orange, purple, red
categories = ['Process', 'Technology', 'Data Quality', 'Documentation', 'Knowledge  ']

for i, cat in enumerate(categories):
    ax.barh(y + i*width - 2*width, df[cat], width, label=cat, color=colors[i], alpha=0.85, edgecolor='black', linewidth=0.5)

ax.set_yticks(y)
ax.set_yticklabels(df['Department'], fontsize=9, weight='bold')
ax.set_xlabel('Maturity Score (1–5)', fontsize=10, weight='bold')
ax.set_xlim(0, 5.5)
ax.set_title('Department Maturity Scorecard', fontsize=12, pad=15, color='#1e3a8a', weight='bold')

# Reference Line for Enterprise Average at 1.7
ax.axvline(1.7, color='#dc2626', linestyle='--', linewidth=1.5, label='Enterprise Average (1.7)')

ax.legend(loc='lower right', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_2_bar.png'), dpi=300, bbox_inches='tight')
plt.close()

# ----------------- Viz 3: Heatmap -----------------
print("Generating Viz 3...")
categories_hm = [
    'Leadership & Governance', 'Strategy Alignment', 'Sales Operations', 'Customer Lifecycle', 
    'Operational Excellence', 'Process Standardization', 'Documentation', 'Knowledge Management', 
    'Technology Landscape', 'Data Quality', 'Reporting & Analytics', 'Automation Readiness', 
    'AI Readiness', 'Compliance Readiness', 'Financial Operations', 'Scalability', 
    'Change Readiness', 'Customer Experience'
]
current_scores = [2.5, 2.0, 1.0, 1.5, 2.0, 1.5, 1.7, 1.5, 2.0, 1.5, 1.5, 1.5, 1.0, 2.0, 2.0, 1.5, 2.0, 2.0]
target_scores = [3.5, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 2.5, 3.5, 3.0, 3.0, 2.5, 2.0, 3.0, 3.5, 3.0, 3.0, 3.0]
gaps = [t - c for c, t in zip(current_scores, target_scores)]

hm_df = pd.DataFrame({
    'Category': categories_hm,
    'Current': current_scores,
    'Target': target_scores,
    'Gap': gaps
})
hm_df = hm_df.iloc[::-1]  # reverse

fig, ax = plt.subplots(figsize=(9, 9))
heatmap_data = hm_df[['Current', 'Target', 'Gap']].values

ax.set_xlim(0, 3)
ax.set_ylim(-0.5, len(categories_hm) - 0.5)

# Draw cell backgrounds
for y_idx in range(len(categories_hm)):
    # Current
    val_curr = heatmap_data[y_idx, 0]
    color_curr = '#fee2e2' if val_curr <= 1.5 else ('#ffedd5' if val_curr <= 2.0 else '#dcfce7')
    rect_curr = plt.Rectangle((0, y_idx - 0.45), 0.9, 0.9, color=color_curr, ec='#94a3b8', lw=0.5)
    ax.add_patch(rect_curr)
    ax.text(0.45, y_idx, f"{val_curr:.1f}", ha='center', va='center', weight='bold', color='#1e293b')

    # Target
    val_targ = heatmap_data[y_idx, 1]
    color_targ = '#dcfce7' if val_targ >= 3.0 else '#ffedd5'
    rect_targ = plt.Rectangle((1, y_idx - 0.45), 0.9, 0.9, color=color_targ, ec='#94a3b8', lw=0.5)
    ax.add_patch(rect_targ)
    ax.text(1.45, y_idx, f"{val_targ:.1f}", ha='center', va='center', weight='bold', color='#1e293b')

    # Gap
    val_gap = heatmap_data[y_idx, 2]
    color_gap = '#dbeafe'  # Blue color shades for gap
    rect_gap = plt.Rectangle((2, y_idx - 0.45), 0.9, 0.9, color=color_gap, alpha=val_gap/2.0 * 0.7 + 0.1, ec='#94a3b8', lw=0.5)
    ax.add_patch(rect_gap)
    ax.text(2.45, y_idx, f"+{val_gap:.1f}", ha='center', va='center', weight='bold', color='#1e3a8a')

ax.set_xticks([0.45, 1.45, 2.45])
ax.set_xticklabels(['Current Score', 'Target Score', 'Maturity Gap'], fontsize=10, weight='bold')
ax.set_yticks(np.arange(len(categories_hm)))
ax.set_yticklabels(hm_df['Category'], fontsize=9, weight='bold')
ax.set_title('Enterprise Maturity Heatmap — Current vs. Target', fontsize=12, pad=20, color='#1e3a8a', weight='bold')
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left=False, bottom=False)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_3_heatmap.png'), dpi=300, bbox_inches='tight')
plt.close()

# ----------------- Viz 4: Network Diagram -----------------
print("Generating Viz 4...")
fig, ax = plt.subplots(figsize=(9, 7))
G = nx.DiGraph()

node_sizes = {
    'All BD Verticals': 1200,
    'Logistics': 1200,
    'Accounts': 2000,
    'Production': 2500,
    'Marketing': 1000,
    'R&D': 1200,
    'QC': 800,
    'COO': 1000,
    'CBDO': 1000
}

for node, size in node_sizes.items():
    G.add_node(node, size=size)

edges = [
    ('All BD Verticals', 'Logistics', {'color': '#ef4444', 'width': 3, 'label': 'Daily'}),
    ('All BD Verticals', 'Accounts', {'color': '#ef4444', 'width': 3, 'label': 'Per-ship'}),
    ('All BD Verticals', 'R&D', {'color': '#f59e0b', 'width': 1.5, 'label': 'Per-trial'}),
    ('All BD Verticals', 'Production', {'color': '#f59e0b', 'width': 1.5, 'label': 'Per-order'}),
    ('Marketing', 'Accounts', {'color': '#f59e0b', 'width': 1.5, 'label': 'Daily'}),
    ('Logistics', 'Accounts', {'color': '#ef4444', 'width': 3, 'label': 'Per-ship'}),
    ('Logistics', 'Production', {'color': '#ef4444', 'width': 3, 'label': 'Daily'}),
    ('Accounts', 'Production', {'color': '#ef4444', 'width': 3, 'label': 'Per-invoice'}),
    ('R&D', 'Production', {'color': '#f59e0b', 'width': 1.5, 'label': 'Project'}),
    ('R&D', 'QC', {'color': '#f59e0b', 'width': 1.5, 'label': 'Daily'}),
    ('COO', 'Accounts', {'color': '#f59e0b', 'width': 1.5, 'label': 'Continuous'}),
    ('CBDO', 'All BD Verticals', {'color': '#f59e0b', 'width': 1.5, 'label': 'Monthly'})
]

for u, v, attrs in edges:
    G.add_edge(u, v, **attrs)

pos = {
    'CBDO': (-2.5, 1.5),
    'All BD Verticals': (-1.5, 0.8),
    'COO': (-2.5, -0.5),
    'Marketing': (-1.5, -1.5),
    'R&D': (0, 1.8),
    'QC': (1.2, 1.8),
    'Logistics': (0.5, 0.5),
    'Accounts': (0.5, -0.8),
    'Production': (2.0, -0.2)
}

nx.draw_networkx_nodes(G, pos, node_size=[node_sizes[n] for n in G.nodes()], 
                       node_color='#e2e8f0', edgecolors='#64748b', ax=ax)
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif', font_weight='bold', ax=ax)

for u, v, data in G.edges(data=True):
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=data['width'], 
                           edge_color=data['color'], arrowsize=15, min_source_margin=10, min_target_margin=10, ax=ax)

# Draw edge labels manually for spacing
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7, font_color='#475569', ax=ax)

ax.set_title('Cross-Department Dependency Network', fontsize=12, pad=15, color='#1e3a8a', weight='bold')
ax.axis('off')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_4_network.png'), dpi=300, bbox_inches='tight')
plt.close()

# ----------------- Viz 5: Bubble Chart for Risks -----------------
print("Generating Viz 5...")
likelihoods = [5, 4, 3, 4, 5, 4, 5, 4, 5, 5, 4, 5, 5, 4]
impacts = [5, 5, 4, 4, 4, 4, 3, 3, 3, 4, 4, 3, 4, 4]
labels = [f"R{i:02d}" for i in range(1, 15)]
dept_counts = [3, 1, 1, 3, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2]
colors = ['#dc2626', '#dc2626', '#f59e0b', '#f59e0b', '#f59e0b', '#f59e0b', '#f59e0b', '#f59e0b', '#f59e0b', '#f59e0b', '#f59e0b', '#f59e0b', '#dc2626', '#dc2626']

# Jitter to prevent overlapping
np.random.seed(42)
x_jitter = np.array(likelihoods) + np.random.uniform(-0.15, 0.15, len(likelihoods))
y_jitter = np.array(impacts) + np.random.uniform(-0.15, 0.15, len(impacts))

fig, ax = plt.subplots(figsize=(8, 6))

ax.axhspan(0.5, 3.0, 0, 0.5, color='#f8fafc', zorder=0) 
ax.axhspan(3.0, 5.5, 0.5, 1.0, color='#fee2e2', zorder=0) 
ax.axhspan(3.0, 5.5, 0, 0.5, color='#fff7ed', zorder=0) 
ax.axhspan(0.5, 3.0, 0.5, 1.0, color='#eff6ff', zorder=0) 

ax.scatter(x_jitter, y_jitter, s=[c*250 for c in dept_counts], c=colors, alpha=0.7, edgecolors='#475569', linewidths=1.2, zorder=3)

for i, txt in enumerate(labels):
    ax.annotate(txt, (x_jitter[i], y_jitter[i]), ha='center', va='center', weight='bold', fontsize=8, color='white' if colors[i]=='#dc2626' else '#1e293b', zorder=4)

ax.set_xlabel('Likelihood (1 = Unlikely, 5 = Certain)', fontsize=10, fontweight='bold', labelpad=10)
ax.set_ylabel('Business Impact (1 = Low, 5 = Critical)', fontsize=10, fontweight='bold', labelpad=10)
ax.set_title('Enterprise Risk Register — Impact vs. Likelihood', fontsize=12, pad=15, color='#1e3a8a', weight='bold')

ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_yticks([1, 2, 3, 4, 5])
ax.grid(True, linestyle='--', alpha=0.5, zorder=1)

ax.text(4.5, 4.5, "Immediate Action", ha='center', va='center', fontsize=10, color='#991b1b', weight='bold', style='italic', alpha=0.8)
ax.text(1.5, 4.5, "Monitor Closely", ha='center', va='center', fontsize=10, color='#c2410c', weight='bold', style='italic', alpha=0.8)
ax.text(4.5, 1.5, "Quick Fix", ha='center', va='center', fontsize=10, color='#1d4ed8', weight='bold', style='italic', alpha=0.8)
ax.text(1.5, 1.5, "Accept / Minimal", ha='center', va='center', fontsize=10, color='#475569', weight='bold', style='italic', alpha=0.8)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_5_bubble.png'), dpi=300, bbox_inches='tight')
plt.close()

# ----------------- Viz 6: Technology Block Diagram -----------------
print("Generating Viz 6...")
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)

layers = [
    {"title": "1. Communication Layer", "systems": "WhatsApp (dominant) | Email | Slack | WeChat | LINE", "y": 10, "color": "#fee2e2"},
    {"title": "2. Operational Layer", "systems": "Google Sheets (30+ trackers) | Google Drive | Paper Diaries", "y": 8, "color": "#fef3c7"},
    {"title": "3. Business Applications (Zoho)", "systems": "Zoho Books | Zoho Inventory | Zoho Expense | Zoho Payroll | Zoho People | Custom WMS", "y": 6, "color": "#dcfce7"},
    {"title": "4. Marketing / Sales", "systems": "Google Ads | LinkedIn Ads | Dripify (Lapsed) | Contactout | Apollo | Canva", "y": 4, "color": "#e0f2fe"},
    {"title": "5. Compliance & Field", "systems": "CargoX | Field Tracking App", "y": 2, "color": "#f3e8ff"},
    {"title": "6. Analytics (Onboarding)", "systems": "Power BI", "y": 0, "color": "#f1f5f9"}
]

for layer in layers:
    rect = plt.Rectangle((1, layer["y"] - 0.7), 8, 1.4, edgecolor='#64748b', facecolor=layer["color"], alpha=0.8, lw=1.5)
    ax.add_patch(rect)
    ax.text(5, layer["y"] + 0.2, layer["title"], ha='center', va='center', weight='bold', fontsize=10, color='#1e293b')
    ax.text(5, layer["y"] - 0.3, layer["systems"], ha='center', va='center', fontsize=8, color='#475569', style='italic')

# Draw lines showing broken links
ax.annotate('Manual Checks (Phone)', xy=(5, 6.7), xytext=(5, 7.3),
            arrowprops=dict(arrowstyle="<->", color="#dc2626", lw=1.5, ls="--"),
            ha='center', va='center', fontsize=7, color='#dc2626', weight='bold')

ax.annotate('Data Duplication', xy=(3, 6.7), xytext=(3, 7.3),
            arrowprops=dict(arrowstyle="<->", color="#dc2626", lw=1.5, ls="--"),
            ha='center', va='center', fontsize=7, color='#dc2626', weight='bold')

ax.set_title('EF Polymers — Current Technology Ecosystem', fontsize=12, pad=15, color='#1e3a8a', weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_6_block.png'), dpi=300, bbox_inches='tight')
plt.close()

# ----------------- Viz 7: Data Flow Diagram -----------------
print("Generating Viz 7...")
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

sources = [
    "Field Teams\n(WhatsApp location/activity)", 
    "Customers\n(POs/Receipts on WhatsApp)", 
    "Production Floor\n(manual QC/Stock sheets)", 
    "Vendors\n(MOQ quotes/specs)", 
    "Ad Platforms\n(Google/LinkedIn leads)"
]
processing = [
    "30+ Google Sheets\n(manual entry)", 
    "Zoho Books\n(invoicing)", 
    "WhatsApp Groups\n(routing)", 
    "Email\n(document exchange)", 
    "Paper Diaries\n(field data)"
]
consumers = [
    "COO/CBDO\n(manual verbal briefings)", 
    "Accounts\n(manual reconciliation)", 
    "Board/Investors\n(PowerPoint decks)", 
    "Logistics\n(manual dispatch sheets)"
]

def draw_col(items, x, y_start, y_spacing, color, name):
    coords = []
    ax.text(x, 9.5, name, ha='center', va='center', weight='bold', fontsize=10, color='#1e3a8a')
    for i, item in enumerate(items):
        y = y_start - i * y_spacing
        rect = plt.Rectangle((x - 1.25, y - 0.55), 2.5, 1.1, edgecolor='#475569', facecolor=color, alpha=0.8, lw=1)
        ax.add_patch(rect)
        ax.text(x, y, item, ha='center', va='center', fontsize=7, color='#0f172a', weight='bold')
        coords.append((x, y))
    return coords

src_coords = draw_col(sources, 1.5, 8.0, 1.5, '#e0f2fe', 'Data Sources')
proc_coords = draw_col(processing, 5.0, 8.0, 1.5, '#fef3c7', 'Processing Layer')
cons_coords = draw_col(consumers, 8.5, 7.5, 1.8, '#dcfce7', 'Consumption Layer')

for src in src_coords:
    for proc in proc_coords[:3]:
        ax.plot([src[0]+1.25, proc[0]-1.25], [src[1], proc[1]], color='#94a3b8', lw=0.5, alpha=0.5)

for proc in proc_coords:
    for cons in cons_coords:
        ax.plot([proc[0]+1.25, cons[0]-1.25], [proc[1], cons[1]], color='#94a3b8', lw=0.5, alpha=0.5)

ax.set_title('EF Polymers — Data Flow Architecture (Current State)', fontsize=12, pad=15, color='#1e3a8a', weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_7_sankey.png'), dpi=300, bbox_inches='tight')
plt.close()

# ----------------- Viz 8: Funnel Chart -----------------
print("Generating Viz 8...")
stages = [
    '1. Order Intake (WhatsApp)',
    '2. Data Validation',
    '3. Stock Check (Phone Call)',
    '4. Customer Data Lookup',
    '5. Invoice Generation',
    '6. Logistics Documentation',
    '7. Transit Updates (Manual)'
]
waste_min = [22.5, 12.5, 12.5, 7.5, 0, 10, 25]

fig, ax = plt.subplots(figsize=(8, 5))
y = np.arange(len(stages))
bars = ax.barh(y, waste_min, color='#ef4444', alpha=0.8, edgecolor='#dc2626', height=0.6)

for bar in bars:
    width = bar.get_width()
    if width > 0:
        ax.text(width + 1, bar.get_y() + bar.get_height()/2, f"+{int(width)} min", 
                va='center', ha='left', fontsize=9, weight='bold', color='#dc2626')

ax.set_yticks(y)
ax.set_yticklabels(stages, fontsize=9, weight='bold')
ax.set_xlabel('Time Waste (Minutes)', fontsize=10, weight='bold')
ax.set_xlim(0, 35)
ax.set_title('Order Fulfillment — Time Waste Analysis', fontsize=12, pad=15, color='#1e3a8a', weight='bold')
ax.text(20, 1, "Total Waste: 70–110 min\nper order", bbox=dict(facecolor='#fee2e2', edgecolor='#dc2626', boxstyle='round,pad=0.5'), fontsize=10, weight='bold', color='#dc2626')
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_8_funnel.png'), dpi=300, bbox_inches='tight')
plt.close()

# ----------------- Viz 9: Gantt Chart -----------------
print("Generating Viz 9...")
phases = [
    'Phase 0: Preparation',
    'Phase 1: Quick Wins',
    'Phase 2: Operational Foundation',
    'Phase 3: Digital Transformation',
    'Phase 4: Automation & AI'
]
start_months = [0, 0, 1, 3, 6]
durations = [0.5, 1, 2, 3, 6]
colors_gantt = ['#64748b', '#22c55e', '#3b82f6', '#a855f7', '#6b7280']

fig, ax = plt.subplots(figsize=(9, 5))
y = np.arange(len(phases))

for i in range(len(phases)):
    ax.barh(y[i], durations[i], left=start_months[i], color=colors_gantt[i], alpha=0.85, height=0.5, edgecolor='#475569')

milestones_x = [1, 3, 6, 12]
milestones_y = [1.2, 2.2, 3.2, 4.2]
milestone_labels = ['M1: Intake Digitized', 'M2: CRM Live', 'M3: Dashboards Active', 'M4: AI Pilots ROI']

for i in range(len(milestones_x)):
    ax.scatter(milestones_x[i], milestones_y[i], color='#dc2626', marker='D', s=100, zorder=5, edgecolor='black')
    ax.text(milestones_x[i] + 0.25, milestones_y[i], milestone_labels[i], va='center', ha='left', fontsize=8, weight='bold', color='#dc2626')

ax.set_yticks(y)
ax.set_yticklabels(phases, fontsize=9, weight='bold')
ax.set_xlabel('Months from Kick-off', fontsize=10, weight='bold')
ax.set_xlim(-0.5, 14)
ax.set_xticks(np.arange(14))
ax.set_title('EF Polymers — 12-Month Transformation Roadmap', fontsize=12, pad=15, color='#1e3a8a', weight='bold')
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_9_gantt.png'), dpi=300, bbox_inches='tight')
plt.close()

# ----------------- Viz 10: Prioritization Scatter Plot -----------------
print("Generating Viz 10...")
initiatives = {
    'S01': {'effort': 6, 'impact': 10, 'color': '#3b82f6'}, 
    'S02': {'effort': 5, 'impact': 8, 'color': '#3b82f6'},  
    'S03': {'effort': 3, 'impact': 7, 'color': '#22c55e'},  
    'S04': {'effort': 3, 'impact': 8, 'color': '#22c55e'},  
    'S05': {'effort': 5, 'impact': 8, 'color': '#3b82f6'},  
    'S06': {'effort': 7, 'impact': 9, 'color': '#3b82f6'},  
    'S07': {'effort': 4, 'impact': 7, 'color': '#22c55e'},  
    'S08': {'effort': 4, 'impact': 6, 'color': '#a855f7'},  
    'S09': {'effort': 3, 'impact': 6, 'color': '#a855f7'},  
    'S10': {'effort': 2, 'impact': 7, 'color': '#a855f7'},  
    'S11': {'effort': 6, 'impact': 7, 'color': '#a855f7'},  
    'S15': {'effort': 5, 'impact': 7, 'color': '#a855f7'},  
    'S16': {'effort': 5, 'impact': 5, 'color': '#6b7280'},  
    'S17': {'effort': 7, 'impact': 6, 'color': '#6b7280'}   
}

fig, ax = plt.subplots(figsize=(8, 6))

ax.axhspan(5, 10.5, 0, 5/10.5, color='#dcfce7', alpha=0.3) 
ax.axhspan(5, 10.5, 5/10.5, 1, color='#dbeafe', alpha=0.3) 
ax.axhspan(0, 5, 0, 5/10.5, color='#f1f5f9', alpha=0.3)     
ax.axhspan(0, 5, 5/10.5, 1, color='#fee2e2', alpha=0.3)     

for init, vals in initiatives.items():
    ax.scatter(vals['effort'], vals['impact'], color=vals['color'], s=200, edgecolor='black', zorder=5)
    ax.text(vals['effort'], vals['impact'] + 0.25, init, ha='center', va='bottom', weight='bold', fontsize=8)

ax.axvline(5, color='#94a3b8', linestyle='--', linewidth=1, zorder=2)
ax.axhline(5, color='#94a3b8', linestyle='--', linewidth=1, zorder=2)

ax.set_xlabel('Implementation Effort (1 = Low, 10 = High)', fontsize=10, weight='bold', labelpad=10)
ax.set_ylabel('Business Impact (1 = Low, 10 = High)', fontsize=10, weight='bold', labelpad=10)
ax.set_xlim(0.5, 10.5)
ax.set_ylim(0.5, 10.5)

ax.text(2.5, 9.5, "Quick Wins", ha='center', va='center', fontsize=12, color='#16a34a', weight='bold')
ax.text(7.5, 9.5, "Strategic Investments", ha='center', va='center', fontsize=12, color='#2563eb', weight='bold')
ax.text(2.5, 1.5, "Low-Hanging Fruit", ha='center', va='center', fontsize=12, color='#475569', weight='bold')
ax.text(7.5, 1.5, "Long-Term Bets", ha='center', va='center', fontsize=12, color='#dc2626', weight='bold')

ax.set_title('Initiative Prioritization — Impact vs. Effort', fontsize=12, pad=15, color='#1e3a8a', weight='bold')
ax.grid(True, linestyle=':', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_10_prioritization.png'), dpi=300, bbox_inches='tight')
plt.close()


# ----------------- Viz 11: Organizational Structure Chart (Mermaid 1) -----------------
print("Generating Viz 11...")
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.set_xlim(0.0, 10.5)
ax.set_ylim(1.0, 10.5)

nodes = {
    'CEO': {'text': "Founders / Board", 'pos': (5.0, 9.5), 'color': '#dbeafe', 'border': '#2563eb'},
    'COO': {'text': "Puran Singh Rajput\nCOO", 'pos': (2.5, 7.5), 'color': '#dcfce7', 'border': '#16a34a'},
    'CBDO': {'text': "Ankit Jain\nCo-Founder & CBDO", 'pos': (7.5, 7.5), 'color': '#fef3c7', 'border': '#d97706'},
    
    # COO Children
    'FIN': {'text': "Finance & Accounts\nShobha Shekhawat", 'pos': (1.0, 4.8), 'color': '#f1f5f9', 'border': '#64748b'},
    'MKT': {'text': "Marketing & Retail Sales\nGaurav Jain", 'pos': (2.6, 4.8), 'color': '#f1f5f9', 'border': '#64748b'},
    'MENA': {'text': "MENA International\nNeha Pathak", 'pos': (4.2, 4.8), 'color': '#f1f5f9', 'border': '#64748b'},
    'PROD': {'text': "Production\nRishabh Doshi", 'pos': (1.0, 2.3), 'color': '#f1f5f9', 'border': '#64748b'},
    'RD': {'text': "R&D\nRitu Panwar", 'pos': (2.6, 2.3), 'color': '#f1f5f9', 'border': '#64748b'},
    'LOG': {'text': "Logistics\nNihal Paliwal", 'pos': (4.2, 2.3), 'color': '#f1f5f9', 'border': '#64748b'},
    
    # CBDO Children
    'SEED': {'text': "BD-Seed\nSameer Mahiskar", 'pos': (5.8, 4.8), 'color': '#f1f5f9', 'border': '#64748b'},
    'B2B': {'text': "BD-B2B/RCM\nJatin Jain", 'pos': (7.4, 4.8), 'color': '#f1f5f9', 'border': '#64748b'},
    'NGO': {'text': "BD-NGO/CSR\nVikash Mehta", 'pos': (9.0, 4.8), 'color': '#f1f5f9', 'border': '#64748b'},
    'GOV': {'text': "BD-Government\nShailendra Singh", 'pos': (5.8, 2.3), 'color': '#f1f5f9', 'border': '#64748b'},
    'COCO': {'text': "BD-Cocopeat\nMohit Kumar Gupta", 'pos': (7.4, 2.3), 'color': '#f1f5f9', 'border': '#64748b'}
}

# Draw boxes
for name, info in nodes.items():
    x, y = info['pos']
    rect = plt.Rectangle((x - 0.75, y - 0.65), 1.5, 1.3, edgecolor=info['border'], facecolor=info['color'], alpha=0.9, lw=1.5, zorder=3)
    ax.add_patch(rect)
    ax.text(x, y, info['text'], ha='center', va='center', fontsize=7, color='#1e293b', weight='bold', zorder=4)

# Draw arrows
arrow_props = dict(arrowstyle="->", color='#64748b', lw=1.5, mutation_scale=15, zorder=2)
# CEO -> COO, CBDO
ax.annotate('', xy=(2.5, 8.15), xytext=(5.0, 8.85), arrowprops=arrow_props)
ax.annotate('', xy=(7.5, 8.15), xytext=(5.0, 8.85), arrowprops=arrow_props)

# COO -> children
for name in ['FIN', 'MKT', 'MENA', 'PROD', 'RD', 'LOG']:
    x, y = nodes[name]['pos']
    ax.annotate('', xy=(x, y + 0.65), xytext=(2.5, 6.85), arrowprops=arrow_props)

# CBDO -> children
for name in ['SEED', 'B2B', 'NGO', 'GOV', 'COCO']:
    x, y = nodes[name]['pos']
    ax.annotate('', xy=(x, y + 0.65), xytext=(7.5, 6.85), arrowprops=arrow_props)

# SEED -> COO (Dashed dual report)
arrow_props_dashed = dict(arrowstyle="->", color='#94a3b8', lw=1.2, ls='--', mutation_scale=12, zorder=1)
ax.annotate('', xy=(2.5, 6.85), xytext=(5.8, 5.45), arrowprops=arrow_props_dashed)
ax.text(4.15, 6.15, 'Dual Report', color='#64748b', fontsize=6, rotation=14, ha='center', va='center', weight='bold')

ax.set_title('EF Polymers — Organizational Structure & Reporting Lines', fontsize=12, pad=15, color='#1e3a8a', weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_11_org.png'), dpi=300, bbox_inches='tight')
plt.close()


# ----------------- Viz 12: Order Fulfillment Process (Mermaid 2) -----------------
print("Generating Viz 12...")
fig, ax = plt.subplots(figsize=(8, 10))
ax.axis('off')
ax.set_xlim(0.0, 10.0)
ax.set_ylim(0.5, 10.0)

wf_nodes = {
    'A': {'text': "BD/Sales posts order\n(WhatsApp — often incomplete)", 'pos': (5.0, 9.0), 'color': '#fee2e2', 'border': '#ef4444'},
    'B': {'text': "Logistics validates\norder specs", 'pos': (5.0, 7.5), 'color': '#e0f2fe', 'border': '#0284c7'},
    'C': {'text': "Manual follow-up\ncalls/emails to Sales", 'pos': (1.5, 7.5), 'color': '#fee2e2', 'border': '#ef4444'},
    'D': {'text': "Accounts verifies\nstock availability", 'pos': (5.0, 5.8), 'color': '#e0f2fe', 'border': '#0284c7'},
    'E': {'text': "Phone call to\nProduction Manager", 'pos': (1.5, 5.8), 'color': '#fee2e2', 'border': '#ef4444'},
    'F': {'text': "Accounts generates\nZoho Invoice", 'pos': (5.0, 4.3), 'color': '#e0f2fe', 'border': '#0284c7'},
    'G': {'text': "Logistics prints\nInvoice + E-Way Bill", 'pos': (5.0, 3.0), 'color': '#e0f2fe', 'border': '#0284c7'},
    'H': {'text': "Physical loading\n& dispatch", 'pos': (5.0, 1.7), 'color': '#e0f2fe', 'border': '#0284c7'},
    'I': {'text': "Manual WhatsApp\ntransit updates", 'pos': (8.5, 1.7), 'color': '#fee2e2', 'border': '#ef4444'}
}

# Draw boxes
for name, info in wf_nodes.items():
    x, y = info['pos']
    rect = plt.Rectangle((x - 1.35, y - 0.5), 2.7, 1.0, edgecolor=info['border'], facecolor=info['color'], alpha=0.9, lw=1.5, zorder=3)
    ax.add_patch(rect)
    ax.text(x, y, info['text'], ha='center', va='center', fontsize=7, color='#1e293b', weight='bold', zorder=4)

# Draw arrows
arrow_props_wf = dict(arrowstyle="->", color='#475569', lw=1.5, mutation_scale=15, zorder=2)

# A -> B
ax.annotate('', xy=(5.0, 8.0), xytext=(5.0, 8.5), arrowprops=arrow_props_wf)
# B -> C (Missing data)
ax.annotate('', xy=(2.85, 7.5), xytext=(3.65, 7.5), arrowprops=arrow_props_wf)
ax.text(3.25, 7.7, 'Missing data', color='#ef4444', fontsize=7, ha='center', va='center', weight='bold')
# C -> B
ax.annotate('', xy=(3.65, 7.3), xytext=(2.85, 7.3), arrowprops=arrow_props_wf)

# B -> D (Complete)
ax.annotate('', xy=(5.0, 6.3), xytext=(5.0, 7.0), arrowprops=arrow_props_wf)
ax.text(5.3, 6.65, 'Complete', color='#0284c7', fontsize=7, ha='left', va='center', weight='bold')

# D -> E (No live data)
ax.annotate('', xy=(2.85, 5.8), xytext=(3.65, 5.8), arrowprops=arrow_props_wf)
ax.text(3.25, 6.0, 'No live data', color='#ef4444', fontsize=7, ha='center', va='center', weight='bold')
# E -> D
ax.annotate('', xy=(3.65, 5.6), xytext=(2.85, 5.6), arrowprops=arrow_props_wf)

# D -> F (Stock confirmed)
ax.annotate('', xy=(5.0, 4.8), xytext=(5.0, 5.3), arrowprops=arrow_props_wf)
ax.text(5.3, 5.05, 'Stock confirmed', color='#0284c7', fontsize=7, ha='left', va='center', weight='bold')

# F -> G
ax.annotate('', xy=(5.0, 3.5), xytext=(5.0, 3.8), arrowprops=arrow_props_wf)
# G -> H
ax.annotate('', xy=(5.0, 2.2), xytext=(5.0, 2.5), arrowprops=arrow_props_wf)
# H -> I
ax.annotate('', xy=(7.15, 1.7), xytext=(6.35, 1.7), arrowprops=arrow_props_wf)

ax.set_title('Order Fulfillment Process Flowchart (Current State)', fontsize=12, pad=15, color='#1e3a8a', weight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'viz_12_workflow.png'), dpi=300, bbox_inches='tight')
plt.close()

print("All visualizations generated successfully.")


# ----------------- Markdown to HTML & PDF Conversion -----------------
print("Processing Markdown file...")

with open(md_file_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Replace standard visualization blocks with image tags
viz_replacements = {
    r"VISUALIZATION: Radar/Spider Chart[\s\S]*?Overlay: Industry benchmark line at 3\.0 \(mid-maturity\)": 
        '![EF Polymers — Enterprise Overview](viz_charts/viz_1_radar.png)',
    
    r"VISUALIZATION: Grouped Horizontal Bar Chart[\s\S]*?Color coding: Scores ≤1\.5 = red, 1\.5–2\.5 = amber, ≥2\.5 = green": 
        '![Department Maturity Scorecard](viz_charts/viz_2_bar.png)',
    
    r"VISUALIZATION: Maturity Heatmap \(Matrix/Grid\)[\s\S]*?Gap column: Color intensity proportional to gap size": 
        '![Enterprise Maturity Heatmap — Current vs. Target](viz_charts/viz_3_heatmap.png)',
        
    r"VISUALIZATION: Network/Force-Directed Graph[\s\S]*?Key Insight: Logistics[\s\S]*?operations": 
        '![Cross-Department Dependency Network](viz_charts/viz_4_network.png)',
        
    r"VISUALIZATION: Risk Impact vs\. Likelihood Matrix \(Bubble Chart\)[\s\S]*?Expected Clustering[\s\S]*?quadrant": 
        '![Enterprise Risk Register — Impact vs. Likelihood](viz_charts/viz_5_bubble.png)',
        
    r"VISUALIZATION: Technology Architecture Diagram \(Block Diagram\)[\s\S]*?Color: Red borders for disconnected systems, green for connected": 
        '![EF Polymers — Current Technology Ecosystem](viz_charts/viz_6_block.png)',
        
    r"VISUALIZATION: Sankey / Flow Diagram[\s\S]*?Highlight: No single source of truth exists for any data domain": 
        '![EF Polymers — Data Flow Architecture (Current State)](viz_charts/viz_7_sankey.png)',
        
    r"VISUALIZATION: Funnel/Waterfall Chart[\s\S]*?Annotations: Highlight that this compounds across 10-20 orders/day": 
        '![Order Fulfillment — Time Waste Analysis](viz_charts/viz_8_funnel.png)',
        
    r"VISUALIZATION: Gantt Chart / Timeline[\s\S]*?M4 \(Month 12\): AI pilots producing measurable ROI": 
        '![EF Polymers — 12-Month Transformation Roadmap](viz_charts/viz_9_gantt.png)',
        
    r"VISUALIZATION: Prioritization Quadrant \(Scatter Plot\)[\s\S]*?Color: Green = Phase 1, Blue = Phase 2, Purple = Phase 3, Gray = Phase 4": 
        '![Initiative Prioritization — Impact vs. Effort](viz_charts/viz_10_prioritization.png)'
}

cleaned_content = md_content
for pattern, replacement in viz_replacements.items():
    full_pattern = r"```\n" + pattern + r"\n```"
    match = re.search(full_pattern, cleaned_content)
    if match:
        cleaned_content = re.sub(full_pattern, replacement, cleaned_content)
    else:
        cleaned_content = re.sub(pattern, replacement, cleaned_content)

# Replace Mermaid Code Blocks with the newly generated visualizations
print("Replacing Mermaid blocks with image tags...")
def replace_mermaid_blocks(content):
    pattern = r"```mermaid([\s\S]*?)```"
    def replacer(match):
        block_content = match.group(1)
        if "Founders / Board" in block_content or "CEO" in block_content:
            return '![EF Polymers — Organizational Structure & Reporting Lines](viz_charts/viz_11_org.png)'
        elif "BD/Sales posts order" in block_content or "Logistics validates" in block_content:
            return '![Order Fulfillment Process Flowchart (Current State)](viz_charts/viz_12_workflow.png)'
        else:
            return match.group(0)
    return re.sub(pattern, replacer, content)

cleaned_content = replace_mermaid_blocks(cleaned_content)

# Clean up unicode symbols that might crash ReportLab/xhtml2pdf
symbol_map = {
    "🔴": "<font color='red'><b>CRITICAL</b></font>",
    "🟡": "<font color='orange'><b>MEDIUM</b></font>",
    "🟢": "<font color='green'><b>LOW / OK</b></font>",
    "⚠️": "<b>WARNING:</b>",
    "❌": "<b>[X]</b>",
    "✅": "<b>[OK]</b>",
    "🔍": "<b>MONITOR:</b>"
}

for sym, repl in symbol_map.items():
    cleaned_content = cleaned_content.replace(sym, repl)

print("Converting Markdown to HTML...")

# Convert MD to HTML with extensions
html_body = markdown.markdown(cleaned_content, extensions=['tables', 'fenced_code'])

# Wrap HTML in a clean, styled layout for PDF rendering
html_doc = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @page {{
        size: a4;
        margin: 2cm;
        @frame footer {{
            -pdf-frame-content: footer_content;
            bottom: 1cm;
            left: 2cm;
            right: 2cm;
            height: 1cm;
        }}
    }}
    body {{
        font-family: Helvetica, Arial, sans-serif;
        color: #334155;
        line-height: 1.6;
        font-size: 10pt;
    }}
    h1 {{
        font-size: 18pt;
        color: #1e3a8a; /* Deep navy */
        border-bottom: 2px solid #3b82f6;
        padding-bottom: 5px;
        margin-top: 25px;
        margin-bottom: 15px;
        page-break-before: always;
    }}
    h1:first-of-type {{
        page-break-before: avoid;
    }}
    h2 {{
        font-size: 13pt;
        color: #0f766e; /* Teal */
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 3px;
    }}
    h3 {{
        font-size: 11pt;
        color: #0f172a;
        margin-top: 15px;
        margin-bottom: 8px;
    }}
    p {{
        margin-bottom: 10px;
        text-align: justify;
    }}
    ul, ol {{
        margin-bottom: 10px;
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 5px;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        margin-bottom: 20px;
        font-size: 8.5pt;
    }}
    th {{
        background-color: #1e3a8a;
        color: #ffffff;
        font-weight: bold;
        text-align: left;
        padding: 5px 8px;
        border: 1px solid #1e3a8a;
    }}
    td {{
        border: 1px solid #cbd5e1;
        padding: 5px 8px;
    }}
    tr:nth-child(even) {{
        background-color: #f8fafc;
    }}
    blockquote {{
        border-left: 4px solid #3b82f6;
        background-color: #eff6ff;
        padding: 10px;
        margin: 10px 0;
        font-style: italic;
    }}
    img {{
        display: block;
        margin: 15px auto;
        max-width: 100%;
        height: auto;
    }}
    .center {{
        text-align: center;
    }}
    #footer_content {{
        text-align: center;
        color: #94a3b8;
        font-size: 8pt;
        border-top: 1px solid #e2e8f0;
        padding-top: 5px;
    }}
</style>
</head>
<body>

{html_body}

<div id="footer_content">
    EF Polymers Operational Audit Report &mdash; Page <pdf:pagenumber> of <pdf:pagecount>
</div>

</body>
</html>
"""

# Write intermediate HTML file (for inspection/backup)
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_doc)

print(f"HTML file generated at: {html_file_path}")
print("Converting HTML to PDF using xhtml2pdf...")

# Convert HTML to PDF
with open(pdf_file_path, "wb") as pdf_file:
    orig_cwd = os.getcwd()
    os.chdir(individual_dir)
    try:
        pisa_status = pisa.CreatePDF(html_doc, dest=pdf_file)
    finally:
        os.chdir(orig_cwd)

if pisa_status.err:
    print(f"Error converting HTML to PDF! Code: {pisa_status.err}")
else:
    print(f"PDF successfully generated at: {pdf_file_path}")
