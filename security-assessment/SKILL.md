# Security Assessment

## Cel

Przeprowadź uporządkowaną ocenę bezpieczeństwa wskazanego
hosta, serwera lub usługi.

## Zasady

- Nie wykonuj działań destrukcyjnych.
- Najpierw zbierz informacje, potem wyciągaj wnioski.
- Oddzielaj fakty od hipotez.
- Nie zakładaj, że port oznacza działającą usługę.
- Każde ustalenie powinno mieć evidence.

## Evidence Discipline

- Never invent, infer, or reuse technical facts that are not present
  in the current assessment evidence.
- Every finding must reference explicit evidence collected during
  the current assessment.
- If evidence is unavailable, state "Not verified".
- Do not convert assumptions into findings.
- Do not use knowledge from previous sessions as evidence.
- Distinguish:
  - observed fact
  - interpretation
  - hypothesis
  - recommendation.
- Never report a port, service, container, version, configuration,
  firewall rule or vulnerability unless it was explicitly observed
  or returned by an available tool.

### Finding validation

Before reporting a finding, verify:

1. Is the underlying fact explicitly present in collected evidence?
2. Can I point to the exact tool result supporting it?
3. Am I confusing a known configuration with the current state?
4. Am I assuming something because it is common or expected?

If any answer is uncertain, mark the item as "Not verified"
and do not present it as an observed finding.
## Workflow

1. Zidentyfikuj zakres.
2. Ustal dostępne informacje.
3. Wykonaj discovery.
4. Zidentyfikuj usługi i wersje.
5. Sprawdź potencjalne podatności.
6. Oceń ryzyko.
7. Przygotuj rekomendacje.

## Wynik

Raport powinien zawierać:

### Executive Summary

### Scope

### Findings

Dla każdego:
- severity
- evidence
- impact
- recommendation

### Quick Wins

### Next Steps
