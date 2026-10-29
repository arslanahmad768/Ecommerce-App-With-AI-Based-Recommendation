# Pull Request: Add project README and PR description

## Summary

This PR adds a professional `README.md` that documents the project: its features, the machine learning components behind the recommendation engine, the tech stack, the project structure, setup instructions, and the main API endpoints. It also adds this `PR_DESCRIPTION.md` file for reviewers.

No application code, models, or configuration files are changed.

## Changes

- **Added `README.md`**
  - Project overview and feature list (storefront, ML recommendations, price prediction, sentiment analysis, admin dashboard)
  - Tech stack table and annotated project structure
  - Step-by-step local setup, including the required environment variables
  - API endpoint overview
  - Description of the serialised ML artefacts in `model/`
  - Contribution guidelines
- **Added `PR_DESCRIPTION.md`** (this file)

## Why

The repository had no README, so new contributors and reviewers had no entry point for understanding or running the project. This PR provides that documentation.

## How to Review

1. Read `README.md` and check that the setup steps match your local environment.
2. Confirm the environment variable table matches `Eshop/settings.py`.
3. Check the API endpoint table against `products/urls.py` and `products/views.py`.

## Testing

- [x] Markdown renders correctly on GitHub (headings, tables, code blocks)
- [ ] Setup steps were followed end to end on a clean machine
- [ ] Docker instructions verified (see Known Limitations)

## Known Limitations

- The `Dockerfile` currently contains only a `FROM python:3.9.19-alpine3.19` line and does not install dependencies or start the app. The "Running with Docker" section of the README will not work until the Dockerfile is completed.
- Some API endpoints are documented from the URL configuration and have not yet been exercised by automated tests.

## Follow-up Work

- Complete the `Dockerfile` and verify the Docker instructions
- Add a `LICENSE` file and update the README's contribution section to match
- Add automated tests for the recommendation and checkout flows
