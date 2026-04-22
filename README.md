# Daily Reflection Tree Assignment

## Overview

This project implements a deterministic decision tree for analyzing daily reflections and an optional AI agent that uses the tree to provide structured responses.

---

## Part A: Decision Tree (Deterministic)

A rule-based system that:

* Classifies user emotions
* Identifies intensity and cause
* Provides fixed responses

### Features

* Deterministic outputs (same input → same output)
* Predefined categories
* Structured logic

---

## Guardrails (Important)

To prevent hallucination:

* No generative AI used in Part A
* Only predefined responses
* Strict input validation
* Unknown inputs handled with fallback

---

## Part B: AI Agent (Optional)

A simple AI agent that:

* Takes user input
* Extracts emotion and cause using keyword logic
* Passes data to decision tree
* Returns response

---

## How to Run

```bash
python agent.py
```

---

## Example

Input:
"I feel stressed because of work"

Output:
"Break your tasks into smaller steps and prioritize."

---

## Limitations

* Keyword-based classification (not NLP-based)
* Limited emotional depth
* No real-time learning

---

## Future Improvements

* Use NLP models for better classification
* Add sentiment scoring
* Expand emotional categories
