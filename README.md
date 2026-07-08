# GeoTrace
Open-source toolkit for estimating photo locations when EXIF/GPS metadata is missing, using visual clues, OSINT workflows, and confidence scoring.
# GeoTrace

GeoTrace is an open-source toolkit for estimating where a photo may have been taken when EXIF, GPS, or camera metadata is missing.

It combines metadata inspection, visible-clue extraction, structured OSINT workflows, and confidence-based candidate scoring.

## Why GeoTrace exists

Many images online have their metadata removed. Without EXIF or GPS data, location investigation becomes harder and less repeatable.

GeoTrace helps turn visual clues into a structured investigation process.

## Who it is for

- OSINT learners
- Independent researchers
- Journalists
- Travelers
- Investigators
- Developers building image-intelligence tools

## v0.1 Scope

The first version will focus on a simple workflow:

1. Inspect image metadata
2. Detect missing EXIF/GPS fields
3. Record visible clues
4. List candidate locations
5. Score candidates by confidence
6. Document the reasoning

## Planned Features

- EXIF metadata reader
- Visual clue checklist
- Candidate-location scoring template
- Example investigations
- CLI prototype
- Documentation for repeatable OSINT workflow

## Status

GeoTrace is in early development.

Current milestone: `v0.1 Foundation`
