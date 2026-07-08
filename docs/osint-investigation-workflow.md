# OSINT Investigation Workflow

This document describes the GeoTrace workflow for investigating where a photo may have been taken when EXIF, GPS, or camera metadata is missing.

The goal is to make photo-location research structured, repeatable, and transparent.

GeoTrace does not replace human judgment. It helps users collect clues, compare candidates, and explain confidence clearly.

## 1. Start With Metadata

Begin by checking whether the image contains metadata.

Use the GeoTrace EXIF reader or another trusted metadata tool.

Record:

```text
File name:
File type:
EXIF found: Yes / No
GPS found: Yes / No
Camera model:
Timestamp:
Software/editor:
Other metadata:
```

### Metadata questions

- Does the image contain GPS coordinates?
- Was the image edited or exported from another app?
- Is the timestamp present?
- Could the metadata be missing, stripped, or unreliable?

If GPS metadata exists, treat it as useful evidence, but still verify it with visual clues.

If metadata is missing, continue with visual investigation.

## 2. Record Visible Clues

Use the GeoTrace visual clue checklist.

Record clues from:

- Text, language, and signs
- Buildings and architecture
- Roads, vehicles, and transport
- Trees and vegetation
- Nature and terrain
- Weather, light, and season
- Culture and human activity
- Commercial and digital clues

Do not interpret too quickly. First write down what is actually visible.

Use this format:

```text
Observation:
Possible meaning:
Confidence:
Needs verification:
```

Example:

```text
Observation: German-language sign
Possible meaning: German-speaking region such as Austria, Germany, Switzerland, or parts of other countries
Confidence: Medium
Needs verification: Exact word, spelling, context, and surrounding signs
```

## 3. Separate Observations From Assumptions

This is one of the most important GeoTrace rules.

An observation is something visible in the image.

An assumption is an interpretation of that observation.

| Observation | Assumption |
|---|---|
| A wooden building is visible | It may be a chalet |
| The sign appears German-language | The location may be in a German-speaking region |
| There are mountains in the background | The area may be alpine |
| Outdoor tables are visible | It may be a café, restaurant, or beer garden |

Do not treat assumptions as facts.

## 4. Group Clues by Strength

Classify evidence as strong, medium, or weak.

### Strong clues

- Unique landmark
- Readable place name
- Business name with address
- Road sign with location
- GPS metadata
- Distinctive natural feature

### Medium clues

- Language
- Architecture style
- Road markings
- Transport system
- Vegetation type
- Regional climate or terrain

### Weak clues

- General weather
- Common trees
- Generic buildings
- Outdoor seating
- Common vehicles
- General landscape similarity

Weak clues can help, but they should not carry the investigation alone.

## 5. Create Candidate Locations

Create a list of possible locations.

Candidates can be broad at first:

```text
Austria
Southern Germany
Alpine region
Salzkammergut
Bavaria
```

Then narrow them if stronger clues appear:

```text
Salzkammergut, Austria
Near Lake Wolfgang
Near a horse ranch or chalet-style beer garden
```

Use this table:

| Candidate Location | Why It Is Possible | What Needs Verification |
|---|---|---|
| Candidate 1 |  |  |
| Candidate 2 |  |  |
| Candidate 3 |  |  |

## 6. Search and Compare

Search for evidence that supports or weakens each candidate.

Useful checks include:

- Map search
- Street View
- Satellite view
- Business directories
- Sign/language searches
- Architecture comparisons
- Terrain comparisons
- Local tourism pages
- Public images from the area

Search carefully. Do not only search for evidence that confirms your first guess.

Ask:

```text
What would I expect to see if this candidate is correct?
What would I expect to see if this candidate is wrong?
What evidence is missing?
```

## 7. Score Candidate Locations

Use the GeoTrace candidate-location scoring method.

| Candidate Location | Evidence For | Evidence Against | Missing Checks | Score |
|---|---|---|---|---|
| Candidate 1 |  |  |  | 0–100 |
| Candidate 2 |  |  |  | 0–100 |
| Candidate 3 |  |  |  | 0–100 |

Confidence guide:

| Score Range | Confidence |
|---|---|
| 0–25 | Very Low |
| 26–50 | Low |
| 51–70 | Medium |
| 71–85 | High |
| 86–100 | Very High |

Do not use 100 unless the location is independently verified.

## 8. Write the Reasoning

Every investigation should include a clear explanation.

Use this format:

```text
Most likely location:
Confidence:
Strongest evidence:
Weakest evidence:
Evidence against:
Alternative locations:
What needs verification:
```

Good reasoning should explain:

- Why the top candidate is likely
- Why alternative candidates are less likely
- What evidence is still missing
- What would increase or reduce confidence

## 9. Keep Alternative Candidates Visible

Do not hide alternatives too early.

A strong GeoTrace investigation keeps competing possibilities visible until there is enough evidence to reject them.

Example:

```text
Top candidate: Salzkammergut, Austria
Alternative candidate: Bavaria, Germany
Alternative candidate: Alsace, France
```

Explain why each candidate remains possible or unlikely.

## 10. Responsible Use Rules

GeoTrace should be used carefully.

- Do not expose private people or private homes unnecessarily
- Do not publish sensitive locations without permission
- Do not claim certainty from weak evidence
- Do not use private or copyrighted images without permission
- Separate facts from assumptions
- Record evidence against your preferred answer
- Respect safety, privacy, and legal boundaries

## 11. Final Investigation Output

A completed GeoTrace investigation should include:

```text
Image reference:
Metadata result:
Visible clues:
Candidate locations:
Evidence comparison:
Confidence score:
Final reasoning:
Remaining uncertainty:
Recommended next step:
```

## 12. Workflow Summary

```text
Inspect metadata
↓
Record visible clues
↓
Separate observations from assumptions
↓
Group evidence by strength
↓
Create candidate locations
↓
Search and compare
↓
Score candidates
↓
Write reasoning
↓
Keep alternatives visible
↓
Document final output
```
