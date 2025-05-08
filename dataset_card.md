
---
license: mit
dataset_info:
  features:
    - name: row_id
      dtype: string
    - name: prompt_id
      dtype: string
    - name: profile
      dtype: string
    - name: formatted_prompt
      dtype: string
    - name: Response
      dtype: string
    - name: human_coherence
      dtype: int32
    - name: human_hallucination
      dtype: int32
    - name: human_contradiction
      dtype: int32
    - name: human_deviation
      dtype: int32
    - name: human_leak
      dtype: int32
    - name: human_repetition
      dtype: int32
    - name: auto_coherence
      dtype: int32
    - name: auto_hallucination
      dtype: int32
    - name: auto_contradiction
      dtype: int32
    - name: auto_deviation
      dtype: int32
    - name: auto_prompt_leak
      dtype: int32
    - name: auto_repetition
      dtype: int32
task_categories:
  - text-classification
language:
  - en
---

# A Novel Biomimetic Approach to Red Teaming A.I. Models

This dataset simulates neurodiverse prompt profiles to evaluate LLM safety, reliability, and behavioral fidelity. Human and auto tags identify hallucinations, contradictions, prompt leaks, repetition, and coherence failure. It is designed to guide future diagnostics in AI safety and alignment.

Creator: Paul J. Lesevic  
License: MIT  
