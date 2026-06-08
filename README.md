# 🎲 Coldcrow's Dice Tower

A lightweight **digital dice tower** built for a custom D&D 5e mechanic (**“Moon Sugar”**), then expanded into a general-purpose roller because it was already halfway there.

---

## 📌 Version & Author

- 🏷️ **Version:** 1.2  
- ✍️ **Author:** Coldcrow  
- 🪟 **Platform:** Windows 11

---

## 🧠 What This Is

This project is intentionally **small** and a bit **niche**. There are plenty of online dice rollers that are objectively more feature-rich. This exists because it made one specific table mechanic *fast* and *easy*, and the rest of the app naturally grew from that foundation.

---

## ✨ Features

### 🎲 Standard Roller
Roll classic dice expressions in `NdM`, `NdM+K`, or `NdM-K` form:

- `1D20+5`
- `4D6-2`
- `2D8+3`

Input is **case-insensitive** and **whitespace-tolerant**, so `1d20+5`, `1D20+5`, and `1 D 20 + 5` are all valid. Anything that isn't a well-formed roll is rejected safely.

The standard roller:
- 🎲 Rolls the specified dice
- ➕➖ Applies a modifier
- 🧾 Lists each die result and outputs the total
- 🔁 Loops for repeated rolls; enter `q` to return to the menu

---

### 🧩 Premade / Custom Roller
A menu-driven roller intended for a custom Moonsugar mechanic.

> ⚠️ **Note:** In the current version, custom rollers are **hardcoded**.  
> This would be *much* more useful if end users could define their own custom roller functions without requiring a recompile.

---

## 🚀 How to Use

1. 📥 Download either:
   - 🪟 the **Windows EXE** — just double-click `Coldcrow's Dice Tower.exe`, or  
   - 🐍 the **Python source code** — run `python DiceTower_Main.py` (Python 3, Windows 11)
2. ▶️ Run the application.
3. 🧭 From the menu, select your roller.
4. 📺 Follow the on-screen prompts.