# Git Cheat Sheet for COMP 590 Labs

Use this as a quick reference when starting and submitting each lab. Replace items in `<ANGLE_BRACKETS>` with the correct value.

## 1. One-Time Git Setup

Set the name and email attached to your commits:

```bash
git config --global user.name "Dimitri Cognata"
git config --global user.email "<YOUR_GITHUB_EMAIL>"
```

Check the global settings:

```bash
git config --global --list
```

## 2. Clone the Repository (First Time Only)

```bash
mkdir -p ~/comp590
cd ~/comp590
git clone git@github.com:comp590-fall26-csuci/Dimitri_cognata.git
cd Dimitri_cognata
```

If the repository already contains submodules, use:

```bash
git clone --recurse-submodules git@github.com:comp590-fall26-csuci/Dimitri_cognata.git
```

Useful checks:

```bash
git remote -v        # Show the connected GitHub repository
git branch -a        # Show local and remote branches
git status           # Show the current branch and file changes
```

## 3. Branches: `branch`, `checkout`, and `switch`

List branches:

```bash
git branch          # Show local branches
git branch -a       # Show local and remote branches
```

Traditional commands:

```bash
git checkout main           # Switch to an existing branch
git branch lab3             # Create lab3 without switching to it
git checkout lab3           # Switch to lab3
git checkout -b lab3        # Create lab3 and switch to it
```

Modern alternatives:

```bash
git switch main             # Switch to an existing branch
git switch -c lab3          # Create lab3 and switch to it
```

`git checkout` is still valid and commonly appears in tutorials, workplaces, and older scripts. However, `checkout` performs multiple jobs, including switching branches and restoring files. Git introduced `git switch` specifically for branch movement, so its purpose is clearer and it is harder to use accidentally on a file.

| Goal | Traditional command | Clearer modern command |
| --- | --- | --- |
| List branches | `git branch` | `git branch` |
| Create branch only | `git branch lab3` | `git branch lab3` |
| Switch branches | `git checkout main` | `git switch main` |
| Create and switch | `git checkout -b lab3` | `git switch -c lab3` |

For new interactive work, prefer `git switch`. Learn both because `git checkout` remains common in documentation and existing workflows.

## 4. Start a New Lab

Always update `main` before creating the new lab branch:

```bash
cd ~/comp590/Dimitri_cognata
git switch main
git pull --ff-only
git switch -c lab<NUMBER>
mkdir lab<NUMBER>
```

Example for Lab 3:

```bash
git switch main
git pull --ff-only
git switch -c lab3
mkdir lab3
```

- `git switch main` moves to the main branch.
- `git pull --ff-only` safely downloads new commits without creating an unexpected merge commit.
- `git switch -c lab3` creates and switches to the new branch.

The same workflow using traditional commands is:

```bash
git checkout main
git pull --ff-only
git checkout -b lab3
mkdir lab3
```

## 5. Record Work with Asciinema

Start a new recording:

```bash
asciinema rec lab<NUMBER>/L<NUMBER>.cast
```

Stop the recording:

```bash
exit
```

Append more work to the same recording:

```bash
asciinema rec --append lab<NUMBER>/L<NUMBER>.cast
```

Example:

```bash
asciinema rec --append lab3/L3.cast
```

## 6. Inspect Changes Before Committing

```bash
git status                 # Show changed, staged, and untracked files
git diff                   # Show unstaged changes
git diff --staged          # Show changes ready to be committed
git log --oneline -10      # Show the latest 10 commits
```

## 7. Stage and Commit

Stage everything inside the repository:

```bash
git add -A
```

Check what is staged:

```bash
git status
git diff --staged
```

Create a checkpoint commit:

```bash
git commit -m "Complete Lab <NUMBER> task <TASK_NUMBER>"
```

Example:

```bash
git commit -m "Complete Lab 3 task 1 setup"
```

## 8. Push to GitHub

The first push of a new branch sets its upstream:

```bash
git push -u origin lab<NUMBER>
```

Example:

```bash
git push -u origin lab3
```

After the first push, use:

```bash
git push
```

Recommended checkpoint cycle after each task:

```bash
exit
git status
git add -A
git commit -m "Complete Lab 3 task 2 PyChess"
git push
asciinema rec --append lab3/L3.cast
```

## 9. Pull Request

After completing and pushing the lab:

1. Open the repository on GitHub.
2. Click **Compare & pull request**.
3. Confirm the base branch is `main`.
4. Confirm the compare branch is `lab<NUMBER>`.
5. Add a useful title and description.
6. Click **Create pull request**.

Do not merge the pull request yourself unless the instructor expects you to.

## 10. Git Submodules

A submodule places an external Git repository inside your repository while keeping its history separate.

Add a submodule:

```bash
git submodule add <REPOSITORY_URL> lab<NUMBER>/<FOLDER_NAME>
```

Example:

```bash
git submodule add https://github.com/pychess/pychess.git lab3/pychess
```

Inspect submodules:

```bash
cat .gitmodules
git submodule status
```

Initialize submodules after cloning normally:

```bash
git submodule update --init --recursive
```

Important: the main repository records the submodule URL and exact commit. Files you create for the lab, such as screenshots, should normally remain directly inside `lab<NUMBER>` rather than inside somebody else's submodule.

## 11. Safe Corrections

Unstage a file without deleting it:

```bash
git restore --staged <FILE>
```

Restore a tracked file to its last committed version:

```bash
git restore <FILE>
```

Warning: `git restore <FILE>` discards uncommitted changes in that file.

Correct the most recent commit message before pushing:

```bash
git commit --amend -m "Correct commit message"
```

See exactly where you are:

```bash
git branch --show-current
git status
git log --oneline --decorate -10
```

## 12. End-of-Lab Checklist

```bash
git status
git add -A
git commit -m "Complete Lab <NUMBER>"
git push
git status
```

Confirm that:

- The `.cast` recording is inside the correct lab folder.
- Screenshots and required artifacts are present.
- `git status` says the working tree is clean.
- The lab branch appears on GitHub.
- A pull request from the lab branch to `main` has been created.

## Fast Everyday Reference

```bash
cd ~/comp590/Dimitri_cognata
git switch main
git pull --ff-only
git switch -c lab<NUMBER>
mkdir lab<NUMBER>
asciinema rec lab<NUMBER>/L<NUMBER>.cast

# Complete a task, then type: exit

git add -A
git commit -m "Complete Lab <NUMBER> task <TASK_NUMBER>"
git push -u origin lab<NUMBER>   # First push only

# Continue recording later
asciinema rec --append lab<NUMBER>/L<NUMBER>.cast

# Later pushes
git add -A
git commit -m "Complete Lab <NUMBER> task <TASK_NUMBER>"
git push
```
