# Agent Specification: Automated Creative Analysis & Scoring (ACAS)

## 1. Overview
The ACAS Agent is a specialized AI service within the Creative Unlock AI ecosystem. Its primary function is to ingest raw creative assets (images, videos, copy, layouts), extract meaningful metadata, and evaluate the work against industry-standard benchmarks and specific job requirements.

## 2. Core Objectives
- **Standardization:** Convert diverse creative outputs into the proprietary `JSON-C` (Creative Schema) format.
- **Objective Evaluation:** Provide non-biased scoring across four pillars: Technical Execution, Style Consistency, Commercial Viability, and Innovation.
- **Feedback Loop:** Generate actionable insights for the creative to improve their "Pitch Score."

## 3. Agent Logic Flow
1. **Ingestion:** Receive asset URLs and user-provided descriptions.
2. **Multimodal Analysis:**
    - **Vision Model (e.g., GPT-4o / Claude 3.5 Sonnet):** Analyzes composition, color theory, typography, and brand alignment.
    - **NLP Model:** Analyzes tone of voice, grammar, and persuasive impact of the copy.
3. **Scoring Engine:** Applies weighted algorithms based on the "Job Context" (e.g., a logo for a law firm vs. a mural for a tech startup).
4. **Validation:** Cross-references findings with the "Global Creative Standard" database.
5. **Output:** Returns a signed `AnalysisReport` object.

## 4. Scoring Metrics (The "Creative Quadrant")
| Metric | Description | Weight (Default) |
| :--- | :--- | :--- |
| **Technical Skill** | Proficiency in tools, resolution, grid systems, and syntax. | 30% |
| **Style Index** | Consistency in aesthetic across the portfolio. | 20% |
| **Market Fit** | How well the work aligns with current industry trends/demands. | 35% |
| **Originality** | Detection of unique patterns vs. generic templates. | 15% |