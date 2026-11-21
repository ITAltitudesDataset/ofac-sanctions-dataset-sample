# OFAC Sanctions SDN Dataset — Data Quality Report

**Prepared by IT Altitudes Inc.**

**Dataset:** OFAC Sanctions SDN Reference Dataset  
**Snapshot Date:** September 28, 2026  
**Report Type:** Dataset Quality & Transparency Summary

---

## 1. Executive Summary

This report provides an overview of the OFAC Sanctions SDN Reference Dataset's documented coverage, data structure, quality-review criteria, and known limitations.

The dataset is prepared for research, analytical evaluation, data engineering, and non-production testing.

This report is publisher-issued and does not constitute an independent audit or certification by OFAC.

## 2. Dataset Coverage

| Metric | Documented Value |
|---|---:|
| Full primary SDN records | 19,391 |
| Free preview primary records | 50 |
| Free preview linked addresses | 91 |
| Free preview linked aliases | 215 |
| Snapshot date | September 28, 2026 |
| Original source | U.S. Treasury — OFAC |

These figures are based on the dataset's existing publisher documentation and have not been independently recalculated for this report.

## 3. Data Quality Review Framework

The following checks form the dataset quality-review framework.

| Quality Dimension | Review Objective | Current Evidence Status |
|---|---|---|
| Record completeness | Identify missing and blank values | Detailed measurements pending |
| Duplicate detection | Identify repeated records and identifiers | Detailed measurements pending |
| Schema consistency | Review column names and expected structures | Detailed measurements pending |
| Address relationships | Review primary-to-address linking | Detailed measurements pending |
| Alias relationships | Review primary-to-alias linking | Detailed measurements pending |
| Source provenance | Identify original OFAC source and snapshot | Source documented |
| File readability | Check supported data formats | Format validation results pending |

A check is not considered passed merely because it appears in this framework.

## 4. Missing-Value Assessment

OFAC source records may contain different levels of available information.

Not every missing field necessarily represents a data-quality defect. Some fields may be inapplicable or unavailable in the original source.

### Measurement Status

- Total missing values: Not measured in this report
- Missing-value percentage: Not measured in this report
- Field-level completeness: Pending validation
- Required-field completeness: Pending validation

Detailed statistics should be published only after checking the actual dataset files.

## 5. Duplicate-Record Assessment

Duplicate analysis should distinguish between:

- Repeated primary identifiers
- Repeated complete records
- Multiple legitimate aliases for one primary record
- Multiple legitimate addresses for one primary record

Aliases and addresses should not automatically be treated as duplicate primary SDN records.

**Measured duplicate count:** Pending validation.

## 6. Relational Data Integrity

The buyer kit includes primary SDN information and linked address and alias information.

Recommended integrity checks include:

- Confirming valid references to primary records
- Identifying orphaned address records
- Identifying orphaned alias records
- Checking identifier consistency across related tables

Measured relationship-integrity results will be added after file-level validation.

## 7. Source Attribution & Provenance

**Original Source:** U.S. Department of the Treasury — Office of Foreign Assets Control (OFAC).

The dataset represents a historical reference snapshot and should not be treated as a live sanctions-screening service.

Users should consult official OFAC resources for current sanctions information.

IT Altitudes Inc. is an independent dataset curator and is not affiliated with or endorsed by OFAC.

## 8. Intended Buyer Benefits

This dataset may support:

- Historical sanctions research
- Compliance-related data analysis
- ETL and database testing
- Entity-name matching experiments
- Data quality research
- Academic and educational analysis

These are potential analytical applications, not guarantees of suitability for operational compliance decisions.

## 9. Known Limitations

- Information may change after the snapshot date.
- The dataset does not provide real-time sanctions updates.
- Names, addresses, and aliases may contain source-level variations.
- Missing information may reflect the original OFAC records.
- The dataset does not replace current regulatory due diligence.
- No independently verified quality score is claimed in this report.

## 10. Validation Status

**Current status:** Publisher documentation summary prepared.

**Pending:** Recalculation of completeness, duplicate, schema, and relationship-integrity metrics from the full dataset.

A final quantitative quality score will be published only when supported by recorded validation results.

## 11. License & Disclaimer

- [License & Usage Terms](LICENSE.md)
- [Source & Liability Disclaimer](DISCLAIMER.md)

The dataset is intended for research and analytical use and is not a live compliance or screening tool.

## 12. Full Dataset & Free Preview

**[Purchase the Complete OFAC Sanctions Dataset](https://italtitudes.gumroad.com/l/zkltfw)**

**[Explore the Free GitHub Preview](https://github.com/ITAltitudesDataset/ofac-sanctions-dataset-sample)**

## 13. Contact

**IT Altitudes Inc.**

support@italtitudesdataset.zohodesk.in

---

*Publisher-Issued Dataset Quality & Transparency Report — 2026*
