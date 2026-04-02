---
title: Healthcare OpenEnv
emoji: 🏥
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# Healthcare OpenEnv Environment

## Description
This project simulates a healthcare diagnosis system where an AI agent predicts diseases based on symptoms.

## Features
- AI-based decision environment
- 3 tasks (easy → hard)
- Reward-based learning
- API endpoints (step/reset/state)

## How it works
- `/reset` → generates patient data
- `/step` → agent takes action
- `/state` → current environment state