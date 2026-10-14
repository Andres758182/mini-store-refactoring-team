# Mini Store — Refactoring with a Safety Net

Software Design — Code Smells, Refactoring Techniques, and Testing & Testability

## 1. Overview

In this practice, you will improve the internal design of an existing Python application while preserving its observable behavior.

You will work with an existing codebase containing design problems, automated tests, and a GitHub Actions Continuous Integration (CI) workflow.

The main challenge is not simply to make the code cleaner. It is to identify a meaningful design problem, protect existing behavior with tests, apply justified refactoring techniques, and demonstrate that the software continues to work.

### Learning objectives

By the end of this practice, you should be able to:

- Diagnose a design problem using evidence from existing code.
- Explain why the problem could complicate future changes.
- Identify behaviors that must remain unchanged.
- Write meaningful tests before modifying production code.
- Apply refactoring techniques incrementally.
- Use Git commits to demonstrate the sequence of your work.
- Use GitHub Actions to verify that tests pass.
- Interpret test coverage without treating it as a target.
- Participate in a meaningful peer review.

**Important:** This is a Software Design practice. The objective is to improve design safely, not to maximize test coverage or eliminate every code smell.

---

## 2. Team Organization

### Team size

Work in teams of **2–4 students**.

Solo work is not allowed.

### One repository per team

**Each team must have exactly ONE shared GitHub repository.**

All team repositories **MUST be PUBLIC**.

Only one team member, designated as the **Team Lead**, creates the repository.

The other team members must NOT create additional repositories from the instructor's template.

### Responsibilities

| Role | Responsibility |
| --- | --- |
| Team Lead | Create the team's public repository from the instructor's template and invite teammates. |
| All members | Clone the same team repository to their own computers. |
| All members | Configure their own Python environment. |
| All members | Work on their assigned case using their own branch. |
| All members | Add tests, refactor, and create their own Pull Request. |
| All members | Review at least one teammate's Pull Request. |
| All members | Submit individual evidence in Canvas. |

The Team Lead is responsible for the initial repository setup, but **does not perform the other students' work**.

Every student must use their own GitHub account.

### Case assignments

Assign one case to each student:

| Case | Focus | Production file |
| --- | --- | --- |
| A | Pricing | `src/mini_store/pricing.py` |
| B | Notifications | `src/mini_store/notifications.py` |
| C | Checkout | `src/mini_store/checkout.py` |
| D | Shipping | `src/mini_store/shipping.py` |

- Teams of 2: Cases A–B.
- Teams of 3: Cases A–C.
- Teams of 4: Cases A–D.

Each student is responsible for diagnosing, testing, and refactoring their assigned case.

---

## 3. Create the Team Repository

**WHO:** Team Lead only.

**WHERE:** GitHub website.

**DO THIS ONLY ONCE PER TEAM.**

### Step 1 — Open the instructor's template

Open:

https://github.com/raymundotorres/mini-store-refactoring-starter

You must be signed in to your own GitHub account.

### Step 2 — Create the repository

1. Click **Use this template**.
2. Select **Create a new repository**.
3. Under **Owner**, select your GitHub account.
4. Enter a repository name.

   Suggested name:

   `mini-store-refactoring-team-XX`

   Replace `XX` with your team number or identifier.

5. Under **Visibility**, select **Public**.
6. Leave **Include all branches** unchecked.
7. Click **Create repository**.

**IMPORTANT: The repository must be PUBLIC.**

Do not select Private.

### Step 3 — Confirm repository contents

Your new repository should contain:

- `README.md`
- `pyproject.toml`
- `.gitignore`
- `.vscode/settings.json`
- `.github/workflows/ci.yml`
- `.github/pull_request_template.md`
- `src/mini_store/`
- `tests/`

Do not modify any files yet.

### Step 4 — Invite your teammates

1. Open your new repository on GitHub.
2. Select **Settings**.
3. Open **Collaborators** or **Collaborators and teams** under Access.
4. Select **Add people**.
5. Enter each teammate's GitHub username.
6. Send the invitations.

Each teammate must accept their invitation.

### Step 5 — Share the repository URL

Send the URL of the team's repository to every teammate.

For example:

`https://github.com/<team-lead-username>/mini-store-refactoring-team-XX`

**This is the repository everyone will use.**

Do not send teammates to the instructor's template to create their own repositories.

### Step 6 — Verify initial CI

1. Open the team's repository on GitHub.
2. Select the **Actions** tab.
3. Open the latest **CI** workflow execution for `main`.
4. Confirm that the `test` job completes successfully.
5. Expand **Run tests with coverage**.
6. Record the initial coverage results.

The unmodified starter contains:

- 11 automated tests.
- Approximately 58% overall coverage, including branch coverage.

Your team's initial results should be comparable.

Keep this initial result available for later comparison.

---

## 4. Clone the Team Repository

**WHO:** Every student, including the Team Lead.

**WHERE:** VS Code.

Each student needs their **own local copy** of the same shared repository.

**Cloning does not create another GitHub repository.**

It creates a copy of the existing team repository on your computer.

### Step 1 — Copy the repository URL

1. Open your team's repository on GitHub.
2. Click the green **Code** button.
3. Select **HTTPS**.
4. Click the copy icon next to the repository URL.

Make sure you are copying your **team repository**, not the instructor's starter.

### Step 2 — Clone using VS Code

1. Open Visual Studio Code.
2. Press:

   - **macOS:** `Cmd + Shift + P`
   - **Windows/Linux:** `Ctrl + Shift + P`

3. Type `Git: Clone`.
4. Select **Git: Clone**.
5. Paste your team's repository URL.
6. Press Enter.
7. Choose a folder on your computer where you want to store the project.
8. Wait for VS Code to complete the clone.
9. When asked whether to open the cloned repository, select **Open**.
10. If VS Code asks whether you trust the folder, select **Yes, I trust the authors**, provided you recognize it as your team's repository.

### Step 3 — Verify the project

In VS Code's Explorer, you should see:

- `src`
- `tests`
- `README.md`
- `pyproject.toml`

Make sure VS Code opened the **repository folder**, not just an individual Python file.

**Do not edit production code yet.**

---

## 5. Configure Python in VS Code

**WHO:** Every student.

**WHERE:** Your own computer.

**IMPORTANT: Every student must complete this section independently.**

The Python environment is local to your computer.

Even if a teammate has already configured Python successfully, you must configure your own environment.

### Prerequisites

You need:

1. Visual Studio Code.
2. Python 3.10 or later.
3. The Microsoft **Python** extension for VS Code.
4. The Microsoft **Python Environments** extension for VS Code.

Python 3.13 is recommended because it matches the version used by GitHub Actions.

If Python is not installed, install a supported version before continuing.

If VS Code cannot detect your Python installation, ask the instructor for assistance.

### What is a virtual environment?

A Python virtual environment is an isolated location containing the Python interpreter and packages needed by a particular project.

This project uses a virtual environment so that its testing tools do not interfere with packages installed elsewhere on your computer.

We will create an environment named `.venv`.

**You do not need to use the terminal.**

### Step 1 — Open the correct folder

Make sure VS Code has opened your cloned team repository.

Check that `pyproject.toml` is visible in the Explorer.

### Step 2 — Open the Command Palette

Press:

- **macOS:** `Cmd + Shift + P`
- **Windows/Linux:** `Ctrl + Shift + P`

### Step 3 — Create the environment

1. Type `Python: Create Environment`.
2. Select **Python: Create Environment**.
3. Choose **Venv**.
4. Select an installed Python interpreter.

   Recommended: **Python 3.13**.

5. Follow the prompts to create the environment.

VS Code should create a folder named `.venv` inside your project.

**Do not manually create or edit files inside `.venv`.**

### Step 4 — Install project dependencies

During environment creation, VS Code should ask whether you want to install project dependencies.

1. Select **Install project dependencies**.
2. Find the dependency option associated with `pyproject.toml`.
3. Select the **`test`** dependency group.

Depending on your VS Code version, the option may appear similar to:

`test -e <project path>`

4. Confirm your selection.
5. Wait for the installation to finish.

This installs the testing tools required by the project:

- `pytest`
- `pytest-cov`

**Do not skip this step.**

Installing Python alone is not sufficient to run the project's tests.

You do not need to select the plain `pyproject.toml` entry in addition to the `test` group.

### Step 5 — Verify the Python interpreter

1. Open the Command Palette again.
2. Type `Python: Select Interpreter`.
3. Select **Python: Select Interpreter**.
4. Choose the interpreter located inside your project's `.venv` folder.

The selected interpreter should resemble:

**macOS/Linux**

`.venv/bin/python`

**Windows**

`.venv\Scripts\python.exe`

The precise full path will depend on your computer.

**Do not use a global Python interpreter if your project has a `.venv` environment.**

### Step 6 — Confirm local-only files

The `.venv` folder belongs only to your local computer.

It must NOT be committed or pushed to GitHub.

The repository includes a `.gitignore` file to exclude virtual environments and other generated files.

Do not modify `.gitignore` to force these files into Git.

---

## 6. Run the Starter Tests

**WHO:** Every student.

**WHERE:** VS Code.

Complete this section before modifying production code.

### Step 1 — Open Testing

1. Locate the **Testing** icon in VS Code's Activity Bar.
2. Click the flask-shaped icon.
3. Wait for VS Code to discover the project's tests.

If tests do not appear, click **Refresh Tests**.

The repository includes four test files:

- `tests/test_pricing.py`
- `tests/test_notifications.py`
- `tests/test_checkout.py`
- `tests/test_shipping.py`

### Step 2 — Run all tests

1. In the Testing panel, locate **Run Tests** or **Run All Tests**.
2. Click the run icon.
3. Wait for execution to finish.

**Expected result: 11 tests passing.**

If any test fails, investigate before continuing.

Do not modify production code to resolve an environment-configuration problem.

### Step 3 — Run tests with coverage

1. In the Testing panel, open the available test execution options.
2. Select **Run Tests with Coverage**.
3. Wait for the results.
4. Inspect the coverage information.

The starter's overall baseline is approximately **58% coverage**, including branches.

Individual production modules will have different percentages.

Record the coverage of your assigned module.

### Step 4 — Verify your setup

Before starting the exercise, confirm all of the following:

- [ ] I am working in my team's shared GitHub repository.
- [ ] My team's repository is PUBLIC.
- [ ] I cloned the repository to my own computer.
- [ ] My project has a `.venv` environment.
- [ ] VS Code is using the project's virtual environment.
- [ ] The testing dependencies are installed.
- [ ] VS Code discovers the starter tests.
- [ ] All 11 starter tests pass.
- [ ] I can run tests with coverage.
- [ ] The team's initial CI workflow passed on GitHub.

**Do not begin the refactoring exercise until your environment works correctly.**

---

## 7. Troubleshooting

### Problem: `No module named pytest`

**Likely cause:** VS Code is using a Python interpreter that does not have the project's testing dependencies installed.

**Solution:**

1. Open the Command Palette.
2. Select **Python: Select Interpreter**.
3. Check whether the selected interpreter belongs to your `.venv` folder.
4. If no virtual environment exists, return to Section 5 and create one.
5. Make sure you select the `test` dependency group when installing project dependencies.
6. Refresh the Testing panel.

Do not attempt to fix this by installing packages into the system Python interpreter.

### Problem: VS Code cannot discover any tests

Check the following:

1. Did you open the repository folder?
2. Does the Explorer show `pyproject.toml`?
3. Is the Python extension installed and enabled?
4. Is the correct `.venv` interpreter selected?
5. Were the `test` dependencies installed?

Then select **Refresh Tests** in the Testing panel.

### Problem: Python 3.13 does not appear

Verify that Python is installed on your computer.

You may use another supported version (Python 3.10 or later), although Python 3.13 is recommended.

If VS Code cannot locate your installation, ask the instructor for assistance.

### Problem: GitHub Actions passes, but local tests do not run

GitHub Actions uses its own Python environment.

A successful GitHub Actions run does not automatically configure Python on your computer.

Complete Section 5 to configure your local environment.

### Problem: I cannot push my changes

Verify that:

1. You are signed into your own GitHub account.
2. You cloned your team's repository.
3. You accepted the repository collaborator invitation.
4. You created your own working branch.
5. You are not accidentally working in the instructor's repository.

### Problem: My push did not trigger GitHub Actions

This repository's workflow runs on:

- Pushes to `main`.
- Pull Requests targeting `main`.

A push to your individual working branch does **not** automatically trigger CI unless that branch has an open Pull Request targeting `main`.

Open a **Draft Pull Request** as described in Section 9 to trigger CI without merging your changes.

---

## 8. Diagnose Your Assigned Case

**WHO:** Every student, working on their assigned case.

Before changing production code:

1. Read your assigned production module.
2. Read its existing tests.
3. Identify a meaningful design problem.
4. Explain why the current structure could make a future change difficult.
5. Describe a plausible future change scenario.
6. Identify the behaviors that must remain unchanged.

Base your diagnosis on observable code evidence.

You are not required to eliminate every code smell.

A code smell is a reason to investigate, not an automatic instruction to perform a particular refactoring.

---

## 9. Required Workflow — Tests Before Refactoring

This is the most important part of the practice.

**You must add and verify your new tests BEFORE changing production code.**

Your Git history must demonstrate this sequence.

### Phase A — Create your working branch

Use VS Code's Source Control interface.

1. Open **Source Control**.
2. Select the current branch name.
3. Choose **Create new branch**.
4. Enter a name identifying your case.

Suggested names:

- `case-a-pricing`
- `case-b-notifications`
- `case-c-checkout`
- `case-d-shipping`

5. Confirm that VS Code has switched to your new branch.

**Do not work directly on `main`.**

Each student must use their own branch.

### Phase B — Add your safety-net tests

Before modifying production code:

1. Examine the existing tests for your case.
2. Identify important behaviors that are insufficiently protected.
3. Consider relevant boundaries, alternative paths, and failure scenarios.
4. Add or improve meaningful unit tests.
5. Run the complete test suite locally.
6. Confirm that all tests pass.

Your new tests must validate the **current observable behavior** of the application.

**Do not modify production code during this phase.**

### Phase C — Commit your tests

1. Open VS Code's **Source Control** panel.
2. Review the changed files.
3. Confirm that your changes contain only test-related modifications.
4. Stage the changes.
5. Enter a commit message.

Suggested message:

`Add safety-net tests for Case A`

Adapt the case identifier as needed.

6. Commit the changes.
7. Push your branch to GitHub.

You now have a Git commit containing your tests, while the original production code remains unchanged.

### Phase D — Open a Draft Pull Request

1. Open your team's repository on GitHub.
2. Locate your recently pushed branch.
3. Select **Compare & pull request**, if available.
4. Confirm:

   - Base branch: `main`
   - Compare branch: your working branch

5. Enter a descriptive title.

   Example:

   `Case A — Pricing refactoring`

6. Select **Create draft pull request**.

If GitHub initially offers a regular Pull Request, use the available menu or subsequent option to create or convert it to **Draft**.

**Do not merge this Pull Request.**

You will continue using it throughout the exercise.

### Phase E — Verify CI before refactoring

1. Open your Draft Pull Request on GitHub.
2. Locate its checks or GitHub Actions results.
3. Wait for the **CI** workflow to finish.
4. Confirm that the `test` job passes.
5. Open the job details if necessary.
6. Verify that the automated tests passed.

Keep a link or screenshot of this successful execution.

**MANDATORY CHECKPOINT**

Before modifying any production code, you must have:

- [ ] Added or improved meaningful tests.
- [ ] Executed those tests locally.
- [ ] Committed the test changes.
- [ ] Pushed your branch.
- [ ] Opened a Draft Pull Request.
- [ ] Obtained a successful CI result.

**DO NOT BEGIN REFACTORING UNTIL ALL SIX CONDITIONS ARE MET.**

This is required so that the sequence can be verified later.

### Phase F — Refactor the production code

Now you may begin refactoring.

1. Return to VS Code.
2. Confirm that you are still on your own branch.
3. Open your assigned production module.
4. Apply an appropriate refactoring technique.
5. Make small, focused changes.
6. Run the relevant tests after each meaningful change.
7. Keep observable behavior unchanged.
8. Avoid unrelated rewrites or unnecessary improvements.

Refactoring should improve the structure of the code without intentionally changing what it does.

If tests fail, investigate before continuing.

### Phase G — Commit and push your refactoring

Once your refactoring is complete:

1. Run the full test suite locally.
2. Confirm that all tests pass.
3. Review your changes in Source Control.
4. Commit the production-code refactoring separately from your initial test commit.

Suggested message:

`Refactor Case A pricing design`

5. Push your changes.

You may create multiple refactoring commits if appropriate.

Pushing to the same branch updates your existing Draft Pull Request.

You do not need to create another Pull Request.

### Phase H — Verify final CI and coverage

1. Open your existing Draft Pull Request.
2. Wait for the new CI execution.
3. Confirm that all tests pass.
4. Review the coverage results.
5. Compare them with the initial baseline.
6. Record your final coverage.

**Coverage must not decrease.**

There is **no required final coverage percentage**.

The quality and relevance of your tests matter more than increasing a number.

You may add additional tests if you discover important unprotected behaviors.

Explain why those tests are meaningful.

### Required Git history

Your work must clearly demonstrate:

**Tests → Commit → Push → Green CI → Refactoring → Commit → Push → Green CI**

Both stages belong to the **same working branch and Pull Request**.

The initial test commit must appear before the production-code refactoring commits.

---

## 10. Peer Review and Merge

### Complete your Pull Request

Once your refactoring and final verification are complete:

1. Open your Draft Pull Request.
2. Complete the provided Pull Request template.
3. Explain your diagnosis and design decisions.
4. Include evidence of your initial safety-net commit.
5. Include evidence that CI passed before refactoring.
6. Include initial and final coverage.
7. Mark the Pull Request as **Ready for review**.

### Request a review

Request a review from a teammate.

Your reviewer should evaluate:

- Whether the design problem was properly justified.
- Whether the proposed refactoring addresses that problem.
- Whether tests protect relevant behavior.
- Whether observable behavior was preserved.
- Whether unnecessary complexity was introduced.
- Whether the refactoring remained appropriately focused.

### Review a teammate's work

Every student must review at least one teammate's Pull Request.

A meaningful review includes design reasoning, test quality, or relevant implementation feedback.

A review does not need to invent problems.

Approving a well-justified solution is acceptable.

### Complete the workflow

1. Respond to review feedback on your own Pull Request.
2. Make additional changes when justified.
3. Confirm that CI is green.
4. Obtain the required review.
5. Merge the Pull Request into `main`.

Each student must complete their individual Pull Request.

Do not merge a teammate's work without coordinating with them.

---

## 11. Human Baseline — AI Restriction

This practice establishes a **human baseline** for a later AI-assisted refactoring exercise.

**Generative AI is NOT allowed during this practice.**

Do not use generative AI to:

- Diagnose code smells.
- Identify or select refactoring techniques.
- Write or generate tests.
- Generate production code.
- Perform the refactoring.
- Produce your design reasoning or reflection.

You may use:

- Official documentation.
- Ordinary web search.
- VS Code.
- Python and pytest.
- Git and GitHub.
- GitHub Actions.

The purpose is to develop and demonstrate your own reasoning before comparing it with AI-assisted approaches in a later exercise.

---

## 12. Pull Request Documentation

Use the provided `.github/pull_request_template.md`.

Your Pull Request should explain:

1. **Diagnosis**
   - What design problem did you identify?
   - What evidence supports your diagnosis?
   - What plausible future change makes it relevant?

2. **Safety net**
   - Which behaviors must remain unchanged?
   - Which tests did you add or improve?
   - Which commit contains the tests?
   - Did CI pass before refactoring?

3. **Refactoring**
   - What structural changes did you make?
   - Why do they improve the design?
   - What did you deliberately leave unchanged?

4. **Verification**
   - Do all tests pass?
   - Did final CI pass?
   - What was the initial coverage?
   - What is the final coverage?
   - How do you know observable behavior was preserved?

---

## 13. Individual Canvas Submission

**Every student submits their own evidence in Canvas.**

A shared repository does not replace individual submissions.

Include:

### A. Identification

- Team repository URL.
- Assigned case.
- Your GitHub username.
- Your working branch.

### B. Pull Request

- URL of your own Pull Request.

### C. Diagnosis

- The design problem identified.
- Evidence from the original code.
- A plausible future change scenario.

### D. Safety-net evidence

- Initial tests passing.
- Tests added or improved before refactoring.
- Link to your test-only commit.
- Evidence of successful CI before refactoring.

### E. Refactoring evidence

- Description of your structural changes.
- Explanation of the design improvement.
- Link to your refactoring commit or commits.

### F. Final verification

- All tests passing.
- Initial and final coverage.
- Successful final CI.
- Explanation of behavior preservation.

### G. Peer review

- Evidence of your review of a teammate's Pull Request.
- Evidence that your own Pull Request was reviewed and merged.

### H. Reflection

Briefly explain:

- What you learned about refactoring with a safety net.
- What you deliberately chose not to change, and why.

---

## 14. Final Checklist

Before submitting your work, verify:

### Team setup

- [ ] Our team has exactly one shared GitHub repository.
- [ ] The repository is PUBLIC.
- [ ] All team members are collaborators.
- [ ] Each member has their own local clone.
- [ ] Each member has their own working branch.

### Environment

- [ ] I created my own `.venv` environment.
- [ ] I installed the `test` dependencies.
- [ ] VS Code discovers the tests.
- [ ] I can run tests and coverage locally.

### Safety net

- [ ] I diagnosed my assigned design problem.
- [ ] I added or improved meaningful tests.
- [ ] I committed and pushed my tests before refactoring.
- [ ] CI passed with my new tests and the original production code.

### Refactoring

- [ ] I applied justified structural improvements.
- [ ] I preserved observable behavior.
- [ ] I committed refactoring changes separately.
- [ ] All tests pass.
- [ ] Final CI passes.
- [ ] Coverage has not decreased.

### Collaboration

- [ ] I documented my work in my Pull Request.
- [ ] A teammate reviewed my Pull Request.
- [ ] I reviewed at least one teammate's Pull Request.
- [ ] My Pull Request was merged.

### Submission

- [ ] I submitted my individual evidence in Canvas.
- [ ] My submission includes links to my branch, commits, and Pull Request.
- [ ] My reflection explains my decisions.

---

## Remember

The objective is not to produce the shortest code or achieve the highest coverage.

The objective is to demonstrate that you can:

**Understand existing behavior → Protect it with tests → Improve the design → Verify the result.**

Your Git history and Pull Request should make that process clear.