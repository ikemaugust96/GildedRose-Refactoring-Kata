# GitHub Copilot Instructions for Gilded Rose Kata

## Project Overview

This repository contains implementations of the **Gilded Rose Refactoring Kata** in multiple programming languages. The kata is an exercise in refactoring legacy code while maintaining its behavior through comprehensive test coverage.

## Kata Context

The Gilded Rose is a fictional inn that needs an inventory management system. Items have:

- **name**: The item's name
- **sell_in**: Days remaining to sell the item
- **quality**: A value (0-50) representing item quality

Quality rules vary by item type:

- Normal items: Quality decreases by 1 per day
- Aged Brie: Quality increases by 1 per day
- Sulfuras (legendary): Quality never changes
- Backstage passes: Quality increases, with special rules near concert date
- Conjured items: Quality decreases twice as fast

## Code Structure

Each language directory (Python, Java, C#, etc.) contains:

- `gilded_rose.*` - Main implementation
- `test_gilded_rose.*` or similar - Test suite
- `README.md` - Language-specific instructions

## When Helping with Refactoring

1. **Preserve behavior**: All existing tests must pass before and after refactoring
2. **Use appropriate patterns**: Suggest language-idiomatic solutions (e.g., Strategy pattern, polymorphism)
3. **Improve readability**: Break down complex conditional logic
4. **Maintain test coverage**: Ensure tests remain comprehensive during refactoring
5. **Language conventions**: Follow the conventions and best practices of the specific language

## Key Refactoring Goals

- Eliminate nested conditionals
- Separate concerns (different item types)
- Make the code easier to extend with new item types
- Improve testability and maintainability

## Common Patterns Used

- **Factory Pattern**: Creating item updaters based on item type
- **Strategy Pattern**: Different update strategies for different items
- **Polymorphism**: Using inheritance/interfaces for item-specific behavior

## Testing Requirements

- Run existing tests before and after refactoring
- Add tests for edge cases (quality bounds, sell_in transitions)
- Verify no behavior changes occur during refactoring

## Do Not

- Change the public interface of `GildedRose` class/function
- Modify test files (they verify correct behavior)
- Skip the characterization test phase
