# Candidate Location Scoring Method

This document explains how GeoTrace users can compare possible photo locations when EXIF, GPS, or camera metadata is missing.

The goal is not to prove a location too quickly. The goal is to organize evidence, compare candidates, and explain confidence clearly.

## 1. What Is a Candidate Location?

A candidate location is a possible place where a photo may have been taken.

A candidate can be broad or specific:

- Country
- Region
- City
- Village
- Road
- Landmark
- Building
- Business
- Natural area

Examples:

```text
Austria
Salzkammergut, Austria
Hallstatt, Austria
A beer garden near Lake Wolfgang
A wooden chalet near a mountain road
```
## 2. Evidence Types

GeoTrace separates evidence into categories.

### Strong Evidence

Strong evidence directly supports a location.

Examples:

- Readable street sign
- Business name with known address
- Unique landmark
- GPS metadata
- Recognizable mountain profile
- Local phone number prefix
- Website domain or local company name

### Medium Evidence

Medium evidence supports a region but may not identify one exact place.

Examples:

- Language or alphabet
- Architecture style
- Road signs
- License plate format
- Tree or vegetation type
- Terrain or climate
- Public transport style
- Animal breeds or livestock associated with a region

### Weak Evidence

Weak evidence is useful but not enough alone.

Examples:

- General building color
- Common trees
- Weather
- Outdoor furniture
- Generic mountain view
- Common restaurant or café style
- Generic animals without clear regional signal

## 3. Scoring Scale

Use a score from **0 to 100**.

| Score Range | Confidence Level | Meaning |
|---|---|---|
| 0–25 | Very Low | Candidate is possible but weakly supported |
| 26–50 | Low | Some clues match, but evidence is limited |
| 51–70 | Medium | Multiple clues support the candidate |
| 71–85 | High | Strong evidence supports the candidate |
| 86–100 | Very High | Multiple independent strong clues support the candidate |

Do not use 100 unless the location is independently verified.

## 4. Evidence Table

Use this table to compare candidates.

| Candidate Location | Evidence For | Evidence Against | Missing Checks | Score |
|---|---|---|---|---|
| Candidate 1 |  |  |  | 0–100 |
| Candidate 2 |  |  |  | 0–100 |
| Candidate 3 |  |  |  | 0–100 |

## 5. Evidence Weighting

Use this simple weighting system.

| Evidence Type | Suggested Weight |
|---|---|
| Unique landmark | +30 |
| Readable place name | +25 |
| Business or address match | +25 |
| Road sign or transport clue | +15 |
| Architecture match | +10 |
| Vegetation or terrain match | +10 |
| Weather or season clue | +5 |
| Generic visual similarity | +5 |

Negative evidence should reduce the score.

| Negative Evidence | Suggested Penalty |
|---|---|
| Language mismatch | -20 |
| Road sign mismatch | -15 |
| Architecture mismatch | -10 |
| Terrain mismatch | -10 |
| Climate mismatch | -10 |
| No supporting unique clue | -5 |

## 6. Example Scoring

Example photo clues:

```text
- Wooden chalet
- Outdoor beer garden
- German-language sign
- Deciduous trees
- Alpine-looking terrain
- Horse ranch or riding facility nearby
- Possible regional horse breed
```

Candidate comparison:

| Candidate Location | Evidence For | Evidence Against | Missing Checks | Score |
|---|---|---|---|---|
| Salzkammergut, Austria | German language, alpine terrain, chalet architecture, beer garden culture | No exact sign or landmark visible | Need business/sign match | 72 |
| Bavaria, Germany | German language, beer garden culture, alpine architecture | Terrain not confirmed, no Bavarian-specific sign | Need road/sign comparison | 64 |
| Alsace, France | Some chalet-style buildings, possible tourism setting | German-language clue less direct, terrain uncertain | Need language/sign confirmation | 42 |

## 7. Confidence Explanation

Always explain the score in plain language.

Use this format:

```text
Candidate:
Score:
Confidence level:
Strongest evidence:
Weakest evidence:
Evidence against:
What needs verification:
```

Example:

```text
Candidate: Salzkammergut, Austria
Score: 72
Confidence level: High

Strongest evidence:
The photo appears to show alpine-style wooden architecture, outdoor beer garden seating, German-language signage, and deciduous vegetation.

Weakest evidence:
No unique landmark, address, or business name is visible.

Evidence against:
The same clues could also match parts of Bavaria or other Austrian alpine regions.

What needs verification:
Compare signs, building style, road layout, and nearby businesses against candidate towns.
```

## 8. Rules for Responsible Scoring

GeoTrace scoring should stay careful and transparent.

- Do not claim certainty from weak clues
- Separate evidence from guesses
- Record evidence against each candidate
- Prefer multiple independent clues
- Explain why a candidate scored high or low
- Keep alternative locations visible
- Update scores when new evidence appears

## 9. Final Candidate Summary

Use this final format after scoring.

```text
Most likely candidate:
Score:
Confidence:
Alternative candidates:
Strongest evidence:
Main uncertainty:
Recommended next step:
```

## 10. What This Method Is Not

This method is not a mathematical proof.

It is a structured reasoning tool. The score helps compare candidates, but the explanation matters more than the number.
