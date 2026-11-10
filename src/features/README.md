# How to add features!

Chescript dynamically loads packages contained in [`./feature_code`](./feature_code/). 

Essentially, it loads in every package in that folder, runs `get_value()` that returns a value (`bool`, `int`, or `float` as seen in [the Feature class](../classes/module.py)), and collates it into a list of features (seen in [the Entry class](../classes/module.py).)

**To TL;DR the creation of a new feature**:

1. **Copy-paste** the [`./feature_code/example` folder](./feature_code/example) into [the same `./feature_code` folder](./feature_code/).

2. Rename the new folder into the **actual name of the feature**. (This is what the feature will be named in the final CSV file).

3. Modify `get_value()` in `module.py` to create each feature.

You may add as many helper functions as necessary in `module.py` (and other `.py` files you may make), so long as `get_value()` remains callable by the main feature generation function.