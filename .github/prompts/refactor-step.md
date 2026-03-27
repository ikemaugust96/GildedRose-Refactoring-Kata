# Gilded Rose Refactoring Step-by-Step

## Overview

This prompt guides you through refactoring the Gilded Rose kata incrementally while maintaining test coverage.

## Step 1: Understand Current State

- [ ] Review the existing `gilded_rose.py` implementation
- [ ] Run all tests: `python -m pytest test_gilded_rose.py -v`
- [ ] Verify all tests pass before making changes
- [ ] Identify the nested conditionals that need refactoring

## Step 2: Choose Refactoring Pattern

Select the most appropriate pattern for your language:

### Python: Factory + Strategy Pattern

- Create an abstract `ItemUpdater` base class
- Implement updater subclasses for each item type:
  - `NormalItemUpdater`
  - `AgedBrieUpdater`
  - `SulfurasUpdater`
  - `BackstagePassUpdater`
  - `ConjuredItemUpdater`
- Create `ItemUpdaterFactory` to return appropriate updater
- Update `GildedRose.update_quality()` to use factory

### Other Languages: Polymorphism/Inheritance

- Use language-appropriate abstraction (interfaces, abstract classes)
- Separate item type logic into distinct classes
- Implement factory or switch-based dispatch

## Step 3: Extract First Item Type

1. Create updater class for one item type (e.g., Normal items)
2. Move logic from nested conditionals to the new class
3. Run tests after each small change
4. Verify behavior is identical

## Step 4: Repeat for Remaining Types

1. Extract one item type at a time
2. Run tests after each extraction
3. Maintain test pass rate at 100%
4. Refactor incrementally

## Step 5: Create Factory

1. Build factory method/class to dispatch to correct updater
2. Update `GildedRose.update_quality()` to use factory
3. Remove all nested conditionals
4. Run full test suite

## Step 6: Refine and Optimize

- [ ] Remove code duplication between updaters
- [ ] Add type hints (Python)
- [ ] Improve readability with better variable names
- [ ] Consider extracting common quality update logic
- [ ] Run tests after each refinement

## Step 7: Add Edge Case Tests

- [ ] Test quality bounds (0-50)
- [ ] Test sell_in date transitions
- [ ] Test special cases (Sulfuras never changes)
- [ ] Test conjured items (double decay)
- [ ] All new tests should pass

## Step 8: Validate

- [ ] All original tests pass
- [ ] All new tests pass
- [ ] No public interface changes
- [ ] Code is more readable and maintainable
- [ ] Adding new item types is straightforward

## Key Constraints

- ✅ Preserve `GildedRose` public interface
- ✅ Preserve `Item` class structure
- ✅ Keep test files unchanged
- ✅ Maintain 100% test pass rate
- ✅ Follow language conventions

## Quality Rules Reference

Use these when implementing updaters:

| Item Type | Quality Change | Special Rules                                 |
| --------- | -------------- | --------------------------------------------- |
| Normal    | -1/day         | Min 0, Max 50                                 |
| Aged Brie | +1/day         | Min 0, Max 50                                 |
| Sulfuras  | 0              | Never changes                                 |
| Backstage | Varies         | +1 (>10d), +2 (≤10d), +3 (≤5d), 0 (expired) |
| Conjured  | -2/day         | Min 0, Max 50                                 |

## Testing Commands

```bash
# Run all tests
python -m pytest test_gilded_rose.py -v

# Run specific test
python -m pytest test_gilded_rose.py::test_name -v

# Run with coverage
python -m pytest test_gilded_rose.py --cov=gilded_rose
```
