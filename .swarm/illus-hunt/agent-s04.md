# Judge s04

**Status:** DONE

## Timeline

### Sheets Viewed (all 11 sheets reviewed)
- 4.1-1: 9 tiles viewed. Candidates: #1, #3, #4, #5, #6 (overview, unified, provisioned PT, production, A/B testing). Rejected: #2, #7-9 (governance/Chapter 7).
- 4.1-2: 9 tiles viewed. UI screenshots: #11-13. Rejected: #14-18 (fine-tuning, agents, other chapters).
- 4.1-3: 6 tiles viewed. Rejected: all (fine-tuning, deep learning, gateway/Chapter 7).
- 4.2-1: 9 tiles viewed. Candidates: #1 (FMAPI architecture), #2-3 (gateway), #5-7 (UI). Rejected: #4, #8-9.
- 4.2-2: 9 tiles viewed. Additional candidates: #10-12, #14-15. Rejected: #13 (dup), #16-18 (other chapters).
- 4.2-3: 3 tiles viewed. Weak: #20-21. Rejected: #19 (agents).
- 4.3-1: 9 tiles viewed. Candidates: #1-3 (overview, infrastructure), #6, #8-9 (MLflow registry). Rejected: #4-5 (text docs).
- 4.3-2: 9 tiles viewed. Candidates: #11 (loss curve), #13-15 (workflows, MLflow). Rejected: #10, #12, #16-18.
- 4.3-3: 6 tiles viewed. Candidates: #19-21 (patterns, lifecycle). Rejected: #22-23 (agents, classical ML).
- 4.4-1: 9 tiles viewed. Candidate: #1 (gateway with external models). Rejected: #2-3 (governance), #4-5 (text), #6-9 (agents).
- 4.4-2: 6 tiles viewed. Candidates: #14 (custom providers), #15 (Model Serving with external models). Rejected: #10-13 (agents).

### Full-Size Verification
Verified best candidates for all points:
- **4.1**: p4.1-serving-overview, p4.1-unified-serving, p4.1-provisioned-pt, p4.1-ab-testing, p4.1-serving-production
- **4.2**: p4.2-fmapi-serving, p4.2-external-models, p4.2-gateway-models
- **4.3**: p4.3-fine-tuning, p4.3-ai-runtime, p4.3-model-training-ui
- **4.4**: p4.4-gateway-governance, p4.4-unified-governance, p4.4-external-guardrails, p4.4-external-provider-setup

### Selection Summary
- **4.1 Model Serving**: 5 kept (overview, unified, provisioned PT, A/B testing, production). Mix of diagrams showing scope, pricing/deployment models, and capabilities.
- **4.2 Foundation Model APIs**: 3 kept (FMAPI architecture, external models overview, future gateway). Architecture and integration focus.
- **4.3 Fine-tuning**: 3 kept (overview, AI Runtime infrastructure, training UI). Covers concept, infrastructure, and workflow.
- **4.4 External Models**: 4 kept (gateway governance, unified governance, external guardrails, provider setup). Limited pure-4.4 visuals; content overlaps with governance (Chapter 7) due to central credential management being intrinsic to external models feature.

## Key Rejections
- Governance/Chapter 7 content (Unity Gateway, AI Guardrails, guardrails architecture)
- Agents (Chapter 5) content
- Fine-tuning/training (Chapter 4.3) content appearing in other points
- Text-heavy slides and tables
- Deprecated/marked-draft content (preferred fresher alternatives)

## Summary
All 4 points covered with 4-5 quality visuals each. 4.4 has fewer dedicated visuals because external models as a feature is fundamentally tied to governance/central credential management (inherent to the feature design, not just Chapter 7 governance). Kept governance-adjacent visuals that specifically show external models' integration into serving platform.
