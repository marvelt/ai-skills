
# Training Analysis

## Purpose

Analyze training data using only data actually retrieved from Intervals.icu.

The analysis must be evidence-driven. Never invent, assume, or silently fill in missing values.

Clearly distinguish between:
- observed facts,
- interpretations,
- hypotheses,
- recommendations.

## Training Analysis Principles

1. Analyze trends rather than isolated values whenever sufficient historical data is available.
2. Compare equivalent or comparable workouts whenever possible.
3. Separate **external load** from **internal load**.
4. Consider pace/speed, heart rate, duration, distance, power, and other available metrics together rather than in isolation.
5. Treat heart rate as context-dependent and avoid interpreting it without considering workout type, duration, intensity, and conditions when available.
6. Do not infer or assume HRmax unless it is supported by available data.
7. Distinguish aerobic efficiency from raw pace or speed.
8. Evaluate recovery and recent training load before recommending an increase in training load.
9. Do not prescribe training changes when the available data is insufficient to support them.
10. When required data is unavailable, explicitly state what is missing.
11. Prefer repeated observations and trends over conclusions based on a single workout.
12. When comparing periods, use comparable time windows and clearly state the comparison period.

## Evidence Discipline

For every significant conclusion:

- Identify the data supporting the conclusion.
- Do not present an interpretation as an observed fact.
- Do not present a hypothesis as a confirmed finding.
- If the evidence is weak or incomplete, state the uncertainty explicitly.
- Never fabricate metrics, activities, training load, recovery data, or physiological parameters.

Use the following distinction:

- **Fact** — directly observed in retrieved data.
- **Interpretation** — reasonable conclusion derived from observed data.
- **Hypothesis** — possible explanation that cannot be confirmed from available data.
- **Recommendation** — proposed action based on the available evidence.

## Data Limitations

If the available Intervals.icu data is insufficient for a requested analysis:

1. State what can be established from the available data.
2. State what cannot be established.
3. Identify the additional data that would be required.
4. Do not compensate for missing data with assumptions.

## Read-Only Rule

Training analysis is strictly read-only.

Never call tools that:
- create Intervals.icu data,
- modify Intervals.icu data,
- delete Intervals.icu data,
- add or modify activities,
- add or modify events,
- add notes or messages,
- create, modify, or delete custom items.

Use only tools required to retrieve data for analysis.

## Analysis Workflow

When performing a training analysis:

1. Define the requested scope and time period.
2. Retrieve the relevant training data.
3. Check whether sufficient data is available.
4. Analyze individual sessions where relevant.
5. Analyze trends and training load.
6. Evaluate recovery when relevant data is available.
7. Identify significant findings.
8. Separate facts from interpretations and hypotheses.
9. Provide recommendations only when supported by sufficient evidence.
10. Clearly state limitations and missing data.

## Output Structure

When appropriate, structure the analysis as:

### Rule
When the analysis specifies a sport or activity type, filter the retrieved
activities accordingly. Other activity types may be reported separately
but must not be included in sport-specific calculations.

### Executive Summary

Short summary of the most important findings.

### Data Scope

Period analyzed and data sources used.

### Observed Training

Relevant factual observations from the retrieved data.

### Training Load & Intensity

Analysis of volume, intensity, distribution, and trends.

### Recovery

Analysis of recovery-related data when available.

### Findings

Important interpretations and possible hypotheses.

### Recommendations

Concrete recommendations supported by the available evidence.

### Limitations

Missing data, uncertainty, and factors that may affect interpretation.

## Data Retrieval Efficiency

When analyzing a time period:

1. Retrieve the required data for the full requested period whenever the MCP
   tool supports range-based retrieval.
2. Reuse already retrieved data instead of repeating identical MCP calls.
3. Do not call the same read-only tool repeatedly unless:
   - the previous result was incomplete,
   - a different date range is required,
   - or additional detail is explicitly needed.
4. Retrieve only the data necessary to answer the question.
5. Prefer one broad retrieval followed by local filtering and analysis over
   multiple overlapping retrievals.

## Avoid Overly Absolute Conclusions

Do not state that a metric or capability "cannot be assessed" when the more
accurate conclusion is that the currently available data is insufficient
for a reliable assessment.

Prefer:
"The available data is insufficient to reliably assess X."

Avoid:
"X cannot be assessed."
