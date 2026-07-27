---
tags: [aigis, concept, mathematics, statistics, hypothesis-testing]
created: 2026-07-27
---

# ANOVA — Analysis of Variance

## Overview

**Analysis of Variance** (ANOVA / Analisis Varians) is a statistical method developed by Ronald A. Fisher (1918) to compare the means of **three or more groups** simultaneously. Rather than conducting many pairwise $t$-tests — which inflates the overall Type I error rate — ANOVA partitions total variability into components attributable to different sources.

**Analisis varians** works by comparing the **variance between groups** to the **variance within groups**. If the between-group variance is substantially larger than the within-group variance, the null hypothesis that all group means are equal is rejected.

## The F-Statistic and One-Way ANOVA

### One-Way ANOVA (ANOVA Satu Arah)

Tests whether the means of $k \geq 3$ groups (kelompok/perlakuan) differ across a single factor (faktor tunggal). Let $n_i$ be the sample size and $\bar{y}_i$ the mean of group $i$, with $N = \sum n_i$ the grand total, and $\bar{y}_{..}$ the overall mean.

**Sum of Squares** (Jumlah Kuadrat):

$$
SS_{\text{Between}} = \sum_{i=1}^{k} n_i (\bar{y}_i - \bar{y}_{..})^2
$$

$$
SS_{\text{Within}} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2
$$

$$
SS_{\text{Total}} = SS_{\text{Between}} + SS_{\text{Within}} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_{..})^2
$$

**Mean Squares** (Kuadrat Rata-rata):

$$
MS_{\text{Between}} = \frac{SS_{\text{Between}}}{k - 1}, \qquad MS_{\text{Within}} = \frac{SS_{\text{Within}}}{N - k}
$$

**F-statistic**:
$$
F = \frac{MS_{\text{Between}}}{MS_{\text{Within}}}
$$

Under $H_0$ (all $\mu_i$ equal), $F \sim F(k-1, N-k)$ — an **F-distribution** derajat kebebasan $(k-1, N-k)$.

**Keputusan** (decision): If $F > F_{\alpha}(k-1, N-k)$, reject $H_0$ at significance level $\alpha$ (umumnya $\alpha = 0{.}05$). Alternatively, compute the $p$-value = $P(F_{k-1,N-k} > F_{\text{obs}})$ and reject if $p < \alpha$.

### Assumptions (Asumsi ANOVA) (Asumsi ANOVA)

ANOVA relies on three key assumptions that should be verified before interpreting results:

1. **Independence** (Independensi): Observations within and between groups are independent — not influenced by each other. Violation common in spatial data: measurements near each other may be correlated (autokorelasi).

2. **Normality** (Normalitas): The data in each group follow a normal distribution $N(\mu_i, \sigma^2)$. For large samples ($n_i \geq 20$–$30$), ANOVA is robust to moderate departures from normality (robust terhadap penyimpangan). For small samples, use Shapiro-Wilk or Kolmogorov-Smirnov tests (uji normalitas).

3. **Homoscedasticity** (Homogenitas Varians): All groups share a common variance — $\sigma_1^2 = \sigma_2^2 = \cdots = \sigma_k^2 = \sigma^2$. Check with Levene's test atau uji Bartlett. Jika homogenitas gagal, gunakan Welch's ANOVA (ANOVA Welch) sebagai alternatif non-parametrik (alternatif untuk data tidak homogen).

**Pemeriksaan asumsi penting**: in geodesy, comparing survey techniques or GNSS processing software output, non-independence between measurements is common — spatial autocorrelation violates the independence assumption and may require mixed-effects or geostatistical models instead.

## Two-Way ANOVA (ANOVA Dua Arah)

When two factors (faktor) are of interest simultaneously — e.g., survey method and terrain type — **two-way ANOVA** decomposes the total sum of squares into three components:
- $SS_A$ — variance due to Factor A (faktor A)
- $SS_B$ — variance due to Factor B (faktor B)
- $SS_{AB}$ — interaction variance (interaksi antara A dan B)
- $SS_{\text{Within}}$ — residual/within-cell variance (sisa)

$$
SS_{\text{Total}} = SS_A + SS_B + SS_{AB} + SS_{\text{Within}}
$$

The model for balanced design ($n$ observations per cell):
$$
y_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \varepsilon_{ijk}
$$

where $\alpha_i$ is the $i$-th level effect of Factor A, $\beta_j$ the $j$-th level effect of Factor B $(\text{i}\beta)_{ij} is the interaction effect, and $\varepsilon_{ijk} \sim N(0, \sigma^2)$ is the random error (suku galat).

**Interpretation**: If the interaction term is significant ($p < \alpha$), the effect of one factor depends on the level of the other — the two factors do not act independently (efek tidak saling bebas).

## Post-hoc Tests (Uji Lanjutan)

When the ANOVA $F$-test rejects $H_0$ (there is at least one group difference), we still do **not** know which specific pairs differ. **Post-hoc tests** (uji pasca-hoc) identify the responsible pairs while controlling the overall Type I error rate (tingkat galat tipe I).

### Common post-hoc methods (Metode Lanjutan Umum)

| Test | Controls | Use when... | Bahasa Indonesia |
|------|----------|-------------|------------------|
| **Tukey-Kramer (HSD)** | Family-wise error rate (FWER) | All pairwise comparisons; group sizes may be unequal | Perbandingan berpasangan; ukuran kelompok bisa tidak sama |
| **Bonferroni** | FWER via $\alpha/m$ correction | Small number of planned comparisons | Jumlah perbandingan sedikit |
| **Scheffé** | FWER for all contrasts | Complex comparisons (tidak terduga) | Perbandingan kompleks/kontras |
| **Dunnett** | FWER for comparisons vs. one control | One treatment vs. several controls | Satu perlakuan vs. kontrol |
| **SNK (Student-Neuman-Keuls)** | Per-comparison error rate | Exploratory pairwise groupings | Pengelompokan eksploratori |

### Tukey-Kramer Formula

$$
q = \frac{|\bar{y}_i - \bar{y}_j|}{\sqrt{MS_{\text{Within}} \left( \frac{1}{n_i} + \frac{1}{n_j} \right)}}
$$

Reject $H_0: \mu_i = \mu_j$ if $q > q_{\alpha}(k, N-k)$, where $q_{\alpha}$ is the studentised range critical value.

## ANOVA in Geodesy and Surveying

In geodesy, ANOVA is applied to:

1. **Compare survey techniques** — e.g., does GNSS static produce significantly different baseline errors than RTK for the same network?
2. **Assess different GNSS processing software** — running the same baselines through Gamit, Bernese, RTKLIB, and comparing the resulting coordinate differences.
3. **Evaluate geoid model accuracy** — comparing undulation differences derived from EGM2008, EGM96, and mixed terrestrial-satellite data across survey stations.
4. **Temporal analysis** — determining whether seasonal variations (musiman) in GNSS station coordinates are statistically significant or within noise.

For repeated-measures spatial data (pengukuran berulang pada titik yang sama sepanjang waktu), a **repeated-measures ANOVA** accounts for the correlation between observations taken at the same location.

## Non-parametric alternatives (Alternatif Non-parametrik)

When ANOVA assumptions are violated:
- **Kruskal-Wallis test** → one-way ANOVA without normality assumption (uji peringkat).
- **Friedman test** → two-way ANOVA without normality assumption for blocked/repeated data (data tersarang).

## Related
- [[Probability Foundations]] · [[Hypothesis Testing]] · [[Descriptive Statistics]]

---
*Concept maintained by AIGIS — part of [[Probability Foundations]]*
