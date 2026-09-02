# SLE-1: Rule-Based Student Study Recommendation Agent

## Student Details

- **PRN:** 26UAM302
- **Name:** Jyoti Prakash Chavan
- **Course:** 02AML204 – Introduction to Artificial Intelligence
- **SLE:** SLE-1
- **Programming Language:** Python

---

## 1. Project Overview

This project implements a simple rule-based AI agent called the Student Study Recommendation Agent.

The agent takes information from the user and uses predefined rules to recommend a suitable study strategy.

The project demonstrates the basic concept of an intelligent agent using rule-based decision making.

---

## 2. AI Concept Used

### Rule-Based Agent

A rule-based agent makes decisions by applying predefined IF/ELSE rules to the information received from the user.

In this project, the agent considers:

- Available study hours per day
- Subject difficulty
- Number of days remaining before the exam

Based on these inputs, it produces a study recommendation.

---

## 3. How the Agent Works

The basic workflow is:

User Input
↓
Study Hours + Difficulty + Exam Days
↓
Rule-Based Decision Making
↓
Recommendation
↓
Output

For example:

IF exam days are less than or equal to 3
AND subject difficulty is high

THEN recommend focusing on difficult concepts and important problems.

---

## 4. Features

- Accepts study hours as input.
- Accepts subject difficulty as input.
- Accepts remaining exam days as input.
- Applies predefined decision rules.
- Produces a study recommendation.
- Uses Python functions and conditional statements.

---

## 5. Requirements

- Python 3.x
- Command Prompt / Terminal

No external Python libraries are required.

---

## 6. How to Run

Open a terminal or Command Prompt in the project folder.

Run:

```bash
python ai_agent.py
